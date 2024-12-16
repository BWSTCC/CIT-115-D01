#FUNction
def Get_Valid_Number(sPrompt, nFloat = True, sAllow_Zero = False):
    while True:
        try:
            if nFloat == True:
                nValue = float(input(sPrompt))
            else:
                nValue = int(input(sPrompt))


            if nValue > 0 or (sAllow_Zero and nValue == 0):
                return nValue
        #Error handling
            else:
                print("Input must be a positive number")
        except ValueError:
            print("Input must be a positive number")

#Get input
nDeposit = Get_Valid_Number("What is the original deposit? ")

nInterest_Rate_Percentage = Get_Valid_Number("What is the interest rate? ")

nMonths = Get_Valid_Number("How many months? ", nFloat = False)

nGoal_Amount = Get_Valid_Number("What is the goal amount? " , sAllow_Zero = True)


#Calc
nMonthly_Interest_Rate = (nInterest_Rate_Percentage/100)/12

#Variables used in loops
nDeposit_For_Loop = nDeposit
nDeposit_While_Loop = nDeposit
nMonths_Till_Goal = 0

#Loops
for nCurrent_Month in range(1, nMonths + 1):
    nInterest = nDeposit_For_Loop * nMonthly_Interest_Rate
    nDeposit_For_Loop += nInterest
    print(f"Month {nCurrent_Month: } Account Balance is: ${nDeposit_For_Loop :,.2f}")


while nDeposit_While_Loop < nGoal_Amount:
    nInterest = nDeposit_While_Loop * nMonthly_Interest_Rate
    nDeposit_While_Loop += nInterest
    nMonths_Till_Goal += 1


print(f"It will take: {nMonths_Till_Goal} months to reach the goal of ${nGoal_Amount :,.2f} ")

