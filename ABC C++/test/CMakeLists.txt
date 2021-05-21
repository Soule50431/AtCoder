cmake_minimum_required(VERSION 3.19)
project(a)
project(b)
project(c)
project(d)

set(CMAKE_CXX_STANDARD 14)

add_executable(a a.cpp)
add_executable(b b.cpp)
add_executable(c c.cpp)
add_executable(d d.cpp)
