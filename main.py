import cv2
import numpy as np

img = cv2.imread('Image.jpg')

if img is not None:
    t, l = img.shape[:2]
    img_resize = cv2.resize(img, (400, int((400 / l) * t)))

    hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_float = v.astype(np.float32)

    img_asli = img_resize.copy()
    cv2.putText(img_asli, "Citra Asli", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    v_neg = 255 - v
    img_neg = cv2.cvtColor(cv2.merge([h, s, v_neg]), cv2.COLOR_HSV2BGR)
    cv2.putText(img_neg, "Negative L=255", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    v_log = np.clip(50 * np.log1p(v_float), 0, 255).astype(np.uint8)
    img_log = cv2.cvtColor(cv2.merge([h, s, v_log]), cv2.COLOR_HSV2BGR)
    cv2.putText(img_log, "Log c=50", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    v_inv_log = np.clip(50 * np.log1p(255 - v_float), 0, 255).astype(np.uint8)
    img_inv_log = cv2.cvtColor(cv2.merge([h, s, v_inv_log]), cv2.COLOR_HSV2BGR)
    cv2.putText(img_inv_log, "Inv Log c=50", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    v_pow1 = np.clip(1.0 * np.power(v_float, 0.9), 0, 255).astype(np.uint8)
    img_pow1 = cv2.cvtColor(cv2.merge([h, s, v_pow1]), cv2.COLOR_HSV2BGR)
    cv2.putText(img_pow1, "Power Law c=1.0, y=0.9", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    v_pow2 = np.clip(1.5 * np.power(v_float, 0.7), 0, 255).astype(np.uint8)
    img_pow2 = cv2.cvtColor(cv2.merge([h, s, v_pow2]), cv2.COLOR_HSV2BGR)
    cv2.putText(img_pow2, "Power Law c=1.5, y=0.7", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    baris_1 = np.hstack((img_asli, img_neg, img_log))
    baris_2 = np.hstack((img_inv_log, img_pow1, img_pow2))
    
    gabungan_grid = np.vstack((baris_1, baris_2))

    cv2.imshow('Rangkuman Transformasi (main.py)', gabungan_grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar Image.jpg tidak ditemukan.")