#Section 1: Introduction

"""Introductory Question 1
Write a program that asks the user to enter a number. Store that number in a variable.
Add 2 to that number. store the result in the same variable. and then print out the value of that variable."""

number = eval(input("Enter a number: ")) #TERMINAL:Enter a number: 3.4
number += 2
print(number)                             #TERMINAL:5.4

"""Introductory Question 2
Write a program that asks the user to enter a distance in kilometers and then prints 
out how far that distance is in miles. There are 0.621371 miles in one kilometer"""

distance = eval(input('Enter a distance in km: ' ))   #TERMINAL: Enter a distance in km: 3 
print('The distance in miles is ', distance*0.621371) #The distance in miles is  1.8641130000000001
                                                               
"""Introductory Question 3
Print 2, 6, 10, 14, 18, . . . , 98, 102,all on the same line separated by spaces."""

for x in range(2,106,4):
    print(x,end=" ") #end allows  to print without newline. All results will end in one line 

#Section 2:Introductory loop questions

"""Introductory Loop Question 1
Print the output below. It has 10 A's,followed by 5 copies of BCD, followed by one E, followed by 15 F's. 
Output: AAAAAAAAAABCDBCDBCDBCDBCDEFFFFFFFFFFFFFFF"""

for i in  range(10):
    print('A',end ="")
for i in range(5):
    print('BCD',end='')
print('E',end ='')
for i in range(15):
    print('F',end='') #TERMINAL:AAAAAAAAAABCDBCDBCDBCDBCDEFFFFFFFFFFFFFFF

#or
for i in  range(10):
    print('A',end ="")
for i in range(5):
    print('BCD',end='')
for i in range(1):
    print('E',end='')
for i in range(15):
    print('F',end='') #TERMINAL:AAAAAAAAAABCDBCDBCDBCDBCDEFFFFFFFFFFFFFFF

"""Introductory Loop Question 2
Write a program that asks the user to enter a size and then draws the letter C like the one below.
 It's width and height should be equal and the size specified by the user."""

size = eval(input('Enter a number: ')) #TERMINAL:Enter a number: 5
for i in range(size-1):
    print('*',end='')
for i in range(size-2): #we can change it according to the output as width&height will b same
    print('*')
for i in range(size):
    print('*',end='') #TERMINAL:*****
#                               *
#                               *
#                               *****

"""Introductory Loop Question 3 
Print 29, 28, 27, 26, . . . , 5, 4,all on the same line separated by spaces.) """

for i in range(29,3,-1):
    print(i,end=' ') #TERMINAL:29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 

#Section 3: Number Questions

"""Number Questions 1
Write a program that asks the user for a height in inches and prints out how many feet and inches that is."""

