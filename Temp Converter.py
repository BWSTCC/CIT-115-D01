#Welcome Message
print("Bohdan's Temperature Converter")

#Enter Temp and Classify
nTemperature = float(input("Please enter a temperature:"))
sTemperature_Scale = str(input("Enter F for Fahrenheit or C for Celsius: "))

#Conversion
if sTemperature_Scale == "F" or sTemperature_Scale == "f":
    if nTemperature > 212:
        print("Temp cannot be greater than 212")
    else:
        nCelsius = (5.0/9)* (nTemperature - 32)
        print(f"The Celsius equivalent is {format(nCelsius, '.1f')}")

elif sTemperature_Scale == "C" or sTemperature_Scale == "c":
    if nTemperature > 100:
        print("Temp cannot be greater than 100")
    else:
        nFahrenheit = ((9.0/5.0)* nTemperature + 32)
        print(f"The Fahrenheit equivalent is {format(nFahrenheit, '.1f')}")
#Failure to Comply
else:
    print("Please restart and enter a F or C")
