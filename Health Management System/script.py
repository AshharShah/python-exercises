import csv
import os
from csv import writer


def getdate():
    import datetime
    return datetime.datetime.now()


def getName():
    print("Who Do You Want To Update!")
    print("Enter 1 for Harry")
    print("Enter 2 for Ashhar")
    print("Enter 3 for Bilal\n")
    return int(input("Enter the corresponding Number Of Client: "))


def getType():
    print("Do you want to Log Diet Or Exercise!")
    print("Press 1 for Diet")
    print("Press 2 for Exercise")
    return int(input("Enter the corresponding number: "))


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        write_obj.close()


logType = getType()
print("\n")
logName = getName()
global taskName

if (logType == 1):
    if(logName == 1):
        taskName = input("What did Harry Eat?\n")
        newInfo = [getdate(), taskName]
        append_list_as_row('Health Management System\harry_diet.csv', newInfo)
    elif(logName == 2):
        taskName = input("What did Ashhar Eat?\n")
        newInfo = [getdate(), taskName]
        append_list_as_row(
            'Health Management System\\ashhar_diet.csv', newInfo)
        print(newInfo)
    elif(logName == 3):
        taskName = input("What did Bilal Eat?\n")
        newInfo = [getdate(), taskName]
        append_list_as_row('Health Management System\\bilal_diet.csv', newInfo)
elif (logType == 2):
    if(logName == 1):
        taskName = input("What exercise did Harry do?\n")
        append_list_as_row(
            'Health Management System\harry_exercise.csv', newInfo)
        newInfo = [getdate(), taskName]
    elif(logName == 2):
        taskName = input("What exercise did Ashhar do?\n")
        newInfo = [getdate(), taskName]
        append_list_as_row(
            'Health Management System\\ashhar_exercise.csv', newInfo)
    elif(logName == 3):
        taskName = input("What exercise did Bilal do?\n")
        newInfo = [getdate(), taskName]
        append_list_as_row(
            'Health Management System\\bilal_exercise.csv', newInfo)
