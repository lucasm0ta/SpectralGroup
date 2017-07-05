import csv
from datetime import datetime
from sklearn import datasets

def checkInput(row):
    try:
        date = datetime.strptime(row[0], '%m/%d/%Y')
        date
        return True
    except ValueError as e:
        # print(e)
        return False

def main():
    with open('../data/AirQualityUCI.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            if checkInput(row):
                print ', '.join(row)

if __name__ == "__main__":
    main()