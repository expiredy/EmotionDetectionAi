#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

//#include <pybind11/pybind11.h>
#include <cstdio>
namespace opencv = cv;
using namespace std;


static bool isAppInRun = true;

int main(int, char**)
{
    opencv::Mat frame;
    opencv::VideoCapture capturing("./../database/VerySeriousVideoForAnalyze.mp4");

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
            break;
        }
        imshow("Live", frame);
        if (opencv::waitKey(5) >= 0)
            isAppInRun = false;
    }
    return 0;
}