# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
## pull out the hour
for line in handle:
    if line.startswith("From"):
        words = line.split()
        if words[0]=="From":
            position = line.find(':')
            hour = line[position-2:position]
#            hour = int(hour)
## count and put in dict
            count[hour]=count.get(hour,0)+1## ！！！！重要！！！！

### sort
lst = list()
for key, val in count.items():
    new = (key, val)
    lst.append(new)
lst = sorted(lst)


### output
for val,key in lst[:]:
    print(val,key)
