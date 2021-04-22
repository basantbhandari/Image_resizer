import cv2
import os

source = "/home/basant/Downloads/GAN_WORKSPACE/minor project/paper writing on minor project/performance_parameter/real_36"
destination = "/home/basant/Downloads/GAN_WORKSPACE/minor project/paper writing on minor project/performance_parameter/real_36_resized"



IMG_SIZE = 64

for img in os.listdir(source):
    img_array = cv2.imread(os.path.join(source, img), cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(destination, img), resized)
















