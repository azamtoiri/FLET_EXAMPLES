# file for running project
import os

BASE_DIR = os.getcwd()


def main():
    command_ = 'flet -r ' + BASE_DIR + '\main.py'
    os.system(command_)


if __name__ == '__main__':
    main()
