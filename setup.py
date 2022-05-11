from setuptools import find_packages, setup

setup(
    name="fliton_fib_py",
    version="0.0.1",
    author="Adam Wong",
    author_email="wizzardcloud@gmail.com",
    description="Calculate Fibonacci number series",
    long_description="A basic library to calculate Fibonacci series",
    long_description_content_type="text/markdown",
    url="https://github.com/AdamW666/fliton-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)