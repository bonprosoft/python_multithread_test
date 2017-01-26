//
// Created by igarashi on 17/01/26.
//

#include <iostream>
#include <thread>
#include "Python.h"
#include "sampleclass.hpp"

namespace samplelib {
    int sampleclass::run(int value) {
        std::cout << "[Cpp] Function Called." << std::endl;

        std::cout << "[Cpp] Before sleeping." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(5));

        std::cout << "[Cpp] After sleeping." << std::endl;
        return value * 2;
    }

    int sampleclass::run_thread_friendly(int value) {
        std::cout << "[Cpp] Function Called." << std::endl;

        std::cout << "[Cpp] Before sleeping." << std::endl;
        Py_BEGIN_ALLOW_THREADS
        std::this_thread::sleep_for(std::chrono::seconds(5));
        Py_END_ALLOW_THREADS

        std::cout << "[Cpp] After sleeping." << std::endl;
        return value * 2;
    }

}
