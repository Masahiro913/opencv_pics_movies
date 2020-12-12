# ダウンロードした画像を画面に表示する
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("test.png")
plt.axis("off") #軸を消して画像だけ表示する
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()