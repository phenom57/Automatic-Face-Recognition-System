import cv2
import numpy as np
import sqlite3
import os
import pickle

conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')
c = conn.cursor()
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
f = open('data.pckl', 'rb')
name, rollNo = pickle.load(f)
# name = form.N
# rollNo = form.R
c.execute('INSERT INTO Student (rollNo,name) VALUES (?,?)', (rollNo,name))
uid = c.lastrowid
print('UID = ',uid)
sampleNum = 0
while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_classifier.detectMultiScale(gray, 1.3, 5)
  if faces is not ():
      sampleNum += 1
      for (x,y,w,h) in faces:
          cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
          cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
          cv2.putText(frame, name + ' = ' + str(sampleNum), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
          cv2.waitKey(100)
          cv2.imshow('Face Dataset',frame)
  else:
      print('Face Not Found...!!!')
  if sampleNum == 100 or cv2.waitKey(1) == ord('q'):
      break
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
print('Face dataset created successfully...!!!')