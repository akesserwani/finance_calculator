from Tkinter import *
import ttk




root = Tk()
root.geometry("800x680")
root.resizable(width=False, height=False)
#root.configure(background = "gray")

theme = ttk.Style()
theme.theme_use('classic')


def piechart(size=(200,200),title="Pie chart", data=[ ['a',0.1,'green'],
['b',0.2,'red'],['c',0.2,'blue'], ['d', 0.2, 'orange'], ['e', 0.1, 'yellow'], ['f', 0.2, 'brown']]):

    canvas=Canvas(root,height=size[0],width=size[1])
    canvas.place(x = 500, y = 100)

    p=0
    for i in data:
        angle=i[1]*360
        canvas.create_arc(200,200,50,50,start=p,extent=angle,fill=i[2])
        p+=angle



def calculate():
	income = income_entry.get()
	retirementA = retirement_one.get()
	retirementB = retirement_two.get()
	housing = housing_entry.get()
	food = food_entry.get()
	car = car_entry.get()
	child = child_entry.get()
	misc = misc_entry.get()


	remain = int(income) - int(retirementA) - int(retirementB) - int(housing) - int(food) - int(car) - int(child) - int(misc)
	
	if remain > 0:
		label = Label(root, text = "You have $" + str(remain) + " left over")
		label.place(x = 550, y = 500)
	elif remain < 0:
		label = Label(root, text = "You have no money left")
		label.place(x = 550, y = 500)


	retirement_pie = float(retirementA + retirementB)/float(income)
	housing_pie = float(housing)/float(income)
	food_pie = float(food)/float(income)
	car_pie = float(car)/float(income)
	child_pie = float(child)/float(income)
	misc_pie = float(misc)/float(income)
	remain_pie = float(remain)/float(income)


	

	green = Label(root, text = "  Retirement " + str(round(retirement_pie*100, 2)) + " %")
	green.place(x = 550, y = 320)
	green.configure(foreground = "green")

	red = Label(root, text = "  Housing " + str(round(housing_pie*100, 2)) + " %")
	red.configure(foreground = "red")
	red.place(x = 550, y = 340)

	blue = Label(root, text = "  Food " + str(round(food_pie*100, 2)) + " %")
	blue.configure(foreground = "blue")
	blue.place(x = 550, y = 360)

	orange = Label(root, text = "  Car " + str(round(car_pie*100, 2)) + " %")
	orange.configure(foreground = "orange")
	orange.place(x = 550, y = 380)

	yellow = Label(root, text = "  Childcare " + str(round(child_pie*100, 2)) + " %")
	yellow.configure(foreground = "yellow")
	yellow.place(x = 550, y = 400)

	brown = Label(root, text = "  Misc. " + str(round(misc_pie*100, 2)) + " %")
	brown.configure(foreground = "brown")
	brown.place(x = 550, y = 420)


	if remain > 0:
		purple = Label(root, text = "  Remaining " + str(round(remain_pie*100, 2)) + " %")
		purple.configure(foreground = "purple")
		purple.place(x = 550, y = 440)
		piechart(data=[ ['a', retirement_pie,'green'],['b',housing_pie,'red'],['c',food_pie,'blue'], ['d', car_pie, 'orange'], ['e', child_pie, 'yellow'], ['f', misc_pie, 'brown'], ['g', remain_pie, 'purple']])
	elif remain < 0:
		purple = Label(root, text = "No remaining money")
		purple.configure(foreground = "purple")
		purple.place(x = 550, y = 440)
		piechart(data=[ ['a',0.1,'green'],['b',0.2,'red'],['c',0.2,'blue'], ['d', 0.2, 'orange'], ['e', 0.1, 'yellow'], ['f', 0.2, 'brown']])



def budget():
	income = income_entry.get()

	retirement_one.set(income * 0.15 )
	retirement_two.set(income * 0.05)
	housing_entry.set(income * 0.20)
	food_entry.set(income * 0.10)
	car_entry.set(income * 0.1)
	child_entry.set(income * 0.1)
	misc_entry.set(income * 0.2)	




