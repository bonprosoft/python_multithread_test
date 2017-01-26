# -- coding: utf-8 --
# cython: c_string_type=unicode, c_string_encoding=utf8
# distutils:  language = c++
# distutils:  sources = samplelib/sampleclass.cpp

import time

cdef extern from 'samplelib/sampleclass.hpp' namespace 'samplelib':
    cdef cppclass sampleclass:
        int run(int value) except +
        int run_thread_friendly(int value) except +

cdef class SampleClass:

    cdef sampleclass *_thisptr

    def __cinit__(self):
        self._thisptr = new sampleclass()
        print('[Lib] Internal Cpp instance initialized.')
        if (not self._thisptr):
            raise MemoryError()
        print('[Lib] SampleClass instance initialized.')

    def __dealloc__(self):
        if (self._thisptr):
            del self._thisptr

    def run_external(self, value):
        print('[Lib] Before calling external function.')
        val = self._thisptr.run(value)
        print('[Lib] After calling external function.')
        return val

    def run_thread_friendly_external(self, value):
        print('[Lib] Before calling external function.')
        val = self._thisptr.run_thread_friendly(value)
        print('[Lib] After calling external function.')
        return val

    def run(self, value):
        print('[Lib] Before sleeping.')
        time.sleep(5)
        print('[Lib] After sleeping.')
        return value * 2
