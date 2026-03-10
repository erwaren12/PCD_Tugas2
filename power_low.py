import cv2
import numpy as np

img = cv2.imread('Image.jpg')

if img is not None:
    t, l = img.shape[:2]
    img_resize = cv2.resize(img, (400, int((400 / l) * t)))

    hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_float = v.astype(np.float32)

    v_pow_1 = np.clip(1.0 * np.power(v_float, 0.9), 0, 255).astype(np.uint8)
    v_pow_2 = np.clip(1.5 * np.power(v_float, 0.7), 0, 255).astype(np.uint8)

    hasil_pow_1 = cv2.cvtColor(cv2.merge([h, s, v_pow_1]), cv2.COLOR_HSV2BGR)
    hasil_pow_2 = cv2.cvtColor(cv2.merge([h, s, v_pow_2]), cv2.COLOR_HSV2BGR)

    hasil = np.hstack((img_resize, hasil_pow_1, hasil_pow_2))
    cv2.imshow('Soal 4: Citra Asli | Power Law (c=1.0, y=0.9) | Power Law (c=1.5, y=0.7)', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()