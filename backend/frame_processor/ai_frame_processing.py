import face_recognition
from deepface import DeepFace
import cv2 as opencv
import numpy
from numpy import ndarray
from random import randrange
import os
from filetype import is_image


class ProcessingImage:
    def __init__(self):
        pass

    def get_visualized_data_frame(self):
        pass


def frame_analytics_processor(current_frame_image: ndarray, all_face_locations: list) -> tuple[int, str, int, str]:
    def get_all_real_faces_position() -> list:
        real_faces_array = []
        for face_box in all_face_locations:
            print("given box", face_box)
            cropped_image = current_frame_image[face_box[3]:face_box[0],
                                                face_box[1]:face_box[2]]
            for recognized_face in face_recognition.face_locations(cropped_image):
                print(recognized_face)
                real_faces_array.append(recognized_face)
        return real_faces_array

    def get_most_attractive_face_position():
        frame_center_position = [side_length // 2 for side_length in current_frame_image.shape[:2]]
        most_attractive_person = all_face_locations[0]
        for face_box in all_face_locations[1:]:
            face_box_center_coords = face_box[3] + face_box[0] // 2, face_box[1] + face_box[2] // 2
            if numpy.sqrt((frame_center_position[0] - face_box_center_coords[0]) ** 2 +
                          (frame_center_position[1] - face_box_center_coords[1]) ** 2) >\
                numpy.sqrt((face_box_center_coords[0] - most_attractive_person[0]) ** 2 +
                          (face_box_center_coords[1] - most_attractive_person[1]) ** 2):
                most_attractive_person = face_box
        return most_attractive_person

    def get_emotion(current_frame_image):
        obj = DeepFace.analyze(current_frame_image, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        return obj

    if all_face_locations:
        try:
            all_face_locations = get_all_real_faces_position()
            analysable_face_box = get_most_attractive_face_position()
            analysable_face_box = [analysable_face_box[2], analysable_face_box[3],
                                   analysable_face_box[1], analysable_face_box[0]]
            print("for analys", analysable_face_box)
            image_for_analyze = current_frame_image[analysable_face_box[3]:analysable_face_box[0],
                                                    analysable_face_box[1]:analysable_face_box[2]]

            deep_analyze_response = get_emotion(image_for_analyze)
            print(deep_analyze_response)
            return randrange(1, 5000),\
                   deep_analyze_response["age"],\
                   deep_analyze_response["gender"],\
                   deep_analyze_response["dominant_emotion"]
        except IndexError:
            pass
    return -1, "", 0, ""


def test():
    images = [r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\coool.jpg",
              r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\chair.jpg",
              r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\sunnt.jpg"]
    test_image = opencv.imread(images[0])
    actually_size = (test_image.shape[:2])
    print("total recognized", face_recognition.face_locations(test_image))
    frame_analytics_processor(test_image, [(actually_size[0], 0, actually_size[1], 0)])
    opencv.imshow("A", test_image)
    opencv.waitKey(0)


if __name__ == "__main__":
    test()