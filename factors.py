"""
Joshua Donelly-Higgins, jmd4508@rit.edu, 11/13/17
factors.py

graphing of data using turtle
"""

from rit_lib import *
import utils
import turtle as t
t.tracer(0,0)

def graph(data, x, y, legend):
	"""
	makes a graph of size x * y pixels
	y-axis is labeled from 0 to 100
	x-axis is labeled from 1960 to 20
	takes a list of coords [median life expectancy,...]
	graphs in turtle

	preconditions and postconditions are controlled for by the function
	"""
	#make axes
	t.color("black")
	t.up()
	t.goto(-x/2, -y/2)
	t.left(90)
	t.down()
	t.forward(y)
	t.backward(y)
	t.right(90)
	t.forward(x)
	t.backward(x)
	t.up()

	#make y-coords
	t.backward(20)
	for i in range(11):
		t.down()
		t.write(str(i * 10))
		t.up()
		t.left(90)
		t.forward(y/10)
		t.right(90)

	#make x-coords
	t.goto(-x/2, -y/2)
	t.right(90)
	t.forward(20)
	t.left(90)
	t.down()
	t.write(1960)
	t.up()
	t.forward(x)
	t.down()
	t.write(2015)
	t.up()

	#label axes
	t.goto(-x/2 - 100, 0)
	t.down()
	t.write("life expectancy")
	t.up()
	t.goto(0, -y/2 - 50)
	t.down()
	t.write("year")
	t.up()

	#create legend
	t.goto(-x/2, y/2 + 50)
	for element in legend:
		t.color(element[1])
		t.down()
		t.write(element[0])
		t.up()
		t.left(90)
		t.forward(10)
		t.right(90)

	#graph data
	for element in legend:
		t.color(element[1])
		t.up()
		i = 0
		for coords in data[element[0]]:
			t.goto(i * (x/55) - x/2,coords * (y/100) -y/2)
			i += 1
			t.down()


def main():
	"""
	read data
	compute median life expectancies for income categories
	graph
	prompt user to continue
	compute median life expectancies for regions
	graph

	returns None
	"""
	data = utils.filter_countries(utils.read_data("worldbank_life_expectancy"))

	#compute median life expectancy by year for income categories
	median_income_preprocessing = {"High income": [], "Low income": [], "Upper middle income": [], "Lower middle income": []}
	median_income = {"High income": [], "Low income": [], "Upper middle income": [], "Lower middle income": []}

	for val in data.values():
		median_income_preprocessing[val.IncomeGroup] += [val.data]

	for key in median_income_preprocessing.keys(): #iterate groups
		for year in range(55): #iterate year
			tmp = []
			for country in range(len(median_income_preprocessing[key])): #iterate countries
				if median_income_preprocessing[key][country][year] == '':
					tmp += [0.0]
				else:
					tmp += [float(median_income_preprocessing[key][country][year])]
			tmp.sort()
			median_income[key] += [tmp[len(median_income_preprocessing[key])//2]]

	#compute median life expectancy by year for regions
	median_region_preprocessing = {"Sub-Saharan Africa": [], "South Asia": [], "Europe & Central Asia": [], "Latin America & Caribbean": [], "Middle East & North Africa": [], "North America": [], "East Asia & Pacific": []}
	median_region = {"Sub-Saharan Africa": [], "South Asia": [], "Europe & Central Asia": [], "Latin America & Caribbean": [], "Middle East & North Africa": [], "North America": [], "East Asia & Pacific": []}

	for val in data.values():
		median_region_preprocessing[val.Region] += [val.data]

	for key in median_region_preprocessing.keys(): #iterate groups
		for year in range(55): #iterate year
			tmp = []
			for country in range(len(median_region_preprocessing[key])): #iterate countries
				if median_region_preprocessing[key][country][year] != '':
					tmp += [float(median_region_preprocessing[key][country][year])]
			tmp.sort()
			median_region[key] += [tmp[len(median_region_preprocessing[key])//2]]

	# print(median_income["High income"])
	# print(len(median_income["Low income"]))
	# return None

	#graph by income
	graph(median_income, 400, 400, [("High income", "orange"), ("Low income", "red"), ("Upper middle income", "blue"), ("Lower middle income", "green")])

	#graph by region
	if input("Press ENTER to continue: ") == '':
		t.clear()
		graph(median_region, 400, 400, [("Sub-Saharan Africa", "red"), ("South Asia", "blue"), ("Europe & Central Asia", "green"), ("Latin America & Caribbean", "orange"), ("Middle East & North Africa", "yellow"), ("North America", "black"), ("East Asia & Pacific", "magenta")])
		t.done()


if __name__ == '__main__':
	 # main runs only when directly invoking this module
	 main()


#end of program file