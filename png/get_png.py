from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import cv2 as cv


driver = webdriver.Chrome()
driver.get('http://192.168.1.149:5500/login')
driver.maximize_window()
time.sleep(2)
png_location ='//img'
# code_png = driver.find_element(By.XPATH, png_location).screenshot('./code_png')
driver.find_element(By.XPATH, png_location).screenshot('./master_drawing.png')

# 原图
master_drawing = cv.imread('master_drawing.png')

# 对图片进行去噪处理
denoised_picture = cv.pyrMeanShiftFiltering(master_drawing, 10, 100)
cv.imwrite("denoised_picture.png", denoised_picture)

# 对图片进行灰度处理
grayscale_picture = cv.cvtColor(denoised_picture, cv.COLOR_BGR2GRAY)
cv.imwrite("grayscale_picture.png", grayscale_picture)

# 对图片进行二值化处理（中间的符号：管道符）
threshold_vlue, binary_picture = cv.threshold(grayscale_picture, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
print(f"获取到的阙值: {threshold_vlue}")
cv.imwrite("binary_picture.png", binary_picture)



