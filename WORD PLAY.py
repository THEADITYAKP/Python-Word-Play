#CBSE CS PROJECT IDEA: PYTHON TEXT FILE HANDLING


f=open('words.txt','r')       #txt file opening
r=f.read()      #reading txt file in string format
s=r.split()     #converting string format of the file into list format


def PrintWordsBeginningWithParticularAlphabet():       #2. Function to Print words beginning with particular alphabet
    ip=input("Enter the Alphabet :")
    l=[]
    for item in s:
        if item[0]==ip:
            l.append(item)
    if l==[]:
        print('No such word found!')
    else:
        print("Words beginning with",ip,'are :')
        for i in l:
            print(i)

def CountWordsBeginningWithParticularAlphabet():       #3. Function to Count number of words beginning with particular alphabet
    ip=input("Enter the Alphabet :")
    count=0
    for item in s:
        if item[0]==ip:
            count+=1
    print("Words beginning with (",ip,') alphabet are :',count)
                
def CountWordsBeginningWithAnyVowel():       #4. Function to Count total number of words beginning with any vowel
    count=0
    for item in s:
        if item[0]in 'AEIOUaeiou':
            count+=1
    print("Total number of words beginning with any vowel are :",count)
                
def PrintWordsOfParticularLength():       #6. Function to Print Words of particular length
    ip=int(input("Enter the lenght :"))
    c=0
    for item in s:
        if len(item)==ip:
            print(item)
            c=1
    if c==0:
        print("No word found of length",ip) 

def CountWordsOfParticularLength():       #7. Function to Count Words of particular length
    ip=int(input("Enter the lenght of word :")) 
    count=0
    for item in s:
        if len(item)==ip:
            count+=1
    print('No. of words having',ip,'alphabets are :',count)

def DisplayWordsNotHavingParticularAlphabet():       #8. Function to Display Words not having particular alphabet
    ip=input("Enter the alphabet")
    print("Words not having",ip,"alphabet are :")
    for item in s:
        if ip not in item:
            print(item)

def CountWordsNotHavingParticularAlphabet():       #9. Function to Count Words not having particular alphabet
    ip=input("Enter the alphabet") 
    count=0
    for item in s:
        if ip not in item:
            count+=1
    print("Words not having",ip,"alphabet are :",count)

def DisplayWordsNotHavingAnyVowel():      #10. Function to Display Words not having any vowel
    for word in s:
        for ch in word:
            if ch in 'AEIOUaeiou':
                break
        else:
            print(word)
                        
def CountWordsNotHavingAnyVowel():      #11. Count Words not having any vowel
    c=0
    for word in s:
        for ch in word:
            if ch in 'AEIOUaeiou':
                break
        else:
            c+=1
    print("Words not having any vowel are :",c)

def DisplayWordsNotHavingAnyVowelAndy():      #12. Display Words not having any vowel and y
    for word in s:
        for ch in word:
            if ch in 'AEIOUaeiouy':
                break
        else:
            print(word)

def CountWordsNotHavingAnyVowelAndy():      #13. Count Words not having any vowel and y
    c=0
    for word in s:
        for ch in word:
            if ch in 'AEIOUaeiouy':
                break
        else:
            c+=1
    print("Words not having any vowel and y are :",c)

def CheckPALINDROME(s):         #Checking for PALINDROME words
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    else:
        return True

def DisplayPALINDROMEwords():      #14. Display PALINDROME Words
    for line in s:
        word=line.strip()
        if CheckPALINDROME(word):
            print(word)

def CountPALINDROMEwords():      #15. Count PALINDROME Words
    c=0
    for line in s:
        word=line.strip()
        if CheckPALINDROME(word):
            c+=1
    print("No. of PALINDROME Words are :",c)

def DisplayABECEDARIANwords():      #16. Function to Display ABECEDARIAN Words
    for line in s:
        word=line.strip()
        c=0
        index=0
        while index!=(len(word)-1):
            i=(word[index])
            j=(word[index+1])
            index=index+1
            if ord(j)>=ord(i):
                c=c+1
        if c==(len(word)-1):
            print(word)
            
def CountABECEDARIANwords():      #17. Function to Count ABECEDARIAN Words
    count=0
    for line in s:
        word=line.strip()
        c=0
        index=0
        while index!=(len(word)-1):
            i=(word[index])
            j=(word[index+1])
            index=index+1
            if ord(j)>=ord(i):
                c=c+1
        if c==(len(word)-1):
            count=count+1
    print("No. of ABECEDARIAN Words are :",count)    

def DisplayLongestLengthWord():  #18. Function to Display Longest length word
    L1=0
    L2=[]
    for item in s:      #searching for the maximum length 
        if len(item)>L1:
            L1=len(item)

    for item in s:      #adding the words, which have maximum lenth
        if len(item)==L1:
            L2.append(item)

    print("Maximum length of word =",L1)   #printing the maximum lenght
    print("And Maximum length word are :")
    for item in range(len(L2)):
        print(L2[item])   #printing the words of maximum lenght

