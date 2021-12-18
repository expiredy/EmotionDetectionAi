import face_recognition

import cv2 as opencv

from numpy import ndarray


def frame_analytics_processor(frame: ndarray):
    def detect_face(img):
        # convert the test image to gray image as opencv face detector expects gray images
        gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)

        # load OpenCV face detector, I am using LBP which is fast
        # there is also a more accurate but slow Haar classifier
        face_cascade = opencv.CascadeClassifier('opencv-processing-files/lbpcascade_frontalface.xml')

        # let's detect multiscale (some images may be closer to camera than others) images
        # result is a list of faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        # if no faces are detected then return original img
        if (len(faces) == 0):
            return None, None

        # under the assumption that there will be only one face,
        # extract the face area
        (x, y, w, h) = faces[0]

        # return only the face part of the image
        return gray[y:y + w, x:x + h], faces[0]

    return detect_face(frame)


def test():
    image = opencv.imread("./../database/face-image/woman-smiling-again.jpg")
    opencv.imshow("fuck1", image)
    opencv.waitKey(0)
    framinator_three_thousand = frame_analytics_processor(image)
    opencv.imshow("fuck", framinator_three_thousand)
    opencv.waitKey(0)


if __name__ == "__main__":
    test()