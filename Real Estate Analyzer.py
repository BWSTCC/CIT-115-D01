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

def get_median(list):
    nList_Length = len(list)

    nMiddle_Value = nList_Length // 2

    if nList_Length % 2 == 1:
        return list[nMiddle_Value]
    else:
        return (list[nMiddle_Value - 1] + list[nMiddle_Value]) / 2

def main():
    nProperty_Sale_Values = []

    while True:
        nSale_Price = get_float_input("Enter the property sale value: ")
        nProperty_Sale_Values.append(nSale_Price)
        while True:
            sRe_Input = input("Type Y to enter another Value or N to continue ").upper()
            if sRe_Input == "Y" or sRe_Input == "N":
                break
            else:
                print("Please enter Y or N")
        if sRe_Input == "N":
            break

    #sort
    nProperty_Sale_Values.sort()

    #Print list
    for nValue in nProperty_Sale_Values:
        print(f"${nValue:,.2f}")


    #Calculations
    nMinimum = min(nProperty_Sale_Values)
    nMaximum = max(nProperty_Sale_Values)
    nTotal_Value = sum(nProperty_Sale_Values)
    nAverage = nTotal_Value / len(nProperty_Sale_Values)
    nMedian = get_median(nProperty_Sale_Values)
    nCommission = nTotal_Value * 0.03

    #output
    print(f"Minimum: ${nMinimum:,.2f}")
    print(f"Maximum: ${nMaximum:,.2f}")
    print(f"Total: ${nTotal_Value:,.2f}")
    print(f"Average: ${nAverage:,.2f}")
    print(f"Median: ${nMedian:,.2f}")
    print(f"Commission: ${nCommission:,.2f}")

#Call Main
main()