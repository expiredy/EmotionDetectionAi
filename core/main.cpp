#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

//#include <SQLAPI.h>

#include <string>

namespace opencv = cv;

static bool isAppInRun = true;

opencv::Mat preprocessFrame(opencv::Mat currentFrame){
    return currentFrame;
}


int main(int, char**)
{
    // Sorry i have no idea how 2 initialize adoptive file paths
    std::string analyzingVideoFilePath = "D:/ProjectsField/neuralNetworkForEmotionDetection/database/VerySeriousVideoForAnalyze.mp4";

    opencv::Mat frame;
    opencv::VideoCapture capturing;
    int apiIdReference = opencv::CAP_ANY;
    capturing.open(analyzingVideoFilePath, apiIdReference);

    if (!capturing.isOpened()) {
        return -1;
    }

    while (isAppInRun)
    {
        capturing.read(frame);
        if (frame.empty()) {
            isAppInRun = false;
        }
        if (opencv::waitKey(5) >= 0)
            isAppInRun = false;
        opencv::imshow("Pass", frame);
    }
    return 0;
}