import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

from Logger import *

class FaceRecognizer:

	def __init__(self, mainWin):
		if FaceRecognizer.faceRecognizerInstance != None:
			raise Exception("This class is a Singleton")
		else:
			self.data = pickle.loads(open("encodings.pickle", "rb").read())
			self.mainWin = mainWin
			FaceRecognizer.faceRecognizerInstance = self

	faceRecognizerInstance = None

	@staticmethod
	def getFaceRecognizer(mainWin):
		if FaceRecognizer.faceRecognizerInstance == None:
			FaceRecognizer(mainWin)
		return FaceRecognizer.faceRecognizerInstance

	def parse_args(self):
		ap = argparse.ArgumentParser()
		ap.add_argument("-e", "--encodings", required=True,
						help="path to facial encodings")
		ap.add_argument("-i", "--input", required=True,
						help="path to input video")
		ap.add_argument("-d", "--detection-method", type=str, default="cnn",
						help="detection model: cnn for accuracy, hog for speed")
		return ap.parse_args()


	def recognize_from_video(self, filename=0):

		stream = cv2.VideoCapture(filename)

		i = 0

		cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

		# loop over frames from the video file stream
		while True:
			# grab the next frame
			(grabbed, frame) = stream.read()

			i = i + 1
			# if (i % 6 != 0):
			# 	continue

			# if not grabbed, then the stream was ended
			if not grabbed:
				break

			start = time.time()

			# rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			# rgb = imutils.resize(frame, width=750)
			#
			# frame = self.process_frame(frame)
			# r = frame.shape[1] / float(rgb.shape[1])
			#
			# boxes = face_recognition.face_locations(rgb, model=self.args.detection_method)
			# encodings = face_recognition.face_encodings(rgb, boxes)
			#
			# names = self.recognize_faces(self.data, encodings)

			# self.draw_rectangles(frame, boxes, names, r)
			self.process_frame(frame, detection_method=self.mainWin.getDetectionMethod())
			end = time.time()

			print("time = ", end - start)

			cv2.imshow("frame", frame)
			key = cv2.waitKey(1) & 0xFF

			# if the `q` key was pressed, break from the loop
			if key == ord("q"):
				break

		stream.release()


	def recognize_from_image(self, filename):
		image = cv2.imread(filename)
		cv2.imshow("frame", self.process_frame(image, self.mainWin.getDetectionMethod()))


	def process_frame(self, frame, detection_method):
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		rgb = imutils.resize(rgb, width=750)

		# frame = self.process_frame(frame)
		r = frame.shape[1] / float(rgb.shape[1])

		boxes = None
		if detection_method != 'cascade':
			boxes = face_recognition.face_locations(rgb, model=detection_method,
													number_of_times_to_upsample=self.mainWin.getUpsampleNumber())
		else:
			boxes = self.cascadeDetection(rgb)

		encodings = face_recognition.face_encodings(rgb, boxes, num_jitters=self.mainWin.getJittersNumber())

		names = self.recognize_faces(self.data, encodings)

		self.draw_rectangles(frame, boxes, names, r)

		return frame

	def cascadeDetection(self, rgb):
		face_cascade = cv2.CascadeClassifier('cascade\haarcascade_frontalface_default.xml')
		gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, self.mainWin.getScaleFactor(), self.mainWin.getMinNeighbors())
		boxes = []
		for (x, y, w, h) in faces:
			boxes.append((y, x + w, y + h, x))
		return boxes

	def recognize_faces(self, data, encodings):
		names = []
		for encoding in encodings:
			# match each face to our encodings
			matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=self.mainWin.getTolerance() / 100)
			name = "Unknown"

			# check to see if we have found a match
			if True in matches:
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				name = max(counts, key=counts.get)

			# update the list of names
			names.append(name)

		return names


	def draw_rectangles(self, frame, boxes, names, r):
		for ((top, right, bottom, left), name) in zip(boxes, names):
			# rescale the face coordinates
			top = int(top * r)
			right = int(right * r)
			bottom = int(bottom * r)
			left = int(left * r)

			# draw the predicted face name on the image
			cv2.rectangle(frame, (left, top), (right, bottom),
						  (255, 255, 255), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
						0.75, (255, 255, 255), 2)
			Logger.log(str(name) + ": " + str(left + (right - left) / 2) + ", " + str(top + (bottom - top) / 2))


if __name__ == "__main__":
	recognizer = FaceRecognizer()
	recognizer.recognize_from_video(filename="videos/mekhak_levon.mp4")