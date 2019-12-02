from math import floor                          #importing the function floor()
file=open('mass_github.txt', 'r')					    #Inputting mass from text file (mass.txt)
sum=0                                           #setting sum to null
def fuel_total(mass):
    fuel=floor(mass/3)-2
    if fuel <= 0:
        return 0
    return fuel+fuel_total(fuel)
for line in file:                               #beginning the for loop for to read the lines in mass.txt
    sum+=fuel_total(int(line))                  #the equation for fuel needed for a mass (input())
print(sum)                                      #printing the answer!