def SearchWord():      #19. Function to Check whether entered word is present or not
    ip=input("Enter the Word you want to search :")
    print('Scanning Completed!')
    if ip in s:
        print("Yes, Word is present in the file!")
    else:
        print("Sorry, No such word found!")

def AlphaWordRepeatition():  #20. Function to Display all words formed using some alphabets entered, allowing repetition 
    l=[]
    ip=input("Enter some alphabets :")
    if ip.isalpha():
        c=0
        for word in s:
            word=word.strip()
            for alpha in word:
                if alpha not in ip:
                    break
            else:
                c=1
                l.append(word)
                                    
        if l==[]:
                print("No such word found formed using (",ip,")alphabets and allowing repetition")
        else:
                print("All words formed using",ip,"alphabets, allowing repetition are :")
                for i in l:
                        print(i)
    else:
        print('You have entered someting other than alphabet')

input('''CBSE CS PROJECT IDEA: PYTHON TEXT FILE HANDLING

Program name:WORD PLAY

Made by:
1. Aditya Kumar Pandey of Class XII.C
2. Riya Chauhan of Class XII.A

Batch: 2020-2021
School: St. Paul's School

Under the guidence of Er. Shalabh Agarwal Sir
Press ENTER key to start the Program''')       #Intro of Group
        
repeat='y'
while repeat=='y' or repeat=='Y':
    print("""
Main Menu  
1. Print entire file
2. Print words beginning with particular alphabet
3. Count number of words beginning with particular alphabet
4. Count total number of words beginning with any vowel
5. Count total number of words
6. Print Words of particular length
7. Count Words of particular length
8. Display Words not having particular alphabet
9. Count Words not having particular alphabet
10. Display Words not having any vowel
11. Count Words not having any vowel
12. Display Words not having any vowel and y
13. Count Words not having any vowel and y
14. Display PALINDROME Words
15. Count PALINDROME Words
16. Display ABECEDARIAN Words
17. Count ABECEDARIAN Words
18. Display Longest length word
19. Check whether entered word is present or not
20. Display all words formed using some alphabets entered, allowing repetition
""")
        

    try:
        choice=int(input("Enter your Choice :"))      #asking user's choice
        if choice==1:   #1. Print entire file
            print(r)

        elif choice==2:         #2. Print words beginning with particular alphabet
            PrintWordsBeginningWithParticularAlphabet()            

        elif choice==3:         #3. Count number of words beginning with particular alphabet
            CountWordsBeginningWithParticularAlphabet()
                
        elif choice==4:         #4. Count total number of words beginning with any vowel
            CountWordsBeginningWithAnyVowel()
                
        elif choice==5:         #5. Count total number of words
            print("Total number of words in a file are :",len(s))
                
        elif choice==6:         #6. Print Words of particular length
            PrintWordsOfParticularLength()

        elif choice==7:         #7. Count Words of particular length
            CountWordsOfParticularLength()

        elif choice==8:         #8. Display Words not having particular alphabet
            DisplayWordsNotHavingParticularAlphabet()

        elif choice==9:         #9. Count Words not having particular alphabet
            CountWordsNotHavingParticularAlphabet()

        elif choice==10:        #10. Display Words not having any vowel
            DisplayWordsNotHavingAnyVowel()

        elif choice==11:        #11. Count Words not having any vowel
            CountWordsNotHavingAnyVowel()

        elif choice==12:        #12. Display Words not having any vowel and y
            DisplayWordsNotHavingAnyVowelAndy()

        elif choice==13:        #13. Count Words not having any vowel and y
            CountWordsNotHavingAnyVowelAndy()

        elif choice==14:        #14. Display PALINDROME Words
            DisplayPALINDROMEwords()

        elif choice==15:        #15. Count PALINDROME Words
            CountPALINDROMEwords()

        elif choice==16:        #16. Display ABECEDARIAN Words
            DisplayABECEDARIANwords()

        elif choice==17:        #17. Count ABECEDARIAN Words
            CountABECEDARIANwords()

        elif choice==18:        #18. Display Longest length word
            DisplayLongestLengthWord()
                    
        elif choice==19:        #19. Check whether entered word is present or not
            SearchWord()
                    
        elif choice==20:        #20. Display all words formed using some alphabets entered, allowing repetition
            AlphaWordRepeatition()

        else:
            print("Invalid Choice!!")        #If the user has entered any invalid item
    except ValueError:
        print("You have not entered a proper choice (number)")

        

    repeat=input("""\n\nWould you like to re-run the program
If yes press y,
Else press any other key to close this program:""")        #asking for re-running the program
else:
    print("\n\nThank you for using me\nHave a Nice Day")  #Ending Prog. and printing Thank You Message 
f.close()       #txt file closing
#input()        #this line can be used ONLY if the user is directly running (in black background) the prog. instead of running in "Edit in python(IDLE)", to show the Prog. Closing Message to the user
