import sys
from pybind11 import get_cmake_dir, get_include
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages

__version__ = "0.2.4"

ext_modules = [
    Pybind11Extension("_jsonata",
        ["wrapper.cpp", "duktape-2.7.0/src/duktape.c"],
        include_dirs=[get_include(), "duktape-2.7.0/src/"],
        define_macros = [('VERSION_INFO', __version__)],
        language           = 'c++',
        extra_compile_args = ['-std=c++14'],
        ),
]

setup(
    name="jsonata",
    version=__version__,
    author="Rob J Meijer",
    license='BSD',
    readme = "README.md",
    author_email="pibara@gmail.com",
    url="https://github.com/pibara/jsonata-wrapper",
    description="A simple Python wrapper for the JavaScript JSONata lib.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Environment :: Other Environment'
    ],
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
    packages=find_packages(),
)