title = Label(root, text = "Monthly Finance Calculator", font='Helvetica 28 bold')
title.place(x = 400, y = 10)


income_label = Label(root, text = "Monthly Income (After Taxes)")
income_label.grid(column = 1, row = 3, pady=(20, 0))
income_entry = Scale(root, from_=0, to=50000, resolution = 100, orient=HORIZONTAL, length = 200)
income_entry.grid(column = 1, row = 4, pady=(0, 20))
income_entry.set(3000)

retirement_one_label = Label(root, text = "401k Contribution")
retirement_one_label.grid(column = 1, row = 6)
retirement_one = Scale(root, from_=0, to=1600, orient=HORIZONTAL, resolution = 10, length = 150)
retirement_one.grid(column = 1, row = 7, pady=(0, 20))
retirement_one.set(500)

retirement_two_label = Label(root, text = "Roth IRA Contribution")
retirement_two_label.grid(column = 1, row = 8)
retirement_two = Scale(root, from_=0, to= 500, orient=HORIZONTAL, resolution = 10)
retirement_two.grid(column = 1, row = 9, pady=(0, 20))
retirement_two.set(100)

housing_label = Label(root, text = "Monthly Mortgage/Rent")
housing_label.grid(column = 1, row = 10)
housing_entry = Scale(root, from_=0, to= 10000, orient=HORIZONTAL, resolution = 100, length = 150)
housing_entry.grid(column = 1, row = 11, pady=(0, 20))
housing_entry.set(1000)


food_label = Label(root, text = "Food")
food_label.grid(column = 1, row = 12)
food_entry = Scale(root, from_=0, to= 10000, orient=HORIZONTAL, resolution = 100, length = 150)
food_entry.grid(column = 1, row = 13, pady=(0, 20))
food_entry.set(500)

car_label = Label(root, text = "Monthly Car Payment")
car_label.grid(column = 1, row = 14)
car_entry = Scale(root, from_=0, to= 10000, orient=HORIZONTAL, resolution = 100, length = 150)
car_entry.grid(column = 1, row = 15, pady=(0, 20))
car_entry.set(500)

child_label = Label(root, text = "Child Care and School (include College Funds)")
child_label.grid(column = 1, row = 16)
child_entry = Scale(root, from_=0, to= 10000, orient=HORIZONTAL, resolution = 100, length = 150)
child_entry.grid(column = 1, row = 17, pady=(0, 20))
child_entry.set(500)

misc_label = Label(root, text = "Miscellanous")
misc_label.grid(column = 1, row = 18)
misc_entry = Scale(root, from_=0, to= 20000, orient=HORIZONTAL, resolution = 100, length = 150)
misc_entry.grid(column = 1, row = 19, pady=(0, 10))
misc_entry.set(1000)



calculate = Button(root, text = "Calculate", command = calculate)
calculate.grid(column = 2, row = 18)
budget_button = Button(root, text = "Ideal Spending", command = budget)
budget_button.grid(column = 2, row = 19)


#labels below piechart
green = Label(root, text = "Retirement ")
green.place(x = 550, y = 320)
green.configure(foreground = "green")

red = Label(root, text = "Housing ")
red.configure(foreground = "red")
red.place(x = 550, y = 340)

blue = Label(root, text = "Food ")
blue.configure(foreground = "blue")
blue.place(x = 550, y = 360)

orange = Label(root, text = "Car ")
orange.configure(foreground = "orange")
orange.place(x = 550, y = 380)

yellow = Label(root, text = "Childcare ")
yellow.configure(foreground = "yellow")
yellow.place(x = 550, y = 400)

brown = Label(root, text = "Misc. ")
brown.configure(foreground = "brown")
brown.place(x = 550, y = 420)

purple = Label(root, text = "Remaining ")
purple.configure(foreground = "purple")
purple.place(x = 550, y = 440)


#default piechart
piechart()


root.mainloop()






