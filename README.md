# Python csv File Splitter

Splits larger than 1048575 line csv files into separate files so it can be loaded into excel

## Requirements
Python3 which can be installed [here](https://www.python.org/downloads/)

## To run
1. Create the following file structure where input and output are empty folders. They must be in the same location as the csv-splitter.py file.
    ```
    ├── README.md
    ├── input
    ├── output
    └── csv-splitter.py
    ```

2. Place csv files you would like to split int the `input` folder.
3. Open a terminal in the location of csv-splitter.py <br />

   **For windows:** 
   
        type `cmd` into the address bar of the file explorer

   **For mac:**
        
        navigate to the location of the script in finder
        hit `option` + `command` + `P` to show file path
        right click the far-right folder at the bottom of finder and click `New Terminal at Folder`

4. Type `python csv-splitter.py` <br />
   If that doesn't work, try `python3 csv-splitter.py`
5. When the script is finished, split csv files will be placed in the `output` folder

### Things to Note
* existing files in output folder will be overwritten
* `ctrl`+`c` or `cmd`+`c` will exit or cancel a running program

## Example
### Pass
#### Terminal
```
$ python csv-splitter.py
The following files will be split:
['example1.csv']
Continue? (y/n):y
opening file example1.csv
example1.csv file opened
finished splitting: example1.csv
```
#### File Output
```
.
├── README.md
├── input
│   └── example1.csv
├── output
│   ├── example1.csv_1.csv
│   ├── example1.csv_2.csv
│   ├── example1.csv_3.csv
│   ├── example1.csv_4.csv
│   └── example1.csv_5.csv
└── csv-splitter.py
```

### Fail
```
$ python csv-splitter.py
The following files will be split:
['example.txt'] 
Continue? (y/n):y
example.txt is not a csv file

The following files did not properly split:    
['example.txt']
```