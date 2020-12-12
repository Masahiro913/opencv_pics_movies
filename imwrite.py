import cv2

#画像を読み込む
img = cv2.imread("test.png")

#画像を保存する
cv2.imwrite("out.jpeg", img)

# BMP/PPM/PGM/PBM/JPEG/JPEG2000/PNG/TIFF/OpenEXR/WebPをサポートしている