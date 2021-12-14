#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

#include <cstdio>
namespace opencv = cv;
using namespace std;


static bool isAppInRun = true;

int main(int, char**)
{
    // Sorry i have no idea how 2 initialize adoptive file paths
    string analyzingVideoFilePath = "D:/ProjectsField/neuralNetworkForEmotionDetection/database/VerySeriousVideoForAnalyze.mp4";

    opencv::Mat frame;
    opencv::VideoCapture capturing;
    int apiIdReference = opencv::CAP_ANY;
    capturing.open(analyzingVideoFilePath, apiIdReference);

    if (!capturing.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }

    cout << "Start grabbing" << endl
         << "Press any key to terminate" << endl;

    while (isAppInRun)
    {
        capturing.read(frame);
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            isAppInRun = false;
        }
        if (opencv::waitKey(5) >= 0)
            isAppInRun = false;
        opencv::imshow("Live", frame);
    }
    return 0;
}