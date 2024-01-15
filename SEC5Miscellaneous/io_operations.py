from io import BytesIO, BufferedReader
import os
import sys
from os import strerror

# Open a single file read-only and print its contents to the screen
# without using context manager
# stream = open("inputs/The Zen of Python.txt", "r")
# print(stream.read())
# stream.close()
MAX_BUFFER_SIZE = 65536


def readTotalCharacters():
    """
    The readTotalCharacters function reads a single file and counts the total number of characters in that file.
    It returns an integer value representing the total number of characters.

    :return: The total number of characters in the file
    :doc-author: Trelent
    """
    countCH = 0
    try:
        for line in open("inputs/The Zen of Python.txt", "rt"):
            countCH += len(line)
            return countCH
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))


def readAllLines():
    """
    The readAllLines function reads a single file and prints all the lines in that file to the screen.
    It returns nothing.

    :return: None
    :doc-author: Trelent
    """
    try:
        for line in open("inputs/The Zen of Python.txt", "rt"):
            print(line, end="")
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))


def copyFile(src: str, dest_path: str):
    # define security checks
    if src == dest_path:
        raise RuntimeError("Cannot copy file to itself")
    if not os.path.isfile(src) or not os.access(src, os.R_OK):
        raise RuntimeError("Cannot copy file: %s not found" % src)
    if not dest_path or dest_path == "":
        raise ValueError("Invalid destination file name")

    # copy file
    try:
        with open(src, "rb") as src_file, open(dest_path, "wb") as dest_file:
            buffer = src_file.read(MAX_BUFFER_SIZE)
            while buffer:
                dest_file.write(buffer)
                buffer = src_file.read(MAX_BUFFER_SIZE)
    except IOError as e:
        print("something went wrong:", strerror(e.errno))
        exit(e.errno)


def copyFileByteIO(src: str, dest_path: str):
    # define security checks
    if src == dest_path:
        raise RuntimeError("Cannot copy file to itself")
    if not os.path.isfile(src) or not os.access(src, os.R_OK):
        raise RuntimeError("Cannot copy file: %s not found" % src)
    if not dest_path or dest_path == "":
        raise ValueError("Invalid destination file name")

    with open(src, "rb") as src_file, BytesIO(src_file.read()) as bytes, open(
        dest_path, "wb"
    ) as dest_file:
        dest_file.write(bytes.read())
        print(bytes.read())


if __name__ == "__main__":
    # copyFile("inputs/test.png", "inputs/test2.png")
    copyFileByteIO("inputs/test.png", "inputs/test2.png")
