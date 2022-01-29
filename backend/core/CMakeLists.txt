cmake_minimum_required(VERSION 3.1)
cmake_policy(SET CMP0054 NEW)
set(CMAKE_TRY_COMPILE_TARGET_TYPE "STATIC_LIBRARY")
project(MainSystemCore VERSION 0.1.0)

include(CTest)
enable_testing()

set(CMAKE_CXX_STANDARD 11)

find_package(pybind11 REQUIRED)
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

add_executable(MainSystemCore main.cpp)

include_directories(${pybind11_INCLUDE_DIRS})
target_link_libraries(MainSystemCore  ${pybind11_LIBS} )

FIND_PACKAGE( OpenCV REQUIRED )
INCLUDE_DIRECTORIES( ${OpenCV_INCLUDE_DIRS} )
target_link_libraries(MainSystemCore ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
