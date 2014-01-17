# File: leapyear.py
# A program to detwrmine how many leap years fall between two dates

import calendar

def main():
	print("I hear you're interested in leap years?!")
	year1, year2 = eval(input("PLease enter two years, seperated by a comma: "))
	for i in range(year1, year2 + 1):
		if calendar.isleap(i) is True:
			print(i)


main() 