#40/12-print with decimal point
#40//12-print a round number without decimal 
#40%12-print the remaining fo the dividened
inches = eval(input('What is the Height? '))                        #TERMINAL:What si the Height? 39
print('The Height is',inches//12,'feet and',inches%12,'inches')     #TERMINAL:The Height is 3 feet and 3 inches

"""Write a program that generates and prints 100 random numbers from 50 to 60, all on the same line,
separated by spaces."""

from random import randint
for i in range(100):
    print(randint(50,60),end=' ') #randint prints one number.In for loop,it'll print as much as times we want.
#TERMINAL:51 54 50 58 58 50 54 60 56 59 55 58 50 50 55 52 59 60 60 50 58 57 54 54 55 56 59 54 50 52
#  58 58 59 58 57 56 59 56 57 59 52 55 50 54 54 56 59 55 60 58 50 51 57 50 58 53 50 54 57 59 55 57
#  53 52 50 55 60 53 57 57 54 59 58 52 53 60 58 54 50 59 58 55 50 58 54 59 50 52 51 57 59 57 51 56 
# 54 58 53 55 51 50

"""Number Questions 2
Write a program that generates and prints 10 random zeroes and ones all on the the same line with 
no spaces between them. Then on the next line do the same but with 11 random zeroes and ones. 
On the next line do the same but with 12 random zeroes and ones. In total there should be 50 lines,
 each with one more random value than the previous line. The first few lines might look like below. 
 (Hint: You will want to use one for loop nested within another.) 
1000110101 
11100100101
110101000100
0010010001000 """

from random import randint
for i in range(10,61):
    for j in range(i):
        print(randint(0,1),end='')
    print() 
#TERMINAL:1000110101 
#         11100100101
#         110101000100
#         0010010001000

"""Number Questions 3
Some board games require you to reduce the number of cards you are holding by half, rounded down.
For instance, if you have 10 cards, you would reduce to 5 and if you had 11 cards you would also reduce to 5. 
With 12 cards you would reduce to 6. Write a program that asks the user to enter how many cards they have 
and print out what their hand would reduce to under this rule. """

cards_no = eval(input('How many cards do you have?'))    #TERMINAL:How many cards do you have?13
print('The reduced number of your cards is:',cards_no//2)#TERMINAL:The reduced number of cards for you is: 6

"""In 24-hour time, hours run from 0 o'clock (midnight) to 23 o'clock (aka 11 pm).
Write a program that asks the user for the current hour and for how many hours in the future they want to go.
Have the program print out what the hour will be that many hours in the future.
For instance, if it's 13 o'clock now, 27 hours from now it will be 16 o'clock. [Hint: Use the mod operator.]"""

now = eval(input('What is your current hour?')) #TERMINAL:What is your current hour?18
more = eval(input('Hours in the future you want to go?'))#TERMINAL:Hours in the future you want to go?12
print('Hours in the future:',(now+more)%24) #TERMINAL:Hours in the future: 6

#Section 4:If statement Questions

"""If Statement Questions 1
Ask the user for a length in feet. Then ask them which unit they want to convert to 
(inches, centimeters, or meters) and print out the converted value. There are 12 inches in a foot,
 30.48 cm in a foot, and .3048 meters in a foot. If the unit chosen is not one of the above, 
 then print out an error message 
"""
length= eval(input('What is your length in feet?'))
unit = input('In unit you want to convert to (inches, centimeters, or meters):')
if unit == 'inches':
    print('length in inches:',length*12)
elif unit == 'centimeters':
    print('length in centimeters:',length*30.48)
elif unit == 'meters':
    print('length in meters:',length*.3048)
else:
    print('invalid length')

"""If statement Question 2
Write a program that asks the user to enter a number. If the number is not 0, 2, S or between 10 and 15 or 
between 20 and 25, then the word "Okay" should be printed. Otherwise, nothing should happen."""

number = eval(input('Enetr a number: '))
if not(number==0 or number==2 or number==5 or 10<number<15 or 20<number<25):
    print('Okay')
else:
    print('nothing should happen')

"""If Statement Question 3
Write a program that generates 100 random zeros and ones. Whenever a 0 is generated, the program should print
out a question mark and whenever a 1 is generated An asterisk should be printed. Have everything be printed
on the same line."""

from random import randint
for r in range(100):
    r= randint(0,1)
    if r==0:
        print('?',end='')
    else:
        print('*',end='')

"""If Statement Question 4
Write a program that prints out on separate lines the following 200 item: file0.jpg, filel.jpg file199.jpg,
except that it should not print anything when the number ends in 8, like file8.jpg ,file18.jpg, etc. 
[Hint: if i % 10 is not 8, then i doesn't end in 8.]"""

for i in range(200):
    if i%10 !=8:
        print('file',i,'.jpg')

"""If Statement Question 5
This is a very simple billing program. Ask the user for a starting hour and ending hour,
both given in 24-hour format (e.g., 1 pm is 13, 2 pm is 14, etc.).The charge to use the 
service is $5.50 per hour. Print out the user's total bill. You can assume that the service
will be used for at least 1 hour and never more than 23 hours. Be careful to take care of 
the use that the starting hour is before midnight(11pm=23) and the ending time is after midnight. 
"""

start = eval(input('Enter the start hour(1-23): ')) 
end = eval(input('Enter the end hour(23-24): '))
if end>=start:
    print('The charge is:$',(end-start)*5.50)
else:
    print('The charge is:$',(24-start+end)*5.50)

"""If Statement Question 6
One way to solve math equations is by trial and error. Compares can help with that.
the equation 21x2 - x3 + 21904 = 0 has an integer solution between 1 and 100.
Use a for loop and an if statement to find it."""

for x in range(1,101):
    if 21*x**2-x**3+21904 == 0:
        print(x)

"""If statement Question 7
Write a program to play the following game. the program should randomly generate 10 addition problems
with three numbers ranging from 20 to SO (for example 23+50+37). For each problem, the user guesses 
thr answer. If they get the answer exactly right, print 'Right!' If their answer is within 5 of the 
correct answer, print "Close!' Otherwise, print 'Wrong.' 
"""
from random import randint
for i in range(10):
    a= randint(20,51)
    b= randint(20,51)
    c= randint(20,51)
    print(a,'+',b,'+',c,'=?')
    ans = eval(input('Enter your guess for result: '))
    if ans==(a+b+c):
        print('Right')
    elif abs(ans-(a+b+c))<=5:
        print('Close!')
    else:
        print('Wrong')

#Section 5: Various Topics Try yourself Part 1

"""Various Topic Question 1
In the game Yahtzee, players roll five dice. A Yahtzee is when all five dice are the same.
Write a program that simulates rolling five 10,000 times and counts how many Yahtzees occur.
Print out what percentage of the rolls come out to be Yahtzees."""

from random import randint
count=0
for i in range(10000):
    r1=randint(1,6)
    r2=randint(1,6)
    r3=randint(1,6)
    r4=randint(1,6)
    r5=randint(1,6)
    if r1==r2==r3==r4==r5:
        count+=1
print(count)
print('The percentage of the rolls: ',(100*(count/10000))) 

"""Various Topic Question 2
Write a program that uses a loop to ask the user to enter 5 numbers.Print out how many numbers are positive
and add up all the numbers."""
count=0
total=0
for i in range(5):
    number= eval(input("Enter a number: "))
    if number>0:
        count+=1
        total+=number
print('There are ',count,' positive numbers and the summation is ',total)


"""Various Topic Question 3
Write a program that randomly generates 5 numbers from 1 to 5 and asks the user to guess each number.
For each guess print out whether it is right or wrong. At the end, print out how many the user gets right and
how many they get wrong."""

from random import randint
count=0
for i in range(5):
    r=randint(1,5)
    guess= eval(input('Guess a number(1-5): '))
    if guess==r:
        print('Right!')
        count+=1
    else:
        print('Wrong')
print('No of Right answer is: ',count,'and the no of wrong answer is: ',5-count)

"""Various Topic Question 4
Write a program that generates 20 random numbers from 1 through 10. Print all of the generated numbers
on the same line. Just once, after all the numbers have been printed, print out whether or not the same
number was ever generated twice in a row. [Hint: use a variable to keep track of the most recently 
generated number.] 
"""
from random import randint
repreat =False
previous=randint(1,10)
print(previous,end=' ')
for i in range(19):
    r=randint(1,10)
    print(r,end=' ')
    if previous==r:
        repreat=True
    previous=r
print()
if repreat:
    print('There are the same number was generated twice in a row')
else:
    print('There is no repeat')

"""Various Topic Questions 5
One way to estimate probabilities is to run what is called a computer simulation. Here we will estimate
the probability of rolling doubles with two dice (where both dice come out to the sae value). To do this,
run a loop 10,000 times in which random numbers are generated representing the dice and a count is kept 
of how many times doubles appear. Print out the final percentage of rolls that are doubles."""
    
from random import randint
count=0
for i in range(10000):
    r1= randint(1,6)
    r2= randint(1,6)
    if r1==r2:
        count+=1
print('Doubles appeared',count,'times and percentage of double coming is ',(100*count/10000))

"""Various Topic Questions 6
Write a program that randomly generates 10 numbers from 1 to 10 and asks the user to guess each number.
For each guess print out whether it is right, wrong, or close (within in 1 of the right answer).
Also keep score, where players score 5 for a correct guess, 2 for a close guess, and -1 for a wrong guess.
Print the accumulated score after each guess."""

from random import randint
score=0
for i in range(10):
    n=randint(1,10)
    guess=eval(input('Guess number(1-10): '))
    if guess==n:
        print('Right!')
        score+=5
    elif (guess-n)==1:
        print('Close!')
        score+=2
    else:
        print('Wrong!')
        score+=-1
    print('The accumulated score is: ',score)

"""Various Topic Questions 7
Write a program that adds up 1 + 3 + 5 + 7 + • • • + 999 """

sum=0
for i in range(1,1000,2):
    sum=sum+i
print(sum)

#Section 7: String questions
"""String Questions 1
Write a program that asks the user to enter a number (but just read in that value as a string).
Print out whether that number is an integer or a floating point number. Floating point numbers 
contain decimal points, while integers don't."""

num = input("Enter a number: ")
if '.' in num:
    print("It's a floating point number")
else:
    print("It's a integer")

"""String Questions 2
Write a program that asks the user to enter a programming language. If the language entered is Python,
then print out a message saying that they entered Python. Otherwise don't print out anything.
The program should work regardless of which letters of Python are capitalized 
(it should recognize, Python, python, PYTHON, and even PyTHoN). 
"""

language= input('Write a programming language: ')
if language.lower() =='python':
    print('The language entered is Python')

"""String Questions 3
Write a program that asks the user to enter a sentence, removes all the spaces from the sentence, 
converts the remainder to uppercase, and prints out the result."""

s= input ('Enter a sentence: ')
s=s.replace (' ','')
s=s.upper()
print(s)

"""String Questions 4
Write a program that asks the user to enter a string, replaces all the spaces with asterisks,
then replaces every fifth character (starting with index 0) with an exclamation point, and
finally concatenates three copies of that result together. For example, this is a test would become
!his a is • a a lestlhis * !s • a • lestlhis * Is a • lest."""

s= input ('Enter a string: ')
s=s.replace (' ','*')
t=""
for i in  range(len(s)):
    if i%5==0:
        t+= '!'
    else:
        t+= s[i]
t=t*3
print(t)

"""String Questions 5
Write a program that asks the user to enter a string. If the string is at least five characters long,
then create a new string that consists of the first five characters of the string along with three 
asterisks at the end. Otherwise add enough exclamation points (!) to the end of the string in order 
to get the length up to five. 
"""
s= input('Enter a word: ')
if len(s)>=5:
    s=s.replace(s[- 3:], '***')
else:
    s=s+'!'*(5-len(s))

print(s)

"""String Questions 6
Write a program to find if the string has alphabet characters. Then print out (all on the same line)
the indices of the string that contain letters. The string is A B?*C, the program would output 
0, 2, and 5 since the only letters are at those indices."""

s = 'A B?*C'
for i in range(len(s)):
    if s[i].isalpha():
        print(i,end=' ')

"""String Questions 7
Write a program that does the following: It first asks the person to enter their first and last names
(together on the same line). For simplicity, assume their first and last names are one word each. 
Then ask them for their gender (male/female). Finally ask them if they prefer formal or informal address.
Uppercase/lowercase should not matter when they make their selections. Then print a line that says hello 
to them, using Mr. or Ms. <last name> if they ask for formal address and just their first name otherwise.
Here are two sample runs: 

Name: Don Knuth                                       Name: Grace Hopper
Gender: male                                          Gender: Female
Formal/Informal: informal                             Formal/informal: Formal
Hello, Don.                                           Hello, Ms. Hopper."""

n= input("What's your name(first and last name? ")
g= input('Enter your gender: ')
f= input('Formal/Informal: ')
breakpoint= n.index(' ')
first= n[:breakpoint]
last= n[breakpoint+1:]
if f.lower()=='formal':
    if g.lower()=='male':
        print("Hello, Mr.",last)
    else:
        print("Hello, Ms.",last)
else:
    print('Hello,',first)

"""String Questions 8
String consists of multiple words. Then print out the first letter of each word, all on the same line.
s = 'The weather is so nice'"""

#oneway:split and then append
s = 'The weather is so nice'
l = s.split()
z=[]
for i in range(len(l)):
    z.append(l[i][0])
print(z)

#otherway
s = 'The weather is so nice'
for i in range(len(s)):
    if s[i]==' ':
        print(s[i+1],end=' ')


"""String Questions 9
Use the string given below. Then for each lowercase letter, if the letter is not in the string,
print out a message indicating that and otherwise print out the index of the first occurrence of that 
letter in the string s = 'have a wonderful day'"""

s = 'have a wonderful day'
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in s:
        print(c,'is not in the string')
    else:
        print(c,'is in the idex of',s.index(c))

"""String Questions 10
There is an email below. Assume for this problem that email addresses are of the form username@somedomain.com,
where there is a user name and a domain name separate by the @ symbol. Print out the user name and domain
name on separate lines. email = 'johnnash@hotmail.com'"""

#oneway
email = 'johnnash@hotmail.com'
z=email.index('@')
username= email[:z]
domainname= email[z+1:]
print('User Name: ',username)
print('Domain Name: ',domainname)

#otherway
email = 'johnnash@hotmail.com'
s=email.split('@')
print('User Name: ',s[0])
print('Domain Name: ',s[1])

#Section 7:List Questions
"""List Questions 1
Write a program that creates and prints a list of the square roots of the integers from 1 to 100,
each rounded to 4 decimal places."""
from math import sqrt
l=[]
for i in range(1,100):
    l.append(round(sqrt(i),4))
print(l)

"""List Questions 2
Use the list below create a program. Create a new list that contains just the entries from the random list 
that are greater than 50. L= [1,2,3,4,76,46,45,67,48,90,23,34,56,34]"""

L= [1,2,3,4,76,46,45,67,48,90,23,34,56,34]
N=[]
for i in L:
    if i>50:
        N.append(i)
print(N)

"""List Questions 3
Use list of numbers below. Then print out the smallest thing in the list and the first index at which
it appears in the list. L= [34,34,23,26,35,37,89,56,48,30,48,19,97,40]"""

L= [34,34,23,26,35,37,89,56,48,30,48,19,97,40]
best=0
for i in range(len(L)):
    if L[i]<L[best]:
        best=i
print('The smallest thing in the list is',L[best],"and it's index is",best)

"""List Questions 4
Write a program that uses a list of numbers below with some of the values greater than 10.Print out the
smallest item in the list that is larger than 10. L = [1,5,23,26,24,37,89,56,48,30,48,19,97,9]"""

L = [1,5,23,26,24,37,89,56,48,30,48,19,97,9]
max=max(L)
for i in L:
    if 10<i<max:
        max=i
print('Smallest item larger than 10 in the list:',max)   
