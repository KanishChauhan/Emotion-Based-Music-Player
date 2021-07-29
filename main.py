import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import time
# Create the model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
	# obj=display()
	return render_template('index.html')
@app.route('/about', methods = ['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/emotion_detect', methods = ['GET', 'POST'])
def display():
	# info['emotion_detect'] = request.form['emotion_detect']
	model.load_weights('model.h5')
	# prevents openCL usage and unnecessary logging messages
	cv2.ocl.setUseOpenCL(False)
	# dictionary which assigns each label an emotion (alphabetical order)
	emotion_dict = {0: "angry", 1: "disgusted", 2: "fearful", 3: "happy", 4: "neutral", 5: "sad", 6: "surprised"}
	# start the webcam feed
	cap = cv2.VideoCapture(0)
	found = False
	while not(found):
	# Find haar cascade to draw bounding box around fac
		ret, frame = cap.read()
		if not ret:
			break
		facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces:
		# delay(10	# time.sleep(10)
		# found = True
			cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
			roi_gray = gray[y:y + h, x:x + w]
			cv2.imwrite("static/face.jpg", roi_gray)
			# if cv2.waitKey(1) & 0xFF == ord('q'):
			#     break
		cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
		prediction = model.predict(cropped_img)
		maxindex = int(np.argmax(prediction))
		cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
		# print(emotion_dict[maxindex])
		cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
		# found = True
		time.sleep(3)
		# if cv2.waitKey(1) & 0xFF == ord('q'):
		found = True
	print(emotion_dict[maxindex])
	global emo 
	emo = emotion_dict[maxindex]
	cap.release()
	cv2.destroyAllWindows()
	return render_template("emotion_detect.html", data=emotion_dict[maxindex])

@app.route('/playlist', methods = ['GET', 'POST'])
def playlist():
	print("\n\n" + emo)
	cur = mysql.connection.cursor()
	if emo == 'sad':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'sad'")
	if emo == 'happy':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'happy'")
	if emo == 'angry':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'angry'")
	if emo == 'neutral':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'neutral'")
	if emo == 'surprised':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'surprised'")
	if emo == 'disgusted':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'disgusted'")
	if emo == 'fearful':
		resultValue = cur.execute("SELECT * FROM song_playlist WHERE Genre= 'fearful'")
	# userDetails = cur.execute("SELECT * FROM song_playlist WHERE Genre= $emo").fetchall()
	if resultValue > 0:
		userDetails = cur.fetchall()
	# db.commit()
	return render_template("playlist.html", userDetails=userDetails)

if __name__ == '__main__':
   app.run(debug=True)