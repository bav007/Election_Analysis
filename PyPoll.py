#The data we need to retrieve
#1.  The total number of votes cast
# 2.  A complete list of candidates who received vots
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import datetime as dt
from tracemalloc import stop

now = dt.datetime.now()
print("The time right now is ", now)

file_to_load = 'Resources/election_results.csv'
# Open the election result and read the file.
election_data = open(file_to_load, 'r')

#Close the file
election_data.close()

with open(file_to_load) as election_data:
    print(election_data)

import os
dir(os)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)


file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

outfile = open(file_to_save, "w")
outfile.write("Hello World")

outfile.close()


file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")
txt_file.close()

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    txt_file.close()

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

   # for row in file_reader:
    #    print(row[0])
    headers = next(file_reader)
    print(headers)
