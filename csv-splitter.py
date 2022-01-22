#!/usr/bin/env python3

import os
from posixpath import splitext

MAX_LINES=1048575

# colours for text output
ERR_COL='\033[91m'
WAR_COL = '\033[93m'
END_COL='\033[0m'

def split(filename):
    # opens file
    print("opening file {}".format(filename))
    csvfile = open("./input/{}".format(filename), 'r').readlines()
    print("{} file opened".format(filename))
    filecount = 1

    # split file
    for i in range(len(csvfile)):
        if i % MAX_LINES == 0:
            open("./output/{}_{}.csv".format(splitext(filename)[0], filecount), 'w+').writelines(csvfile[i:i+MAX_LINES])
            filecount += 1
            
    print("finished splitting: {}".format(filename))

def main():
    # get list of all files in input dir
    path = "./input"
    csv_list = os.listdir(path)

    if len(csv_list) == 0:
        print("No files in input folder. \nExitting")
        exit()

    # read user input
    while True:
        try:
            print("The following files will be split:")
            print(csv_list)
            cont_input = input("Continue? (y/n):")
        except KeyboardInterrupt:
            print("\nExiting")
            exit()
        else:
            if cont_input == "y" or cont_input == "Y":
                break
            elif cont_input == "n" or cont_input == "N":
                print("\nExiting")
                exit()
            else:
                print("Input not recognized. Try again")
                continue

    # splits all files in csv_list
    error_files = []
    for file in csv_list:
        if file.endswith('.csv'):
            split(file)
        else:
            print("{}{} is not a csv file{}".format(WAR_COL, file, END_COL))
            error_files.append(file)
    
    # prints any files which were not split
    if len(error_files) != 0:
        print("\n{}The following files did not properly split:".format(ERR_COL))
        print(csv_list)
        print(END_COL)


if __name__ == "__main__":
    main()
