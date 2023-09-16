import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gradop",
    version="0.1.0",
    author="Yogesh Sharma",
    author_email="jangidyogesh123@gmail.com",
    description="A small and simple autograder ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jangidyogesh12/gradop.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",master
    ],
    python_requires='>=3.6',
)