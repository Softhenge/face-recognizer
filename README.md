# face-recognizer
The program demonstrates three most known face detection algorithms :
- [Histogram of Oriented Gradients (HOG) with Support Vector Machine (SVM) model](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf)
- [Convolutional Neural Network (CNN) based face detection](https://www.arunponnusamy.com/cnn-face-detector-dlib.html)
- [Haar Feature based Cascade Classifier](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf)

and a [Deep Metric Learning based face recognition](http://blog.dlib.net/2017/02/high-quality-face-recognition-with-deep.html) algorithm.

The project is based on `face_recognition` library which wraps DLib facial detection\recognition functionality. It is implemented based on [this great article](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)

## Dependencies

- Dlib
- PyQt5
- OpenCV-Python
- imutils
- Face Recognition

## Installation
From the top directory run
`pip install -r requirements.txt` to install required packages

## Usage

1. To create the databese of known persons put the images of the persons which need to be recognized according to the following structure:
1. To define the known people's set put the images according to the following structure:

```bash
├── root
│   ├── person_1
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
│   │   ├── n.jpg
│   ├── person_2
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
│   │   ├── n.jpg
│   ├── ...
│   ├── person_n
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
│   │   ├── n.jpg
```
the directory names will be used as person name.

2. Choose the detection method, click `Select Dataset Directory`, select the root directory of the images.
3. Click `Create List` to define the list of known people.
4. Choose one of the input options from `Input Options` section. The detection/recognition process will be started after providing valid input.
5. You can change the detection method and adjust detection/recognition parameters at runtime.
