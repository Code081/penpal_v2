import pytesseract
from PIL import Image
import cv2
from gtts import gTTS
# from playsound import playsound

image_1 = cv2.imread('./Tests/Image 1.png')

height, width, _ = image_1.shape


# image_2 = cv2.imread('image_2.png')
# image_3 = cv2.imread('image_3.png')

cv2.imshow('Image 1', image_1)
# cv2.imshow('Image 2', image_2)
# cv2.imshow('Image 3', image_3)

print(pytesseract.image_to_string(image_1))

character_box = pytesseract.image_to_boxes(image_1)

for a in character_box.splitlines():
    a = a.split(' ')
    print(a)
    x, y, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])
    cv2.rectangle(image_1, (x, height-y), (w, height-h), (0, 0, 255), 1)
    
    # putting text
    cv2.putText(image_1, a[0], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 2)
    
cv2.imshow('Image 1', image_1)

cv2.waitKey(0)