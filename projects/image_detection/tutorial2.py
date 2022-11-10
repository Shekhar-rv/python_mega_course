from zipfile import ZipFile
import glob
import cv2
import os


# unzip the file
with ZipFile("sample_images.zip", "r") as zip:
    zip.extractall(path="./images")

# Create a list of all the images
images = glob.glob("*.jpg")
print(images)

img_path = "/images"
# Create a list of all the images
for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.imwrite(os.path.join(img_path, "resized_" + image), re)
    cv2.destroyAllWindows()
