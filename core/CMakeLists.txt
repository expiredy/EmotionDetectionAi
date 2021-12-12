cmake_minimum_required(VERSION 3.0.0)
project(MainSystemCore VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(MainSystemCore main.cpp)

find_package( OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

include_directories(${PYTHON_INCLUDE_DIRS})

set(PYBIND11_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/pybind11)
add_subdirectory(${PYBIND11_DIR}/ pybind11)

target_link_libraries( MainSystemCore ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)