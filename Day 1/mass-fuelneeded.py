from math import floor                          #importing the function floor()
file=open('mass.txt', 'r')					    #Inputting mass from text file (mass.txt)
sum=0                                           #setting sum to null
for line in file:                               #beginning the for loop for to read the lines in mass.txt
    sum+=floor(int(line)/3)-2                   #the equation for fuel needed for a mass (input())
print(sum)                                      #printing the answer!