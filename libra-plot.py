import argparse
import csv
import matplotlib.pyplot as plt
import sys

from datetime import datetime
from decimal import Decimal


MIN_PYTHON = (3, 6)
VERSION = "1.0.0"


if sys.version_info < MIN_PYTHON:
    print(f"Minimum python version must be >= {MIN_PYTHON}")
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument('file', help='CSV file to parse')
args = parser.parse_args()

dates = []
trend = []
weight = []

with open(args.file) as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    counter = 0
    for row in reader:
        counter += 1
        if(not row or (row and row[0].startswith('#'))):
            continue

        date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').date()

        dates.append(date)
        weight.append(Decimal(row[1]))
        trend.append(Decimal(row[2]))

plt.figure(figsize=(40, 10))

plt.plot(dates, weight, label='Weight')
plt.plot(dates, trend, label='Trend', color='r')

plt.xlabel('Dates')
plt.ylabel('Pounds')
plt.gca().grid(True)

plt.tight_layout()
plt.savefig('output.png', dpi=72)
