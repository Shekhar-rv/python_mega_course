import cv2

# Read the image as a grayscale image
img = cv2.imread("galaxy.jpg", 0)

# Display the type and image
print("Type of image:\n", type(img))
print("The actual image in 2D arrays\n", img)
print("The Shape of the array\n", img.shape)
print("Dimensions of the array\n", img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
