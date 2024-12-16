#import

import math

#FUNctions
def get_float_input(sPrompt):
    while True:
        try:
            nFloat =  float(input(sPrompt))
            if nFloat > 0:
                return nFloat
            #Error Handling
            else:
                print("Input must be a positive number")

        except ValueError:
            print("Input must be a positive number")


def get_gallons_of_paint(Square_Feet, Feet_per_Gallon):
    return math.ceil(Square_Feet / Feet_per_Gallon)

def get_labor_hours(Labor_Hours, Total_Gallons):
    return Labor_Hours * Total_Gallons

def get_labor_costs(Labor_Hours, Labor_Charge):
    return Labor_Hours * Labor_Charge

def get_paint_cost(Total_Gallons, Paint_Price):
    return Total_Gallons * Paint_Price

def get_sales_tax(state):
    if state == "CT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return 0.07
    elif state == "VT":
        return 0.06
    else:
        return 0.0

def print_cost_estimate(total_gallons, labor_hours, paint_cost, labor_cost, sales_tax, total_cost, file_name):
    print(f"The amount of gallons needed is {total_gallons}")
    print(f"The paint job will take {labor_hours}")
    print(f"The total cost of paint is ${paint_cost:,.2f}")
    print(f"The total cost of labor is ${labor_cost:,.2f}")
    print(f"The amount of tax you have to pay is ${sales_tax:,.2f}")
    print(f"The total cost of the paint job is ${total_cost:,.2f}")

    #Write file
    with open(file_name, "w") as file:
        file.write(f"The amount of gallons needed is {total_gallons}\n")
        file.write(f"The paint job will take {labor_hours}\n")
        file.write(f"The total cost of paint is ${paint_cost:,.2f}\n")
        file.write(f"The total cost of labor is ${labor_cost:,.2f}\n")
        file.write(f"The amount of tax you have to pay is ${sales_tax:,.2f}\n")
        file.write(f"The total cost of the paint job is ${total_cost:,.2f}\n")

    print(f"The file {file_name} has been created.")

def main():
    #Get Input
    nSquare_Feet_of_Wall = get_float_input("How many square feet is the wall? ")
    nPaint_Price = get_float_input("What is the price of paint per gallon? ")
    nFeet_Per_Gallon = get_float_input("How many feet does your gallon of paint cover? ")
    nLabor_Hours_Per_Gallon = get_float_input("How many labor hours per gallon? ")
    nLabor_Charge_Per_Hour = get_float_input("How much is labor per hour? ")
    sState = input("Enter the State Initials of the state the job is being done in: ")
    sLast_Name = input("What is the last name of the customer? ")

    #Calculations
    nGallons_Needed = get_gallons_of_paint(nSquare_Feet_of_Wall, nFeet_Per_Gallon)
    nLabor_Hours_Needed = get_labor_hours(nLabor_Hours_Per_Gallon, nGallons_Needed)
    nCost_of_Labor = get_labor_costs(nLabor_Hours_Needed, nLabor_Charge_Per_Hour)
    nCost_of_Paint = get_paint_cost(nGallons_Needed, nPaint_Price)
    nTax_Rate = get_sales_tax(sState)
    nSales_Tax = (nCost_of_Labor + nCost_of_Paint) * nTax_Rate
    nTotal_Cost = nCost_of_Labor + nCost_of_Paint + nSales_Tax

    #Output file
    sFile_Name = f"{sLast_Name}_PaintJobOutput.txt"
    print_cost_estimate(nGallons_Needed, nLabor_Hours_Needed, nCost_of_Paint, nCost_of_Labor,  nSales_Tax, nTotal_Cost, sFile_Name)

#call main
main()