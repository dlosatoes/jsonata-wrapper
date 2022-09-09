project(jsonata)
cmake_minimum_required(VERSION 3.22)
add_subdirectory(pybind11)
include_directories(duktape-2.7.0/src)
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)
pybind11_add_module(jsonata wrapper.cpp duktape-2.7.0/src/duktape.c)

