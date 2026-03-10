import cv2
import numpy as np

img = cv2.imread('Image.jpg')

if img is not None:
    t, l = img.shape[:2]
    img_resize = cv2.resize(img, (400, int((400 / l) * t)))

    hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_float = v.astype(np.float32)

    v_inv_30 = np.clip(30 * np.log1p(255 - v_float), 0, 255).astype(np.uint8)
    v_inv_50 = np.clip(50 * np.log1p(255 - v_float), 0, 255).astype(np.uint8)

    hasil_30 = cv2.cvtColor(cv2.merge([h, s, v_inv_30]), cv2.COLOR_HSV2BGR)
    hasil_50 = cv2.cvtColor(cv2.merge([h, s, v_inv_50]), cv2.COLOR_HSV2BGR)

    hasil = np.hstack((img_resize, hasil_30, hasil_50))
    cv2.imshow('Soal 3: Citra Asli | Inv Log C=30 | Inv Log C=50', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()