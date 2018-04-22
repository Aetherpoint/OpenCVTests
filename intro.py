import numpy as np
import cv2

device = 0
cap = cv2.VideoCapture(device)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# if capture failed to open, try again
if not cap.isOpened():
	cap.open(device)

# only attempt to read if it is opened
if cap.isOpened:
	cap.set(3,640)
	cap.set(4,480)

	while True:
		re, img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


		# Only display the image if it is not empty
		if re:
			# cv2.imshow("video output", img)
			cv2.imshow("video output", gray)
		# if it is empty abort
		else:
			print("Error reading capture device")
			break
		k = cv2.waitKey(10) & 0xFF
		if k == 27:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()
else:
	print("Failed to open capture device")






















# import cv2
# import numpy as np
# import matplotlib as mpl
# mpl.use('TkAgg')
# import matplotlib.pyplot as plt


# 							  0
# img = cv2.imread('images/6.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR - 1
#IMREAD_UNCHANGED = -1





# cv2.imshow('image', img);
# cv2.waitKey(0);
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80, 100], 'c', linewidth=5);
# plt.show();

# cv2.imwrite('watchgray.png', img)