import cv2

# 讀取影像
image = cv2.imread('nono_han.jpg')

# 假設這裡有一個訓練好的目標檢測模型，可以使用模型來檢測影像中的物體
# 在這裡假設檢測結果存儲在detections列表中，每個檢測結果包含物體的類別、分數和Bounding Box的位置信息

# 假設 detections 是一個列表，每個元素是一個 tuple，包含了 (class_id, confidence, x, y, w, h)
# class_id 是物體的類別，confidence 是檢測分數，(x, y) 是Bounding Box的左上角座標，w 和 h 是寬度和高度

# 繪製Bounding Box
for detection in detections:
    class_id, confidence, x, y, w, h = detection
    color = (0, 255, 0)  # Bounding Box的顏色，這裡選擇綠色
    thickness = 2  # Bounding Box的線條寬度
    cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

# 顯示標註後的影像
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
