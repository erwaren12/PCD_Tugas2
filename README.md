# Tugas Pengolahan Citra Digital (PCD) - Transformasi Citra

Repositori ini berisi implementasi algoritma **Transformasi Tingkat Keabuan** menggunakan bahasa pemrograman Python, *library* OpenCV, dan Matplotlib. Seluruh kode disajikan dalam format interaktif Jupyter Notebook (`.ipynb`) sehingga gambar hasil pengolahan citra dapat langsung dilihat di dalam dokumen tanpa memerlukan jendela *pop-up* eksternal.

Berdasarkan materi perkuliahan, repositori ini mengimplementasikan empat jenis transformasi:
1. Transformasi Linier (Negative Image)
2. Transformasi Logaritmik
3. Transformasi Inverse Logaritmik
4. Transformasi Power-Law ($n^{th}$ power)

### 🌟 Pendekatan Khusus: Pemrosesan Ruang Warna HSV
Untuk mencegah efek klise pada warna asli (distorsi warna), citra berwarna (BGR) dikonversi terlebih dahulu ke ruang warna **HSV (Hue, Saturation, Value)**. Rumus matematika hanya diaplikasikan pada saluran **V (Value/Kecerahan)**, sementara warna dasar (Hue) dan kepekatan (Saturation) dibiarkan utuh. Setelah diproses, gambar dikonversi ke format RGB agar warna tetap natural saat dirender oleh Matplotlib.

## 📁 Struktur File

* **`negative.ipynb`**: Implementasi *Negative Image* ($G = L - F$).
* **`logaritmik.ipynb`**: Implementasi Transformasi Logaritmik ($G = c \cdot \log(F + 1)$).
* **`inverse_logaritmik.ipynb`**: Implementasi Transformasi Inverse Logaritmik ($G = c \cdot \log(L - F + 1)$).
* **`power_law.ipynb`**: Implementasi Transformasi Power Law ($G = c \cdot F^y$).
* **`Image.jpg`**: Citra sampel yang digunakan sebagai bahan uji coba pengolahan.

## 🛠️ Persyaratan Sistem

Pastikan *library* berikut sudah terinstal di *environment* komputer Anda sebelum menjalankan *notebook*:
```bash
pip install opencv-python numpy matplotlib ipykernel
