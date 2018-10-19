"""
Joshua Donelly-Higgins, jmd4508@rit.edu, 11/13/17
utils.py

Utilities that:
	-read data
	-filter data
"""

from rit_lib import *
import sys
enc = sys.getdefaultencoding() #used to initiate utf-8 encoding THIS MAY BE NECESSARY ONLY FOR MY SYSTEM

def read_data(filename):
	"""
	reads /data/ + filename + _data.txt
	reads /data/ + filename + _metadata.txt
	returns dict[country code] = object(name, data, Region, IncomeGroup, SpecialNotes)
	"""
	data_dict = {}
	data_obj = struct_type("data_obj", (str, "name"), (list, "data"), (str, "Region"),(str, "IncomeGroup"),(str, "SpecialNotes"))
	data = open("data/" + filename + "_data.txt", encoding = enc)
	metadata = open("data/" + filename + "_metadata.txt", encoding = enc)

	metadata.readline() #drop first line
	data.readline() #drop first line

	#read lines
	for line in data:
		current_line_metadata = metadata.readline().split(',')
		current_line_data = line.split(",")
		data_dict[current_line_data[1]] = data_obj(current_line_data[0], current_line_data[2:-1],current_line_metadata[1],current_line_metadata[2],current_line_metadata[3])

	data.close()
	metadata.close()

	return data_dict


def valid_region(data, region):
	"""
	determines if region is valid
	True if valid
	False if invalid
	returns bool
	"""
	bool = False

	for val in data.values():
		if region == val.Region:
			bool = True

	return bool


def valid_income(data, income):
	"""
	determines if income is valid
	True if valid
	False if invalid
	returns bool
	"""
	bool = False

	for val in data.values():
		if income == val.IncomeGroup:
			bool = True

	return bool


def filter_region(data, region):
	"""
	takes data in the form of a dict[country code] = object(name, data, region, incomegroup, specialnotes)
	returns filtered data
	"""
	data = filter_countries(data)
	if region == "all":
		return data

	return_dict = {}

	for key, val in data.items():
		if region == val.Region:
			return_dict[key] = val

	return return_dict


def filter_income(data, income):
	"""
	takes data in the form of a dict[country code] = object(name, data, region, incomegroup, specialnotes)
	returns filtered data
	"""
	data = filter_countries(data)
	if income == "all":
		return data

	return_dict = {}

	for key, val in data.items():
		if income == val.IncomeGroup:
			return_dict[key] = val

	return return_dict


def filter_countries(data):
	"""
	filters data to only contain countries
	returns filtered data
	"""
	out = {}

	for key, val in data.items():
		if val.Region != '' and val.IncomeGroup != '':
			out[key] = val

	return out


def main():
	"""
	reads data
	counts regions
	counts income groups
	prints regions
	prints income groups

	ask user to filter data by region
	ask user to filter data by income
	asks user to specify country and prints data

	returns None
	"""
	data = read_data("worldbank_life_expectancy")

	#Count and Print Entities and Countries

	region_countrycounts = {}
	income_countrycounts = {}

	for key, val in data.items():
		if val.Region in region_countrycounts.keys():
			region_countrycounts[val.Region] += 1
		else:
			region_countrycounts[val.Region] = 1
		if val.IncomeGroup in income_countrycounts.keys():
			income_countrycounts[val.IncomeGroup] += 1
		else:
			income_countrycounts[val.IncomeGroup] = 1

	print("%d entities" % len(data))
	print("%d countries" % (len(data) - income_countrycounts[""]))

	#Print Regions and Country Counts

	print("\nRegions and their country counts:")
	for key, val in region_countrycounts.items():
		if key == '':
			continue
		print(key + ": " + str(val))

	print("\nIncome groups and their country counts:")
	for key, val in income_countrycounts.items():
		if key == '':
			continue
		print(key + ": " + str(val))

	#Filter and Print Countries

	input_str = input("\nEnter region (press ENTER to skip): ")
	if input_str != '':
		regions = filter_region(data, input_str)
		bool = True
		for key, val in regions.items():
			bool = False
			print(val.name + " (" + key + ")")
		if bool:
			print("No countries with this region.")

	input_str = input("Enter income group (press ENTER to skip): ")
	if input_str != '':
		incomes = filter_income(data, input_str)
		bool = True
		for key, val in incomes.items():
			bool = False
			print(val.name + " (" + key + ")")
		if bool:
			print("No countries with this income group.")

	country = input("Enter country code or name (press ENTER to quit): ")
	while country != '':
		for key, val in data.items():
			if country == val.name:
				country = key
		try:
			for i in range(len(data[country].data)):
				if i == 0:
					print("Data for " + data[country].name + ":")
				print("Year: %d, Life Expectancy: %s" % ((1960 + i), data[country].data[i]))
		except KeyError:
			print("No country exists with this code or name.")
		country = input("Enter country code (press ENTER to quit): ")


if __name__ == '__main__':
	 # main runs only when directly invoking this module
	 main()


#end of program file