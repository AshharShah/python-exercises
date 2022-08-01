import csv


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


logType = getType()
print("\n")
logName = getName()
global taskName

if (logType == 1):
    if(logName == 1):
        file = open('Health Management System\csv-files\harry-diet.csv')
        taskName = input("What did Harry Eat?\n")
    elif(logName == 2):
        file = open('Health Management System\csv-files\ashhar-diet.csv')
        taskName = input("What did Ashhar Eat?\n")
    elif(logName == 3):
        file = open('Health Management System\csv-files\bilal-diet.csv')
        taskName = input("What did Bilal Eat?\n")
elif (logType == 2):
    if(logName == 1):
        file = open('Health Management System\csv-files\harry-exercise.csv')
        taskName = input("What exersice did Harry do?\n")
    elif(logName == 2):
        file = open('Health Management System\csv-files\ashhar-exercise.csv')
        taskName = input("What exersice did Ashhar do?\n")
    elif(logName == 3):
        file = open('Health Management System\csv-files\bilal-exercise.csv')
        taskName = input("What exersice did Bilal do?\n")
