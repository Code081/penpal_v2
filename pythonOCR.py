import pytesseract
from PIL import Image
import cv2
from gtts import gTTS
# from playsound import playsound

image_1 = cv2.imread('./Tests/Image 1.png')
# image_2 = cv2.imread('image_2.png')
# image_3 = cv2.imread('image_3.png')

# cv2.imshow('Image 1', image_1)
# cv2.imshow('Image 2', image_2)
# cv2.imshow('Image 3', image_3)

print(pytesseract.image_to_string(image_1))

cv2.waitKey(0)