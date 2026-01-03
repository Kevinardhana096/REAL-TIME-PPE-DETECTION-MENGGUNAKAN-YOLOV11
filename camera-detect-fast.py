"""
camera-detect-fast.py
Optimized real-time camera detection using Ultralytics YOLO with a producer-consumer queue.
Features:
- Separate capture thread to avoid blocking on inference
- Drop frames when queue is full (keeps stream live)
- Resize frames before inference to reduce compute
- Optional GPU + half precision if CUDA available
- FPS counter and periodic logging

Run:
./venv/Scripts/python.exe camera-detect-fast.py

Adjust `TARGET_WIDTH` / `TARGET_HEIGHT` and `CONF_THRESHOLD` to trade-off speed/accuracy.
"""

from ultralytics import YOLO
import cv2
from threading import Thread
from queue import Queue
import time
import sys

# Configuration
MODEL_PATH = "best.onnx"       # your model checkpoint
TARGET_WIDTH = 640            # resize width for inference (lower -> faster)
TARGET_HEIGHT = 360           # resize height for inference
CONF_THRESHOLD = 0.15         # confidence threshold
IOU_THRESHOLD = 0.45
QUEUE_SIZE = 1                # keep only the latest frame
LOG_EVERY_N_FRAMES = 60

# Capture thread reads frames continuously and pushes to a small queue
class CameraCapture(Thread):
    def __init__(self, src=0, queue_size=1):
        super().__init__(daemon=True)
        self.cap = cv2.VideoCapture(src)
        self.q = Queue(maxsize=queue_size)
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("[capture] failed to read frame")
                self.running = False
                break
            # If queue full, drop the oldest (non-blocking behavior)
            if self.q.full():
                try:
                    _ = self.q.get_nowait()
                except Exception:
                    pass
            self.q.put(frame)
        self.cap.release()

    def read(self, timeout=0.01):
        try:
            return self.q.get(timeout=timeout)
        except Exception:
            return None

    def stop(self):
        self.running = False


def main():
    # Load model
    print("Loading model:", MODEL_PATH)
    model = YOLO(MODEL_PATH)

    # Try to move model to CUDA and enable half precision if available
    try:
        # This will raise if CUDA not available for this build
        import torch
        if torch.cuda.is_available():
            print("CUDA available -> moving model to GPU and enabling half precision")
            # ultralytics YOLO wrapper sets device per-call, but calling .to may help
            try:
                model.to('cuda')
            except Exception:
                pass
            use_half = True
        else:
            print("CUDA not available -> running on CPU")
            use_half = False
    except Exception:
        print("torch not available or cannot check CUDA; defaulting to CPU")
        use_half = False

    # Start camera capture thread
    cam = CameraCapture(src=0, queue_size=QUEUE_SIZE)
    cam.start()

    win_name = "PPE Detection - Fast"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    frame_count = 0
    t_start = time.time()
    last_log = time.time()

    try:
        while True:
            frame = cam.read()
            if frame is None:
                # nothing new, small sleep to avoid busy loop
                time.sleep(0.005)
                continue

            # Resize frame for faster inference (keep a copy for display)
            h, w = frame.shape[:2]
            resized = cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT))

            # Run inference (pass small imgsz to inference to be explicit)
            results = model(resized, conf=CONF_THRESHOLD, iou=IOU_THRESHOLD, verbose=False)

            annotated = results[0].plot()

            # Upscale annotated back to window size for display (optional)
            annotated_display = cv2.resize(annotated, (w, h))

            # FPS calculation
            frame_count += 1
            elapsed = time.time() - t_start
            fps = frame_count / elapsed if elapsed > 0 else 0.0

            # Draw FPS and simple overlay
            cv2.putText(annotated_display, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(annotated_display, f"Conf: {CONF_THRESHOLD}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

            cv2.imshow(win_name, annotated_display)

            # Periodic logging
            if frame_count % LOG_EVERY_N_FRAMES == 0:
                print(f"Processed {frame_count} frames, FPS ~ {fps:.2f}")
                # print some detections summary
                dets = results[0].boxes
                if len(dets) > 0:
                    for box in dets:
                        try:
                            cls = int(box.cls[0])
                            conf = float(box.conf[0])
                            name = model.names[cls]
                            print(f"  - {name}: {conf:.2f}")
                        except Exception:
                            pass
                else:
                    print("  - no detections in last frame")

            # Exit on 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        cam.stop()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
