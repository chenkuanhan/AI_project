import cv2

# 載入預訓練的人臉檢測器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 讀取圖片
image = cv2.imread('nono_han.jpg')

# 將圖片轉換為灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用人臉檢測器檢測人臉
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 在圖片上繪製人臉標註
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 顯示標註後的圖片
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
