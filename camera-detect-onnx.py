from ultralytics import YOLO
import cv2

# Load ONNX model
model = YOLO("best.onnx")  # pastikan file ini ada di folder project

# Buka kamera (0 = kamera laptop)
cap = cv2.VideoCapture(0)

# Resolusi opsional (biar lebih ringan)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat mengakses kamera!")
        break

    # Deteksi dengan ONNX
    results = model(frame)

    # Gambar bounding box
    annotated = results[0].plot()

    cv2.imshow("PPE Detection - ONNX Camera", annotated)

    # Tekan Q untuk berhenti
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
