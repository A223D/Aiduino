import numpy as np
import cv2
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from time import sleep
import os
import serial
# from gpiozero import LED
ser = serial.Serial("COM5")
print(ser.name)
# bioled=LED(3, False)
# nonbioled=LED(2, False)


labels=['1', 'L', 'OK', 'Palm', 'Peace']
model = load_model('final_model.h5')
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2
cap = cv2.VideoCapture(0)


def start():
    text='nothing yet'
    while(True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        frame=cv2.flip(frame, flipCode=1)
        cv2.imwrite('./pic.jpg', frame)
        img = image.load_img('./pic.jpg', target_size=(224, 224))
        x=image.img_to_array(img)
        x=np.expand_dims(x, axis=0)
        images=np.vstack([x])
        results = model.predict(images)
        idx=np.where(results[0]==np.amax(results[0]))
        print(type(results[0]))
        print(results[0])

        cv2.putText(frame, text, bottomLeftCornerOfText, font, fontScale, (0,0,0), lineType+2)
        cv2.putText(frame, text, bottomLeftCornerOfText, font, fontScale, (255,255,255), lineType)
        print(text)
        if (labels[idx[0][0]]=='Peace'):
            text='Gesture: Peace'
            ser.write(b'A')
        elif (labels[idx[0][0]]=='L'):
            text='Gesture: L'
        elif (labels[idx[0][0]]=='OK'):
            text='Gesture: OK'
            ser.write(b'J')
        elif (labels[idx[0][0]]=='Palm'):
            text='Gesture: Palm'
        else:
            text='No gesture'
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

start()
cap.release()
cv2.destroyAllWindows()
