#### Creates a Search a Number printout in the comandline ####
# The idea is to find all numbers from 1 - X as fast as possible 
# Parameter: Dim_xy: Size of the grid for the numbers to be distriuted
# Max_num: is X in 1 - X


import random 
import os

def newline():
    print('')

################# initialisation ###########################
Dim_xy = 40 # Size of the grid ---> allways square
Max_num = 50 # Number of Values in the "plot"
Matr = []

FrameCharacter = '*' #length == 1 is true
FrameLength = len(FrameCharacter) # not implemented 


################# Matrix ###########################
# ceate number matrix for dots
for number in range (1,Max_num+1):  
    numx = random.randint(0,Dim_xy) #x pos in the grid of the number
    numy = random.randint(0,Dim_xy) #y pos in the grid of the number
    row = [number,numx,numy]
    Matr.append(row)

################# Line String ###########################
# create string "row by row"
PlotString = []
for i in range (Dim_xy+1): #iterate over rows
    ColumNum = [] # All numbers of the current row
    rowtext = []  # the final text to describe the current row
    
    for ii in range(Max_num): #iterate over matrix to find numbers in that row 
        if Matr[ii][2] == i: #number is in the row (y)
            # if two numbers are on the same position
            Double_booked_flag = 1
            while Double_booked_flag: #repeat if the position of a number was changed 
                Double_booked_flag = 0
                  
                for Numberino in range(len(ColumNum)): #if another number is allready in that pos
                    if Matr[ii][1] == ColumNum[Numberino][1]:
                        Matr[ii][1] = random.randint(0,Dim_xy)
                        Double_booked_flag = 1
                if len(ColumNum)> Dim_xy:
                    print('Error to many numbers in one line')
                    break
                    
            #### append the approved number
            ColumNum.append([Matr[ii][0],Matr[ii][1]])
            
    ### create the string for the current row 
    for stringpos in range(Dim_xy+1): #position in sting 
        flag = 0
        for indexNum in range(len(ColumNum)): #check if number exists
            if ColumNum[indexNum][1] == stringpos: # if yes put the number on the position
                rowtext.append("%s" % ColumNum[indexNum][0])
                flag = 1
        if flag == 0:
            rowtext.append(" ")
        
    rowtext = ' '.join(rowtext)
    PlotString.append(''.join([rowtext]))


##################### Adjust the lines to the same length ########################
# THis is needet because to digit numbers take more space then one digit numbers # 

Str_len = 0
for i in PlotString:
    if len(i) > Str_len:
        Str_len = len(i)

for i in range(len(PlotString)):
    dif = Str_len - len(PlotString[i])
    PlotString[i] = PlotString[i] + ' '*dif


################# frame and plot #################################
print(FrameCharacter*(Str_len+2+2))


for line in PlotString:
    print(FrameCharacter,line,FrameCharacter)
    

print(FrameCharacter*(Str_len+2+2))
