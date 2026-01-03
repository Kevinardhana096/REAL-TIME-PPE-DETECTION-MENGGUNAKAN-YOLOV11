# LaTeX Paper: PPE Detection using YOLOv11

Paper lengkap untuk proyek deteksi Personal Protective Equipment (PPE) menggunakan YOLOv11.

## 📁 Struktur File

```
paper/
├── main.tex           # File LaTeX utama (paper lengkap)
├── references.bib     # Database referensi (BibTeX)
└── README_LATEX.md    # Panduan ini
```

## 📄 Isi Paper

Paper ini mencakup:

1. **Abstract** - Ringkasan penelitian dan hasil
2. **Introduction** - Latar belakang dan kontribusi
3. **Related Work** - Review arsitektur object detection dan PPE detection
4. **Methodology**
   - Dataset (Construction-PPE, 572 training images, 11 classes)
   - Model Architecture (YOLOv11-Large)
   - Training Configuration
   - Evaluation Metrics
   - Optimization Strategies
5. **Experiments and Results**
   - Training results
   - Overall performance (mAP@50: 57.47%, Precision: 63.53%)
   - Per-class performance analysis
   - Inference speed benchmarks
6. **Discussion** - Analisis mendalam performa dan limitasi
7. **Future Work** - Pengembangan lebih lanjut
8. **Conclusion** - Kesimpulan penelitian

## 🖼️ Figures Included (7 images)

1. **Figure 1** (output1.png) - Sample images from training dataset
2. **Figure 2** (output2.png) - Class distribution in training set
3. **Figure 3** (output3.png) - Training curves (loss, mAP, precision, recall)
4. **Figure 4** (output4.png) - Confusion matrix (normalized)
5. **Figure 5** (output5.png) - Precision-Recall curves for all classes
6. **Figure 6** (output6.png) - Sample detection results on test images
7. **Figure 7** (output7.png) - Real-time camera inference demonstration

## 🔧 Cara Kompilasi

### Opsi 1: Overleaf (Recommended - Paling Mudah)

1. Buka [Overleaf](https://www.overleaf.com/)
2. Klik "New Project" → "Upload Project"
3. Upload semua file di folder `paper/`
4. Overleaf akan otomatis compile
5. Download PDF hasil kompilasi

### Opsi 2: Local LaTeX Installation

**Windows:**
```bash
# Install MiKTeX: https://miktex.org/download

# Compile dengan pdflatex
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Linux/Mac:**
```bash
# Install TeX Live
# Ubuntu/Debian: sudo apt-get install texlive-full
# Mac: brew install --cask mactex

# Compile
cd paper
pdflatex main.tex
bibtex main.tex
pdflatex main.tex
pdflatex main.tex
```

**Mengapa 3x pdflatex?**
- Run 1: Generate auxiliary files
- bibtex: Process citations
- Run 2: Integrate citations
- Run 3: Resolve cross-references

### Opsi 3: Online LaTeX Editors

- **Overleaf**: https://www.overleaf.com/ (Recommended)
- **Papeeria**: https://papeeria.com/
- **CoCalc**: https://cocalc.com/

## 📊 Mengubah/Menyesuaikan Paper

### Ganti Informasi Penulis

Edit baris 18-23 di `main.tex`:

```latex
\author{\IEEEauthorblockN{Your Name}
\IEEEauthorblockA{\textit{Department/Faculty} \\
\textit{University Name}\\
City, Country \\
email@university.edu}
}
```

### Tambah Gambar/Grafik

Untuk menambahkan gambar hasil training (confusion matrix, PR curve, dll):

1. Export gambar dari notebook (.png atau .pdf)
2. Letakkan di folder `paper/`
3. Tambahkan di LaTeX:

```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.48\textwidth]{confusion_matrix.png}
\caption{Confusion Matrix dari Model YOLOv11-Large}
\label{fig:confusion}
\end{figure}
```

### Update Hasil Eksperimen

Jika Anda retrain model dan mendapat hasil berbeda, update:

- Tabel 2 (Overall Performance) - baris ~268-279
- Tabel 3 (Per-Class Performance) - baris ~285-303
- Angka dalam text di section Results

### Tambah Referensi

Tambahkan entry baru di `references.bib`:

```bibtex
@article{author2024title,
  title={Title of Paper},
  author={Author Name},
  journal={Journal Name},
  year={2024}
}
```

Lalu cite di main.tex:
```latex
According to recent work \cite{author2024title}, ...
```

## 📝 Tips Penulisan

1. **Pastikan data konsisten** - Angka di paper harus match dengan hasil notebook
2. **Tambahkan visualisasi** - Confusion matrix, training curves, sample detections
3. **Jelaskan trade-offs** - Diskusikan mengapa beberapa class performa rendah
4. **Cantumkan limitasi** - Honest discussion tentang weaknesses
5. **Future work specific** - Berikan concrete suggestions, bukan generic

## 🎨 Format Paper

Paper menggunakan format **IEEE Conference** - standar untuk computer vision conferences seperti:
- CVPR (Computer Vision and Pattern Recognition)
- ICCV (International Conference on Computer Vision)
- ECCV (European Conference on Computer Vision)
- ICIP (International Conference on Image Processing)

Untuk format journal atau conference lain, ubah documentclass di baris 1:
```latex
% Conference
\documentclass[conference]{IEEEtran}

