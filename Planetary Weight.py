#Step 1: Named Constants

nMERCURY_FACTOR = 0.38
nVENUS_FACTOR = 0.91
nMOON_FACTOR = 0.165
nMARS_FACTOR = 0.38
nJUPITER_FACTOR = 2.34
nSATURN_FACTOR = 0.93
nURANUS_FACTOR = 0.92
nNEPTUNE_FACTOR = 1.12
nPLUTO_FACTOR = 0.066

#Step 2 Ask for input

sName = input ("What is your name? ")
nWeight = float ( input ("What is your weight? ") )


#Step 3 Calculate

nMercury_Weight = nWeight * nMERCURY_FACTOR
nVenus_Weight = nWeight * nVENUS_FACTOR
nMoon_Weight = nWeight * nMOON_FACTOR
nMars_Weight = nWeight * nMARS_FACTOR
nJupiter_Weight = nWeight * nJUPITER_FACTOR
nSaturn_Weight = nWeight * nSATURN_FACTOR
nUranus_Weight = nWeight * nURANUS_FACTOR
nNeptune_Weight = nWeight * nNEPTUNE_FACTOR
nPluto_Weight = nWeight * nPLUTO_FACTOR

#Step 4 Output

print(f"{sName}, here are your weights on the different planets of the solar system:")

#Step 4.1 Format
print(f"{'Mercury Weight:':25s}  {format( nMercury_Weight, '10,.2f')}")
print(f"{'Venus Weight:':25s}  {format( nVenus_Weight, '10,.2f')}")
print(f"{'Moon Weight:':25s}  {format( nMoon_Weight, '10,.2f')}")
print(f"{'Mars Weight:':25s}  {format( nMars_Weight, '10,.2f')}")
print(f"{'Jupiter Weight:':25s}  {format( nJupiter_Weight, '10,.2f')}")
print(f"{'Saturn Weight:':25s}  {format( nSaturn_Weight, '10,.2f')}")
print(f"{'Uranus Weight:':25s}  {format( nUranus_Weight, '10,.2f')}")
print(f"{'Neptune Weight:':25s}  {format( nNeptune_Weight, '10,.2f')}")
print(f"{'Pluto Weight:':25s}  {format( nPluto_Weight, '10,.2f')}")
