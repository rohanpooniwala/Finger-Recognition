import tflearn
import cv2
import numpy as np
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation


print "Loading data-----------------------"
k=0
X = []
Y_t = []

for i in [1,2,3,4,5]:
        while True:
                img = cv2.imread('./'+str(i)+'/'+str(k)+'.jpg')
                if img == None:
                        break
                X.append(cv2.resize(img.astype('float'),(100,100)))
                Y_t.append([i-1])
                k += 1
print X
print Y_t
Y = tflearn.data_utils.to_categorical(Y_t,5)
print Y
Y_t=[]

'''
image_prep = ImagePreprocessing()
image_prep.add_featurewise_zero_center()
image_prep.add_featurewise_stdnorm()

image_aug = ImageAugmentation()
image_aug.add_random_flip_leftright()
image_aug.add_random_rotation(max_angle=25.)
'''

print "Creating net----------------"
#t_norm=tflearn.initializations.uniform(minval=-1.0,maxval=1.0)

net = tflearn.input_data(shape = [None,100,100,3]
                        #,data_preprocessing = image_prep)
                        #,data_augmentation = image_aug
                        )

net = tflearn.conv_2d(net,100,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.conv_2d(net, 80,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.max_pool_2d(net,2)

net = tflearn.conv_2d(net,75,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.conv_2d(net, 40,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.max_pool_2d(net,2)

net = tflearn.conv_2d(net,64,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.conv_2d(net,32,3 ,activation = 'ReLU')#,weights_init=t_norm)
net = tflearn.max_pool_2d(net,2)

net = tflearn.fully_connected(net, 200, activation = 'ReLU')#,weights_init=t_norm)
#net = tflearn.dropout(net,0.5)

net = tflearn.fully_connected(net, 5, activation = 'softmax')#,weights_init=t_norm)

rm = tflearn.optimizers.RMSProp (learning_rate=0.001, decay=0.5, momentum=0.2)
net = tflearn.regression(net, optimizer = rm,
                        loss = 'categorical_crossentropy')

model = tflearn.DNN(net)

print "Net created ------------------"

model.load("test.tflearn")

print model.predict(X[:15])
print Y[:15]

print "Starting webbcam"
cam = cv2.VideoCapture(0)
print "Web cam started" 

while True:
	ret_val, img = cam.read()
	img = cv2.resize(img, (100, 100)) 
	cv2.imshow('my webcam', img)
	k = cv2.waitKey(1)
	if k==27:
		break
	elif k==32:
		print model.predict([img])

cv2.destroyAllWindows()