% Journal
\documentclass[journal]{IEEEtran}

% ACM format
\documentclass{acmart}
```

## 📦 Package Dependencies

Paper menggunakan package LaTeX berikut:
- `IEEEtran` - IEEE formatting
- `cite` - Citation management
- `amsmath`, `amssymb`, `amsfonts` - Math symbols
- `graphicx` - Image inclusion
- `booktabs` - Professional tables
- `hyperref` - Hyperlinks dalam PDF

Semua package ini standard dan included dalam TeX Live/MiKTeX.

## 🐛 Troubleshooting

**Error: "File not found"**
- Pastikan semua file (.tex, .bib) dalam satu folder
- Check nama file case-sensitive

**Error: "Undefined references"**
- Run bibtex, lalu pdflatex 2x lagi

**Error: "Package not found"**
- Update TeX distribution: `tlmgr update --all` (TeX Live) atau MiKTeX Package Manager

**Table/Figure tidak muncul di posisi yang benar**
- Gunakan `[H]` instead of `[h]`: `\begin{figure}[H]`
- Atau gunakan `[htbp]` untuk lebih flexible

## 📚 Referensi yang Digunakan

Paper ini mengutip:
- YOLO papers (YOLOv1-v4, YOLOv8, YOLOv11)
- Object detection architectures (R-CNN, Faster R-CNN, SSD)
- PPE detection literature (Nath et al., Wu et al., Fang et al.)
- Computer vision fundamentals (ResNet, FPN, CSPNet)
- Deployment tools (ONNX)

Total: ~30 referensi

## 📧 Submission Tips

Jika ingin submit ke conference/journal:

1. **Baca Call for Papers** - Check format requirements
2. **Follow page limits** - Paper ini ~8 pages (typical conference limit: 6-8)
3. **Double-check plagiarism** - Pastikan paraphrase dengan benar
4. **Add author contributions** - Jelaskan siapa yang melakukan apa
5. **Include code/data availability** - Link to GitHub jika open source

## ✅ Checklist Sebelum Submit

- [ ] Informasi penulis sudah diisi
- [ ] Semua angka hasil match dengan eksperimen
- [ ] Gambar/tabel memiliki caption yang jelas
- [ ] References lengkap dan formatted benar
- [ ] Spelling dan grammar di-check
- [ ] Paper di-compile tanpa error
- [ ] PDF readable dan tidak ada formatting issues

## 🎓 Contoh Citation Paper Ini

Jika orang lain ingin cite paper Anda:

```bibtex
@inproceedings{yourname2025ppe,
  title={Real-Time Construction Personal Protective Equipment Detection Using YOLOv11},
  author={Your Name},
  booktitle={Conference Name},
  year={2025}
}
```

---

**Good luck dengan paper Anda! 🚀**

Untuk pertanyaan, edit file `main.tex` sesuai kebutuhan atau upload ke Overleaf untuk kemudahan kolaborasi.
