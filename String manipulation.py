"""
a simple program that allows user to enter first name and surname and displays in different form 
"""
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

f_initial = fname[0]
l_initial = lname[0]

print("{}. {}".format(f_initial.upper(), l_initial.upper()))

print(fname.capitalize() + " " + lname.upper())

print(f_initial + fname.lower())
