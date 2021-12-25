import cv2 as opencv
import mediapipe
import time
import threading
from threading import Thread
from numpy import ndarray
from asyncio import get_event_loop


class FrameProcessingThread(Thread):
    stop_thread_event = threading.Event

    acync_processing_loop = get_event_loop

    processing_video_frame = ndarray
    array_of_face_boxes = list

    def __init__(self, processing_video_frame, array_of_face_boxes):
        self.processing_video_frame, self.array_of_face_boxes = processing_video_frame, array_of_face_boxes
        super(FrameProcessingThread, self).__init__()
        self.stop_thread_event = threading.Event()

    def stop_thread(self):
        self.stop_thread_event.set()
        print(f"{self.getName()} is dead")

    def run(self):
        print(f"{self.getName()} is started")


class NeuralNetworkProcessManager:
    SKIP_FRAMES_COUNT = 15
    TOTAL_ALLOWED_THREADS = 20
    max_frames_per_second = 60
    fps_counter = int
    processing_loop = get_event_loop

    current_video_frame = ndarray
    array_of_face_boxes = list

    processing_threads_holder_array = list

    def __init__(self):
        self.processing_loop = get_event_loop()
        self.fps_counter = 0
        self.processing_threads_holder_array = [FrameProcessingThread for _ in range(self.TOTAL_ALLOWED_THREADS)]

    async def start_new_processing_session(self):
        for processing_thread_index in range(len(self.processing_threads_holder_array)):
            try:
                if not self.processing_threads_holder_array[processing_thread_index].is_alive():
                    self.processing_threads_holder_array[processing_thread_index].stop_thread()
                    self.__create_new_process(processing_thread_index)
            except TypeError:
                self.__create_new_process(processing_thread_index)

    def __create_new_process(self, processing_thread_index: int):
        self.processing_threads_holder_array[processing_thread_index] = \
            FrameProcessingThread(self.current_video_frame, self.array_of_face_boxes)
        self.processing_threads_holder_array[processing_thread_index].start()


    def get_frame_update(self, current_video_frame: ndarray, array_of_face_boxes: list):
        self.current_video_frame, self.array_of_face_boxes = current_video_frame, array_of_face_boxes
        self.fps_counter += 1
        if self.fps_counter % self.SKIP_FRAMES_COUNT == 0:
           self.processing_loop.run_until_complete(self.start_new_processing_session())
        self.fps_counter %= self.max_frames_per_second


class FaceDetector:
    results = None
    mediapipe_face_detection = None
    mediapipe_raw = None
    face_detection = None

    min_detection_con = float

    current_video_frame = ndarray

    def __init__(self, min_detection_con=0.5):
        self.min_detection_con = min_detection_con
        self.mediapipe_face_detection = mediapipe.solutions.face_detection
        self.mediapipe_raw = mediapipe.solutions.drawing_utils
        self.face_detection = self.mediapipe_face_detection.FaceDetection(self.min_detection_con)

    def __preprocess_current_frame_image(self):
        return opencv.cvtColor(self.current_video_frame, opencv.COLOR_BGR2RGB)

    def get_find_faces(self, video_stream_frame: ndarray, is_debug_mode=True):
        self.current_video_frame = video_stream_frame
        self.results = self.face_detection.process(self.__preprocess_current_frame_image())
        all_face_locations = []
        if self.results.detections:
            for index, detection in enumerate(self.results.detections):
                current_face_box_location = detection.location_data.relative_bounding_box
                image_height, image_width, ic = self.current_video_frame.shape
                all_face_locations.append((int(current_face_box_location.xmin * image_width),
                                           int(current_face_box_location.ymin * image_height),
                                           int(current_face_box_location.width * image_width),
                                           int(current_face_box_location.height * image_height)))
                if is_debug_mode:
                    self.current_video_frame = self.debug_draw(all_face_locations[-1])
        return self.current_video_frame, all_face_locations

    def debug_draw(self, bbox: tuple[int, int, int, int], rt=4):
        opencv.rectangle(self.current_video_frame, bbox, (255, 0, 255), rt)
        return self.current_video_frame


def main():
    session_is_running = True
    video = [r"C:\Users\yarao\Videos\4K Video Downloader\AndrewBaranov.mp4",
             "./../database/VerySeriousVideoForAnalyze.mp4"]
    video_stream_capture = opencv.VideoCapture(video[1])
    face_detector = FaceDetector()
    processing_manager = NeuralNetworkProcessManager()

    while session_is_running:
        frame_status, image_frame = video_stream_capture.read()
        if frame_status:
            image_frame, bboxs = face_detector.get_find_faces(image_frame)
            opencv.imshow("Debug window", image_frame)
            if bboxs:
                processing_manager.get_frame_update(image_frame, bboxs)
            if opencv.waitKey(1) == 27:
                session_is_running = False


if __name__ == "__main__":
    main()