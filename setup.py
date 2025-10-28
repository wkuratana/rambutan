# Imports
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy


# TODO: This is a temp extension for testing the build
extensions = [
    Extension(
        "seam_carver.test_build", 
        sources=["src/seam_carver/backend.c"],
        include_dirs=[numpy.get_include()]
    )
]

setup(
    ext_modules=cythonize(extensions)
)