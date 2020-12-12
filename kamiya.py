#画像のダウンロード
import urllib.request as req 
url = "../image/kamiyaface.jpg"
req.urlretrieve(url,"test.png")

#opencvで読み込む
import cv2
img = cv2.imread("test.png")
print(img)