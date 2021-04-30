# 9.4 Write a program to read through the mbox-short.txt and figure out w
# ho has sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

## read a file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

## strip all the name and creates a dictionary that mpas the sender's email
count = dict()
for line in fh:
    if line.startswith("From"):
        words = line.split()
        if words[0]=="From":
            word = words[1]
            count[word]=count.get(word,0)+1#注意后面的get用的是圆括号

## find the biggest vaule in dictionary
max = None ## None的第一个字母大小才能被识别
for a,b in count.items(): ## dic 的遍历对象是item
    if max is None or b>max: ##这里的条件要用is，用==没有用
        champ = a
        max = b

print(champ, max)
