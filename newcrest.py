from csv import DictReader
from datetime import datetime

all_data = []
with open("data/Newcrest/DATA - Grind Size data csv Rev 2/Grinding-2015-11.csv.txt") as f:
    for line in DictReader(f):
        line["Date"] = datetime.strptime(line["Date"], "%d/%m/%Y %H:%M:%S")
        print line
