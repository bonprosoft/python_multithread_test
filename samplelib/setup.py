try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

import sys
from Cython.Build import cythonize
from Cython.Distutils import build_ext

build_requires = [
    'Cython>=0.2'
]

ext = [
    Extension('samplelib',
              sources=['samplelib.pyx',
                       'samplelib/sampleclass.cpp'],
              language='c++',
              extra_compile_args=['-std=c++11'],
              extra_link_args=['-std=c++11'])
]

setup(name='samplelib',
      version='1.0.0',
      cmdclass={'build_ext': build_ext},
      setup_requires=build_requires,
      ext_modules=ext)
