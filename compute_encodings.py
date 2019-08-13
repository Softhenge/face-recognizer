from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
from Logger import *


class FaceEncoder:

	def __init__(self, mainWin):
		if FaceEncoder.faceEncoderInstace != None:
			raise Exception("This class is a Singleton")
		else:
			self.encodings = []
			self.names = []
			self.mainWin = mainWin
			FaceEncoder.faceEncoderInstace = self

	faceEncoderInstace = None

	@staticmethod
	def getFaceEncoder(mainWin):
		if FaceEncoder.faceEncoderInstace == None:
			FaceEncoder(mainWin)
		return FaceEncoder.faceEncoderInstace

	def parse_args(self):
		ap = argparse.ArgumentParser()
		ap.add_argument("-i", "--images", required=True,
						help="path to the input images")
		ap.add_argument("-e", "--encodings", required=True,
						help="path to the db file of name:encoding pairs to be generated")
		ap.add_argument("-d", "--detection-method", type=str, default="cnn",
						help="detection model: cnn for accuracy, hog for speed")
		args = ap.parse_args()

		return args


	def generate_encodeings(self, images, filename):
		imagePaths = list(paths.list_images(images))

		# loop over the images
		for (i, imagePath) in enumerate(imagePaths):
			Logger.log("Processing image {}/{}".format(i + 1, len(imagePaths)))

			image = cv2.imread(imagePath)
			rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			# detect bounding boxes for each face
			faces = face_recognition.face_locations(rgb_image, model=self.mainWin.getDetectionMethod(),
													number_of_times_to_upsample=self.mainWin.getUpsampleNumber())

			# compute embedding
			face_encodings = face_recognition.face_encodings(rgb_image, faces, num_jitters=self.mainWin.getJittersNumber())

			# use folder's name as persons name
			name = imagePath.split(os.path.sep)[-2]

			# save name and encodings
			for encoding in face_encodings:
				self.encodings.append(encoding)
				self.names.append(name)

		self.save_encodings(filename)


	def save_encodings(self, fileName):
		Logger.log("Saving names and encodings...")
		data = {"encodings": self.encodings, "names": self.names}
		f = open(fileName, "wb")
		f.write(pickle.dumps(data))
		f.close()
		Logger.log("Done.")

if __name__ == "__main__":
	encoder = FaceEncoder()
	encoder.generate_encodeings()
	encoder.save_encodings()
