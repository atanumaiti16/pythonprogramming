import string

al= set(string.ascii_lowercase)

str=input("enter a line")

letter=set(str.lower())

if al==letter:
 print("string has all letters")
else:
 print("string doesnot have all letters")