"""
Joshua Donelly-Higgins, jmd4508@rit.edu, 11/13/17
ranking.py

analysis of life expectancy
"""

from rit_lib import *
import utils

CountryValue = struct_type("CountryValue", (str, "country"), (float, "value")) #create country value

def sorted_ranking_data(data, year):
	"""
	collects countryvalue list for year
	sorts them in descending order

	returns sorted data
	"""
	country_list = []

	for val in data.values():
		try:
			country_list += [CountryValue(val.name, float(val.data[int(year) - 1960]))]
		except ValueError:
			pass

	return sorted(country_list, key=lambda x: x.value, reverse=True)


def main():
	"""
	ask for year of interest
	ask for region
	ask for income
	print top 10 life expectancies
	print bottom 10 life expectancies
	repeat

	returns None
	"""
	data = utils.filter_countries(utils.read_data("worldbank_life_expectancy")) #read data and filter for countries

	#User Input

	year_of_interest = int(input("Enter a year of interest (-1 to quit): ")) #ask for year of interest
	if year_of_interest == -1:
		return None
	region = input("Enter a region (all for all regions): ") #ask for region
	income = input("Enter an income category (all for all categories): ") #ask for income category

	while True: #loop until user quits loop
		newdata = data
		if year_of_interest < 1960 or year_of_interest > 2015:
			print("valid years are 1960 to 2015")
		else:
			bool = True
			if region != "all":
				if utils.valid_region(data, region):
					newdata = utils.filter_region(data, region)
				else:
					bool = False
					print("not valid region")
			if income != "all":
				if utils.valid_income(data, income):
					newdata = utils.filter_income(data, income)
				else:
					bool = False
					print("not valid income")
			if bool:
				countries = sorted_ranking_data(newdata, year_of_interest)
				print("\nTop 10 life expectancies for %d:" % year_of_interest)
				for i in range(len(countries)):
					if i < 10:
						print("%d: %s %f" %((i + 1), countries[i].country, countries[i].value))
				print("\nBottom 10 life expectancies for %d:" % year_of_interest)
				for i in range(len(countries)):
					if (len(countries) - i) < 10:
						print("%d: %s %f" %((i + 1), countries[i].country, countries[i].value))

		#User Input

		year_of_interest = int(input("Enter a year of interest (-1 to quit): ")) #ask for year of interest
		if year_of_interest == -1:
			return None
		region = input("Enter a region (all for all regions): ") #ask for region
		income = input("Enter an income category (all for all categories): ") #ask for income category


if __name__ == '__main__':
	 # main runs only when directly invoking this module
	 main()


#end of program file