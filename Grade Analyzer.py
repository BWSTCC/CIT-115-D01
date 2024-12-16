#Name
sName = input("What is the name of the student to go through the grade grinder? ")

#Test Numbers
nTest1 = int(input("Test score 1: "))
nTest2 = int(input("Test score 2: "))
nTest3 = int(input("Test score 3: "))
nTest4 = int(input("Test score 4: "))

#Be nice and drop the lowest grade?
sDrop_Grade = input("Drop lowest grade? Y or N: ")

#Check for valid input
if nTest1 < 0 or nTest2 < 0 or nTest3 < 0 or nTest4 < 0:
    print("All test scores must be greater than 0")
    raise SystemExit

#Drop Grade? Calculate grade
else:
    if sDrop_Grade == "Y" or sDrop_Grade == "y":
        if nTest1 < nTest2 and nTest1 < nTest3 and nTest1 < nTest4:
            nDropped_Total = nTest2 + nTest3 + nTest4
            
        elif nTest2 < nTest1 and nTest2 < nTest3 and nTest2 < nTest4:
            nDropped_Total = nTest1 + nTest3 + nTest4
            
        elif nTest3 < nTest1 and nTest3 < nTest2 and nTest3 < nTest4:
            nDropped_Total = nTest1 + nTest2 + nTest4
            
        else:
            nDropped_Total = nTest1 + nTest2 + nTest3

        nGrade_Average = nDropped_Total / 3
        
    elif sDrop_Grade == "N" or sDrop_Grade == "n":
        nGrade_Average = (nTest1 + nTest2 + nTest3 + nTest4)/4
        
    else:
        print("Type a Y or a N to drop lowest value")
        raise SystemExit
    
print (f"{sName}'s grade average is {format(nGrade_Average,'.1f')}")        
    
#Find corresponding letter Grade

if nGrade_Average >= 97.0:
    sLetter_Grade = "A+"
    
elif nGrade_Average >= 94.0:
    sLetter_Grade = "A"

elif nGrade_Average >= 90.0:
    sLetter_Grade = "A-"

elif nGrade_Average >= 87.0:
    sLetter_Grade = "B+"

elif nGrade_Average >= 84.0:
    sLetter_Grade = "B"

elif nGrade_Average >= 80.0:
    sLetter_Grade = "B-"

elif nGrade_Average >= 77.0:
    sLetter_Grade = "C+"

elif nGrade_Average >= 74.0:
    sLetter_Grade = "C"

elif nGrade_Average >= 70.0:
    sLetter_Grade = "C-"

elif nGrade_Average >= 67.0:
    sLetter_Grade = "D+"

elif nGrade_Average >= 64.0:
    sLetter_Grade = "D"

elif nGrade_Average >= 60.0:
    sLetter_Grade = "D-"

else:
    sLetter_Grade = "F"

print(f"{sName}'s letter grade is {sLetter_Grade}")
              
