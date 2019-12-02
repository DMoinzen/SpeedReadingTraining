# Word counting and formating a text over multiple lines 

import time  

############ Text ##############
TextString = "Hallo mein Name ist Tim und ich Arbeite an einem Programm, das diverse Übungen zum erlernen von Speedreading beinhaltet. Ich habe es schon geschafft mir einen Generellen Überblick über das Thema zu verschaffen, allerdings ist es im großen und ganzen recht Komplex. Als nächstes möchte ich gerne das Testen von der Lesegeschwindigkeit automatisieren. Dazu brauche ich diverse Grundvorraussezungen. Das ganze sollte mit jedem beliebigen Text funktionieren. Dazu kann man zum Beispiel Texte aus dem Internet verwenden, oder diese sogar selbst verfassen. Der Text sollte in der konsole zeilenweise dargestellt werden. Das Programm sollte erkennen können, wie viele wörter gerade gelesen werden, und dementsprechend auch die Zeit stoppen in welcher dies geschehen ist. - Tim"

FormatedString = []

#print(TextString)

######Parameter
LineLength = 50 #character

DisplayMode = 'n' #possilbe values: 'n', 'm', 'ml', 'mp', 'wpm'
wpm = 200

####### count number of words sum 
def NumberOfWords(Text):
    #1 split the text in chunks "similar to words" e.g by spaces
    
    NumberSpace = -1
    ListOfSpaces = [-1] #Startvalue
    SpaceString = ' '
    NoLetterList = ['-',':','_',',','.',''] 
    LetterList = set('abcdefghijklmnopqrstuvwxyzäüöABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ1234567890')
    #Word = 'Hallo'
    #print(LetterList.intersection(Word))
    while True: #identify all whitespace
        NumberSpace = Text.find(SpaceString,NumberSpace+1)
        if not NumberSpace == -1: 
            ListOfSpaces.append(NumberSpace)
        else:
            break
    ListOfSpaces.append(len(Text)+1) # Last Value
    
    WordList = []
    for indexS in range(len(ListOfSpaces)-1):
        WordList.append(Text[ListOfSpaces[indexS]+1:ListOfSpaces[indexS+1]])
    #print(WordList)
    #2 identify if chunk = word 
    # Remove remaining whitespaces: for easy detection  
    
    # Remove < single length items
    RemoveList = []
    
    for Word in WordList:
        if len(Word) <= 1:
            RemoveList.append(Word)
        elif not LetterList.intersection(Word):
            RemoveList.append(Word)

    for Word in RemoveList:
        WordList.remove(Word)
    #print(WordList)
    # Remove items only consisting of these characters
    
    
    #3 cound words
    WordNum = len(WordList)
    return WordNum
    

####### Format text 
# cut string after specified length 
# Do not seperate a word e.g. cut where a space is 
# do not start a new line with a whitespace 
# if there is a new line character start a new line 
# For now: no word seperation 
NumberSpace = -1
ListOfSpaces = []
SpaceString = ' '

while True:
    NumberSpace = TextString.find(SpaceString,NumberSpace+1)
    if not NumberSpace == -1: 
        ListOfSpaces.append(NumberSpace)
    else:
        break

NewLineLocations = [-1] 
for i in ListOfSpaces:
    if i > LineLength + NewLineLocations[-1]:
        ind = ListOfSpaces.index(i)
        NewLineLocations.append(ListOfSpaces[ind-1])
        
NewLineLocations.append(len(TextString)) # The last value

for ii in range(len(NewLineLocations)-1):
    FormatedString.append(TextString[NewLineLocations[ii]+1:NewLineLocations[ii+1]])


#print(ListOfSpaces)
#print (NewLineLocations)


####### display text #######
# Display modes:
# Normal --> n
# Mesure time --> m
# Measure Time per line  --> ml
# Measure Time per multipe lines (paragraph) --> mp
# Display with wpm speed --> wpm

if DisplayMode == 'n': #Ok works as intended
    for line in FormatedString:
        Wordcount = NumberOfWords(line)
        dif = 4 - len(str(Wordcount))
        CountStr = str(Wordcount) + ' '*dif
        print(CountStr,line)
    Number = NumberOfWords(TextString)
    print('___')
    print(Number)
    
elif DisplayMode == 'm':
    i = 1
elif DisplayMode == 'ml':
    i = 1
elif DisplayMode == 'mp':
    i = 1
elif DisplayMode == 'wpm':
    for line in FormatedString:
        start = time.time()
        Wordcount = NumberOfWords(line)
        dif = 4 - len(str(Wordcount))
        CountStr = str(Wordcount) + ' '*dif
        print(CountStr,line)
        #calculate the waiting time depending on the number of words in the row
        WaitingTime = Wordcount/wpm*60 #in Seconds 
        endtime = time.time()
        time.sleep(0.3)
        print (endtime-start)
        
        
    Number = NumberOfWords(TextString)
    print('___')
    print(Number)
else :
    print('Warning: Invalid DisplayMode - No output displayed!')
    
    
start = time.time()
print(1)
time.sleep(10)

endtime = time.time()
print(endtime-start)




#print('The End')
