# Tugas Pengolahan Citra Digital (PCD) - Transformasi Citra

[cite_start]Repositori ini berisi implementasi algoritma **Transformasi Tingkat Keabuan** [cite: 1] menggunakan bahasa pemrograman Python dan *library* OpenCV. 

[cite_start]Berdasarkan materi perkuliahan, repositori ini mengimplementasikan empat jenis transformasi[cite: 45]:
1. [cite_start]Transformasi Linier (Negative Image) [cite: 46]
2. [cite_start]Transformasi Logaritmik [cite: 47]
3. [cite_start]Transformasi Inverse Logaritmik [cite: 47]
4. [cite_start]Transformasi Power-Law ($n^{th}$ power) [cite: 48]

### 🌟 Pendekatan Khusus: Pemrosesan Ruang Warna HSV
Untuk mencegah efek klise pada warna asli (distorsi warna), citra berwarna (BGR) dikonversi terlebih dahulu ke ruang warna **HSV (Hue, Saturation, Value)**. Rumus matematika hanya diaplikasikan pada saluran **V (Value/Kecerahan)**, sementara warna dasar (Hue) dan kepekatan (Saturation) dibiarkan utuh. Setelah diproses, gambar dikembalikan ke format BGR agar warna tetap natural.

## 📁 Struktur File

* [cite_start]**`negative.py`**: Implementasi *Negative Image* ($G = L - F$)[cite: 68, 70].
* [cite_start]**`logaritmik.py`**: Implementasi Transformasi Logaritmik ($G = c \cdot \log(F + 1)$)[cite: 82, 84].
* [cite_start]**`inverse_logaritmik.py`**: Implementasi Transformasi Inverse Logaritmik ($G = c \cdot \log(L - F + 1)$)[cite: 85, 86].
* **`power_low.py`**: Implementasi Transformasi Power Law ($G = c \cdot F^y$)[cite: 109, 112].
* **`main.py`**: Program utama interaktif/rangkuman yang mengintegrasikan seluruh metode transformasi di atas dalam satu jendela.
* **`Image.jpg`**: Citra sampel yang digunakan sebagai bahan uji coba pengolahan.

## 🛠️ Persyaratan Sistem

Pastikan *library* berikut sudah terinstal di komputer Anda:
```bash
pip install opencv-python numpy
