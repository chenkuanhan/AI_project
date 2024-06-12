```
(base) PS C:\Users\Asus\Documents\AI_Code> python '.\Bounding Box.py'
[ WARN:0@0.012] global loadsave.cpp:241 cv::findDecoder imread_('input_image.jpg'): can't open/read file: check file path/integrity
Traceback (most recent call last):
  File "C:\Users\Asus\Documents\AI_Code\Bounding Box.py", line 21, in <module>
    cv2.imshow("標過後的",image)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:973: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
```
