cmake_minimum_required(VERSION 3.0.0)
cmake_policy(SET CMP0054 NEW)
project(MainSystemCore VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})


find_package(pybind11 REQUIRED)

add_executable(MainSystemCore main.cpp)

target_link_libraries(MainSystemCore  ${OpenCV_LIBS} )
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)