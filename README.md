# PPE Detection dengan YOLOv11

📄 **Academic Paper**: Full LaTeX paper available in `paper/` directory - ready for conference submission!

## ⚠️ Mengapa Tidak Ada Bounding Box di Kamera?

### Model Sudah Terlatih dengan Baik ✓
Berdasarkan hasil validasi dari notebook:
- **mAP50**: 57.47% 
- **Precision**: 63.53%
- **Recall**: 49.07%

Model **BISA mendeteksi** seperti terlihat di output cell 20 notebook yang menunjukkan bounding box yang jelas pada test images.

### Penyebab Tidak Ada Deteksi di Kamera:

1. **Model dilatih untuk objek PPE construction khusus:**
   - Helmet (safety helmet warna terang)
   - Vest (high-visibility vest)
   - Boots (safety boots)
   - Gloves (sarung tangan kerja)
   - Goggles (kacamata safety)

2. **Performa per-class bervariasi:**
   ```
   helmet      : mAP50 = 0.863 ✓ BAIK
   vest        : mAP50 = 0.847 ✓ BAIK
   Person      : mAP50 = 0.901 ✓ BAIK
   gloves      : mAP50 = 0.823 ✓ BAIK
   boots       : mAP50 = 0.785 ✓ BAIK
   no_helmet   : mAP50 = 0.461 ⚠️ RENDAH
   no_goggle   : mAP50 = 0.000 ❌ TIDAK BISA DETEKSI
   no_boots    : mAP50 = 0.000 ❌ TIDAK BISA DETEKSI
   ```

3. **Kondisi real-time berbeda dari training data:**
   - Training images: foto construction site dengan pencahayaan dan angle tertentu
   - Kamera Anda: mungkin indoor, pencahayaan berbeda, tidak ada PPE equipment

## 🧪 Cara Testing

### 1. Test dengan Gambar Statis
```bash
./venv/Scripts/python.exe test-image-detect.py
```

### 2. Test dengan Kamera (sudah diperbaiki)
```bash
./venv/Scripts/python.exe camera-detect.py
```
Script sudah ditingkatkan dengan:
- ✓ Confidence threshold lebih rendah (0.15 dari 0.25)
- ✓ Info jumlah deteksi di layar
- ✓ Logging setiap 30 frame
- ✓ Display class yang terdeteksi

### 3. Untuk Mendapatkan Deteksi yang Bagus:

**Opsi A: Gunakan PPE Equipment Nyata**
- Pakai safety helmet
- Pakai safety vest (rompi oranye/kuning)
- Pakai boots & gloves
- Pastikan pencahayaan cukup

**Opsi B: Tunjukkan Gambar PPE di Layar**
- Cari foto construction worker di Google
- Tampilkan di layar/tablet
- Arahkan kamera ke gambar tersebut

**Opsi C: Retrain dengan Data Anda**
- Ambil foto dengan kamera Anda sendiri
- Label dengan Roboflow/CVAT
- Train ulang model

## 📊 Hasil Training

Dataset: Construction-PPE dari Ultralytics
- Training images: ~572 gambar
- Validation images: 143 gambar
- Classes: 11 (helmet, gloves, vest, boots, goggles, none, Person, no_helmet, no_goggle, no_gloves, no_boots)
- Epochs: 200 (dengan early stopping)
- Model: YOLOv11n (Nano - 2.5M parameters)

## 🎯 Kesimpulan

Model **BERFUNGSI dengan BAIK** untuk dataset yang dia pelajari. Tidak ada deteksi di kamera Anda karena:
- ❌ Tidak ada PPE equipment di frame
- ❌ Objek berbeda dari training data
- ❌ Kondisi pencahayaan/angle berbeda

**Ini NORMAL dan EXPECTED!** Model object detection hanya mendeteksi objek yang mirip dengan training data.
