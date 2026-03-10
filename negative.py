import cv2
import numpy as np

# Transformasi Linier (Negative Image) menggunakan HSV
img = cv2.imread('Image.jpg')

if img is not None:
    t, l = img.shape[:2]
    img_resize = cv2.resize(img, (400, int((400 / l) * t)))

    # 1. Konversi dari BGR ke HSV
    hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    
    # 2. Pisahkan channel Hue (Warna), Saturation (Kepekatan), dan Value (Kecerahan)
    h, s, v = cv2.split(hsv)

    # 3. Terapkan rumus Negative HANYA pada channel V (Kecerahan)
    v_neg_255 = 255 - v
    v_neg_128 = np.clip(128 - v.astype(np.int16), 0, 255).astype(np.uint8)

    # 4. Gabungkan kembali channel H dan S asli dengan V yang sudah diproses
    hsv_255 = cv2.merge([h, s, v_neg_255])
    hsv_128 = cv2.merge([h, s, v_neg_128])

    # 5. Kembalikan ke format BGR agar bisa ditampilkan dengan warna yang benar
    hasil_255 = cv2.cvtColor(hsv_255, cv2.COLOR_HSV2BGR)
    hasil_128 = cv2.cvtColor(hsv_128, cv2.COLOR_HSV2BGR)

    # Gabungkan gambar
    hasil = np.hstack((img_resize, hasil_255, hasil_128))
    cv2.imshow('Soal 1: Citra Asli | Negative 255 | Negative 128', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar Image.jpg tidak ditemukan.")