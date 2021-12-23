import cv2 as opencv
import mediapipe
import time
from threading import Thread


class FaceDetector:
    results = None
    croping = (500, 500)

    def __init__(self, min_detection_con=0.5):
        self.min_detection_con = min_detection_con
        self.mediapipe_face_detection = mediapipe.solutions.face_detection
        self.mediapipe_raw = mediapipe.solutions.drawing_utils
        self.face_detection = self.mediapipe_face_detection.FaceDetection(self.min_detection_con)

    def __preprocess_frame_image(self, video_stream_frame):
        opencv.resise()
        return opencv.cvtColor(video_stream_frame, opencv.COLOR_BGR2RGB)

    def get_find_faces(self, video_stream_frame, is_debug_mode=True):
        video_stream_frame = self.__preprocess_frame_image(video_stream_frame)
        self.results = self.face_detection.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for index, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                image_height, image_width, ic = video_stream_frame.shape
                bbox = int(bboxC.xmin * image_width), int(bboxC.ymin * image_height),\
                       int(bboxC.width * image_width), int(bboxC.height * image_height)
                if is_debug_mode:
                    video_stream_frame = self.debug_draw(video_stream_frame, bbox)
        return video_stream_frame, bboxs

    def debug_draw(self, video_stream_frame, bbox, rt=4):
        opencv.rectangle(video_stream_frame, bbox, (255, 0, 255), rt)
        return video_stream_frame


def main():
    session_is_running = True
    video = [r"C:\Users\yarao\Videos\4K Video Downloader\AndrewBaranov.mp4",
             "./../database/VerySeriousVideoForAnalyze.mp4"]
    video_stream_capture = opencv.VideoCapture(video[0])
    face_detector = FaceDetector()
    processor = FaceAnalyticThread()
    processor.start()
    while session_is_running:
        frame_status, image_frame = video_stream_capture.read()
        if frame_status:
            image_frame, bboxs = face_detector.get_find_faces(image_frame)
            opencv.imshow("Image", image_frame)
            if opencv.waitKey(1) == 27:
                session_is_running = False


if __name__ == "__main__":
    main()