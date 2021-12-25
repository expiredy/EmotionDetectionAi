import face_recognition
import cv2 as opencv
import numpy
from numpy import ndarray

import os
from filetype import is_image

DATASET_FOLDER_PATH = "./../database/"


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
            opencv.imshow("ASss",  cropped_image)
            opencv.waitKey(0)
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

    all_face_locations = get_all_real_faces_position()
    analysable_face_box = get_most_attractive_face_position()
    analysable_face_box = [analysable_face_box[2], analysable_face_box[3],
                           analysable_face_box[1], analysable_face_box[0]]
    print("for analys", analysable_face_box)
    image_for_analyze = current_frame_image[analysable_face_box[3]:analysable_face_box[0],
                                            analysable_face_box[1]:analysable_face_box[2]]

    opencv.imshow("shet", image_for_analyze)
    opencv.waitKey(0)

    return ()


def test():
    images = [r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\coool.jpg",
              r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\chair.jpg",
              r"D:\ProjectsField\neuralNetworkForEmotionDetection\database\andrew-baranow\sunnt.jpg"]
    test_image = opencv.imread(images[0])
    # opencv.imshow("Fuck-1", test_image)
    actually_size = (test_image.shape[:2])
    print("total recognized", face_recognition.face_locations(test_image))
    # for face in face_recognition.face_locations(test_image):
    #     opencv.rectangle(test_image, [face[-1]] + list(face[:-1]), (255, 0, 255), 3)
    #     opencv.waitKey(0)

    frame_analytics_processor(test_image, [(actually_size[0], 0, actually_size[1], 0)])


if __name__ == "__main__":
    test()