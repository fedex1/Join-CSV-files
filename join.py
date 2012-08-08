import sys
import hashlib
import csv

# join.py will perform a join of csv files based on the first column which is used as a key
# (CSV file can be thought of as a database table.)
# this is very useful when you have data in different CSV files that you'd like to merge or join together 
# into one CSV file based on some joining key.
#
# An example is you have a database of registration data with names, birthdates, addresses, etc.
# You also have a database of timing data with names, times, etc.
# You need to have a table with names, birthdates, addresses, AND times.
# You simply set the first column as the joining key, in this case name OR any key that can be used to join and run join.py
#
# Form example,
# %cat 1.csv
# 9,1
# 9,2
# 9,3
# 9,4
# 9,5
# 9,6
# 9,7
# 9,8
# 9,9
#
# %cat registrations.csv
# bill,birthdate,address
#
# %cat timings.csv
# bill,time
# 
# %cat 1.csv registrations.csv timings.csv |join.py
# 
# Will result in the joined table
# 18,9,1,9,2,9,3,9,4,9,5,9,6,9,7,9,8,9,9
# 5,bill,birthdate,address,bill,time
#
# Also we prepend the number of columns in the row since you will probably want to sort by that next to 
# group like records.
#


def main():
    writer = csv.writer(sys.stdout,lineterminator='\n')
    savekey = None
    csvReader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    dict={}
    for row in csvReader:
        if row[0] in dict:
            dict[row[0]].append(row)
        else:
            dict[row[0]] = [row]

    for key in dict:
        mergelist=[]
        totallen=0
        for listitem in dict[key]:
            mergelist.extend(listitem)
            totallen = totallen + len(listitem)
        mergelist.insert(0,totallen)
        writer.writerow(mergelist)



if __name__ == '__main__':
    main()
