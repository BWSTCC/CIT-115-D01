#input

nStarting_Principal = float (input (f"What is the starting principal? "))
nInterest_Rate = float ( input (f"What is the annual interest rate? "))
nInterest_Compound = int ( input (f"How many times a year is the interest compounded? "))
nAccount_Years =  int (input (f"How many years will the account earn interest? "))


#Calc
nInterest_Rate_Percentage = nInterest_Rate/100
#FV = PV(1+r/m)**mt
nTotal = nStarting_Principal * (1 + (nInterest_Rate_Percentage/nInterest_Compound))**(nInterest_Compound*nAccount_Years)


#Output

print(f"At the end of {nAccount_Years} years you will have ${format(nTotal,',.2f')}")


