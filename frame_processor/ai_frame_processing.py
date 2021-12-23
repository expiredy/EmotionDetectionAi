import face_recognition
import cv2 as opencv
from numpy import ndarray

import os
from filetype import is_image

DATASET_FOLDER_PATH = "./../database/"


class ProcessingImage:
    def __init__(self):
        pass

    def get_visualized_data_frame(self):
        pass


def frame_analytics_processor(current_frame_image: ndarray) -> (dict, ndarray):
    def use_current_frame_image() -> ndarray:
        return current_frame_image

    def get_all_faces_position() -> list[ndarray]:
        all_faces_position_array = face_recognition.face_locations(use_current_frame_image())
        return all_faces_position_array

    def get_more_attractive_face_position() -> ndarray:
        pass

    some_data = get_all_faces_position()

    return {}, current_frame_image


def get_loaded_dataset() -> list[ndarray]:
    for root, directories, files in os.walk(DATASET_FOLDER_PATH):
        for file_name in files:
            if is_image(os.path.join(root, file_name)):
                yield face_recognition.face_encodings(opencv.imread(os.path.join(root, file_name)))[0]


def test():
    print("start")
    all_dataset_images = get_loaded_dataset()
    test_image = face_recognition.face_encodings(opencv.imread(r"C:\Users\yarao\Downloads\ummE-VZb4-E.jpg"))[0]
    print("all data was given")
    result = face_recognition.compare_faces(list(all_dataset_images), test_image)
    print(result)


if __name__ == "__main__":
    test()