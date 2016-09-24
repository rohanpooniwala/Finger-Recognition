import cv2

i = 1
n = 0
cam = cv2.VideoCapture(0)

while True:
	ret_val, img = cam.read()
	img = cv2.resize(img, (100, 100)) 
	cv2.imshow('my webcam', img)
	k = cv2.waitKey(1)
	if k==27:    # Esc key to stop
        	break
	elif k==49:
		i = 1
		print "Changed to ",i
	elif k==50:
		i = 2
		print "Changed to ",i
	elif k==51:
		i = 3
		print "Changed to ",i
	elif k==52:
		i = 4
		print "Changed to ",i
	elif k==53:
		i = 5
		print "Changed to ",i
	elif k==32: 	#space
		cv2.imwrite('./'+str(i)+'/'+str(n)+'.jpg',img)
		n = n + 1
		print "Saved ",n

cv2.destroyAllWindows()
