import cv2 as opencv
from numpy import ndarray
from ai_frame_processing import frame_analytics_processor
#dict key config
USER_ID_KEY_NAME = "id"
USER_GENDER_KEY_NAME = "gender"
USER_AGE_KEY_NAME = "age"
USER_MOOD_KEY_NAME = "mood"
FACE_FRAME_POSITION_KEY_NAME = "face_position"


DEBUG_WINDOW_NAME = "Soon we all will be fucked by Dany's plushy"


def get_frame_analytics(video_frame: ndarray, debug_mode: bool = False) -> (dict, ndarray):
    data, processed_video_frame = {}, video_frame
    if video_frame is not None:
        data, processed_video_frame = frame_analytics_processor(video_frame)
    return (data, processed_video_frame) if debug_mode else (data, video_frame)


def main():
    session_is_running = True

    video_stream_capture = opencv.VideoCapture("./../database/VerySeriousVideoForAnalyze.mp4")

    opencv.namedWindow(DEBUG_WINDOW_NAME)

    while session_is_running:
        session_is_running, current_frame = video_stream_capture.read()

        response, current_frame = get_frame_analytics(current_frame)
        try:
            opencv.imshow(DEBUG_WINDOW_NAME, current_frame)
        except opencv.cv2.error:
            session_is_running = False
        if opencv.waitKey(1) == 27:
            session_is_running = False
    opencv.destroyAllWindows()


if __name__ == "__main__":
    main()