import cv2 as opencv

from ai_frame_processing import frame_analytics_processor


def video_analyzing_loop(video_stream_capture):
    loop_is_available = True
    while loop_is_available:
        ret_val, current_frame = video_stream_capture.read()
        # opencv.imshow('my webcam', img)
        if opencv.waitKey(1) == 27:
            loop_is_available = False  # esc to set loop running flag to quit the loop
    opencv.destroyAllWindows()


def main():
    camera_video_capture = opencv.VideoCapture(0)
    video_analyzing_loop(camera_video_capture)


if __name__ == '__main__':
    main()