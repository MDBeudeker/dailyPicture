import cv2
from datetime import date
import os.path


today = date.today()
d1 = today.strftime("%d-%m-%Y")
img_name = "D:/python/dailyPicture/foto_{}.png".format(d1)


fileExists = os.path.isfile(img_name)

if fileExists == True:
	print("Photo already exists for date {}!".format(d1))
	quit()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("test")

print("press space to continue")

while True:
	ret, frame = cam.read()
	if not ret:
		print("failed to grab frame")
		break

	cv2.imshow("test",frame)

	k = cv2.waitKey(1)
	if k%256 == 32:
		#space pressed
		cv2.imwrite(img_name, frame)
		print("{} written!".format(img_name))
		break

cam.release()

cv2.destroyAllWindows()
