#!/usr/bin/python3

#It prints the num of and list of arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    list_arg = len(arg)-1

    if list_arg >1:
        print("{} arguments.".format(list_arg))
        for i in range(1, size + 1):
            print("{}:{}".format(i, arg[i]))

    elif list_arg == 0:
        print("{} arguments.".format(list_arg))
    else:
        print("{} arguments:".format(list_arg))
        print("{}: {}".format(list_arg, arg[1]))
