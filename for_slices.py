import cv2

image = cv2.imread('images/kisa.jpg')

# ВНИМАНИЕ! В OpenCV первым аргументом идет ВЫСОТА!
# sliced_region = image_np[:, 50:150]

print(f'image shape = {image.shape}')

height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]

# ВНИМАНИЕ! В OpenCV первым аргументом идет ВЫСОТА!
# image[height // 2:height , 50:150] = [0, 0, 255]
# image[:height // 2, 150:200] = [255, 0, 0]

roi = image[:height // 2, :]

roi[:,:, 0] = 0
roi[:,:, 1] = 0

image[height // 2+1:, :] = roi

# cv2.imshow('Sliced Image', sliced_region)
cv2.imshow('Sliced Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()