cmake_minimum_required(VERSION 2.8)
project(samplelib)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_BUILD_TYPE Release)

set(SOURCE_FILES sampleclass.cpp sampleclass.hpp)
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
add_library(samplelib SHARED sampleclass.cpp)
target_link_libraries(samplelib ${PYTHON_LIBRARIES})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./libs/)
