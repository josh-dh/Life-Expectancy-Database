"""
Joshua Donelly-Higgins, jmd4508@rit.edu, 11/13/17
drop.py

analysis of drops in life expectancy
"""

from rit_lib import *
import utils
import ranking

Range = struct_type("Range", (str, "country"), (int, "year1"), (int, "year2"), (float, "value1"), (float, "value2")) #create range

def sorted_drop_data(data):
	"""
	collects data and creates list of Range objects from data
	sorts list
	returns sorted list
	"""
	country_list = []

	for val in data.values():
		i = 0
		year_start = 0
		year_end = 0
		val_start = 0.0
		val_end = 100.0

		for item in val.data:
			if item != "":
				i += 1

		for start in range(len(val.data)):
			for end in range(start + 1, len(val.data)):
				try:
					if float(val.data[end]) - float(val.data[start]) < val_end - val_start:
						val_start = float(val.data[start])
						val_end = float(val.data[end])
						year_start = start
						year_end = end
				except ValueError:
					pass
		if i > 1:
			country_list += [Range(country = val.name, year1 = 1960 + year_start, year2 = 1960 + year_end, value1 = val_start, value2 = val_end)]

	return sorted(country_list, key=lambda x: (x.value2 - x.value1), reverse=False)


def main():
	"""
	get data, filter for countries, print list of worst drops

	returns None
	"""
	data = utils.filter_countries(utils.read_data("worldbank_life_expectancy")) #retrieve data and filter for countries

	print("Greatest Drops in life expectancy from 1960 to 2015:")

	country_list = sorted_drop_data(data) #get list of drop data sorted
	for i in range(0, 10):
		print("%d: %s from %d (%f) to %d (%f): %f" % ((i + 1), country_list[i].country, country_list[i].year1, country_list[i].value1, country_list[i].year2, country_list[i].value2, (country_list[i].value2 - country_list[i].value1)))


if __name__ == '__main__':
	 # main runs only when directly invoking this module
	 main()


#end of program file