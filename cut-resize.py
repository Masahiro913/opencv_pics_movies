#画像の１部分だけを切り取ってリサイズ
import matplotlib.pyplot as plt
import cv2

#画像を読み込む
img = cv2.imread("test.png")
#画像の一部分を切り取る  *画像の左上が(0,0)となる座標軸
im2 = img[150:450, 150:450]
#画像をリサイズ
im2 = cv2.resize(im2, (400,400))
#リサイズした画像を保存
cv2.imwrite("cut-resize.png",im2)

#画像を表示
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()