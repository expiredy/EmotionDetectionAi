import face_recognition
import cv2 as opencv
from numpy import ndarray


class ProcessingImage:
    def __init__(self):
        pass

    def get_visualized_data_frame(self):
        pass


def frame_analytics_processor(current_frame_image: ndarray) -> (dict, ndarray):
    def get_all_faces_position() -> list[ndarray]:
        pass

    def get_more_atractive_face_position() -> ndarray:
        pass


    return {}, current_frame_image


def test():
    image1 = opencv.imread("./../database/andrew-baranow/coool.jpg")
    image2 = opencv.imread("./../database/andrew-baranow/chair.jpg")

    framinator_three_thousand = frame_analytics_processor(image1)[1]
    framinator_four_thousand = frame_analytics_processor(image2)[0]

    results = face_recognition.compare_faces([framinator_three_thousand], framinator_four_thousand)

    print(results)
    # opencv.imshow("fuck", framinator_three_thousand)
    # opencv.waitKey(0)
    print(framinator_three_thousand)


if __name__ == "__main__":
    test()