from setuptools import setup

setup(
  __project__ = "ml",
  __version__ = "2.0.5",
  __description__ = "a Python module that teaches a computer to read pixelated images",
  __packages__ = ["os, tensorflow, fore, matplotlib, numpy"],
  __author__ = "Shaunak Ghosh",
  __author_email__ = "shaunakg2011@gmail.com"
  __classifiers__ = [
    "Development Status :: 5 - Stable",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 4",
  ],
  Environment :: Console
  Environment :: Console :: Wget
  Environment :: Console :: Flask
  Environment :: Console :: TensorFlow
  Environment :: Console :: Numpy
  Environment :: Console :: Fore
  Environment :: Console :: Os
  Environment :: GPU
  __requires__ = ["TensorFlow, Numpy, Pip3, Pip, Npm, Mvn, Guizero"]
)
