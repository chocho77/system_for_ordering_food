import itertools


# Python program to iterate
# over 3 lists using zip function
# tutorial link: https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/


num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

# iterates over 3 lists and executes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for (a, b, c) in zip(num, color, value):
	print (a, b, c)
