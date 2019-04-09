#1 A good Frist Program

print("This is my first python program")
print("i learn how to print a line in python")

#2 Comments and Pound Characters

print("a line for comments")   #  this is print line
'''for
multi line 
comments''' #this is example of multi line comments

#3 Numbers and Maths

a=10
print("Aman Has "+str(a)+" cows")
pen=5
lunchBox=1
mobile=1
bag=1
print("mohit have total "+str(pen+lunchBox+mobile+bag)+" items")
a=10
b=20
c=30
d=a+b+c
e=b-a
f=c/a
print("sum is  " +str(d)+ " and substation is " +str(e)+ " division is: " +str(f))

#4 Variables and names

train=40
loco_pilot=25
pessenger=1000
Driven_train= loco_pilot
total_pessenger= pessenger*Driven_train
print("Total Train= "+ str(train)+ " Driven Train "+str(Driven_train)+" Total Pessengerr" +str(total_pessenger))

#5 More Variables and Printing

my_name = 'Brijesh Kumar'
my_age = 21 # not a lie
my_height = 72 # inches
my_weight = 70 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d kg heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)
print ("If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight))

#6 String and Text

x = "There are %d types of people." % 189
Hindi = "Hindi"
do_not = "don't"
y = ("Those who know %s and those who %s." % (Hindi, do_not))
print (x)
print (y)
print ("I said: %s." % x)
print( "I also said: '%s'." % y)
funny = False
joke_evaluation = ("Isn't that joke so funny?! %r")
print (joke_evaluation % funny)
w = ("This is the left side of...")
e = ("a string with a right side.")
print (w + e)

#7 More Printing

one="B"
two="R"
three="I"
four="J"
five="E"
six="S"
seven="H"
Eight="K"
nine="U"
Ten="M"
eleven="A"
Twelve="R"
print("My Name is :" )
print(one+two+three+four+five+six+seven+" "+Eight+nine+Ten+eleven+Twelve)

#8printing printing

f = "%s %s %s %s"
print (f % (1,2 , 3, 4))
print (f % ("A", "B", "C", "D"))
print (f % (False, True, False, True))
print (f % (f, f, f, f))

#9Printing Printing Printing

Name = "Mayank Brijesh Agam Ayushi Dicya Amisha Abhishek Ritin"
Age = "25\n21\n27\n19\n20\n22\n24\n25"
print ("Here are the Name: ",Name)
print ("Here are the Age: ",Age)

#10 What Was That

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
 I'll do a list:
 \t* Cat food
 \t* Fishies
 \t* Catnip\n\t* Grass
 """
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#11 Asking Questions

print ("Whats your name?",)
name =input()
print ("How tall are you?",)
height =input()
print ("How much do you weigh?",)
weight =input()
print ("So, you're name is %r , %r tall and %r heavy." % (
 name, height, weight))

#12 Prompting People

age =input("How old are you? ")
height =input("How tall are you? ")
weight =input("How much do you weigh? ")
print ("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))

#13 Parameters, Unpacking, Variables

from sys import argv
script, first, second, third, forth, five, six, = argv
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
print ("Your forth variable is:", forth)
print ("Your fifth variable is:", five)
print ("Your sixth variable is:",six)

#14 Prompting and

file, user_name = argv
prompt = '<'
print ("Hi %s, I'm the %s file." % (user_name, file))
print ("I want to ask you a some questions.")
print ("Do you have car %s?" % user_name)
likes =input(prompt)
print ("Where do your place %s?" % user_name)
lives =input(prompt)
print ("which machine are you using?")
computer =input(prompt)
print ("""
ok, so you said to me %r about choice me.
Your place in %r. Not sure where that is.
And you have a %r machine. good.
 """ % (likes, lives, computer))

#15 Reading Files

script, filename = argv
txt = open(filename)
print ("File %r:" % filename)
print (txt.read())
print("file name:")
file_twise =input("> ")
txt_twise = open(file_twise)
print (txt_twise.read())

#16 Reading and Writing Files

from sys import argv
file, title = argv
print ("Delete all stuff from file  %r." % title)
print ("for skip deletion press ctrl+C.")
print ("for removing write RETURN.")
input("?")
print ("opening is going on")
target = open(title, 'w')
print ("Truncating the file. Goodbye!")
target.truncate()
print ("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")
line5 = input("line 5: ")
line6 = input("line 6: ")
print ("write all lines into the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")
target.write(line5)
target.write("\n")
target.write(line6)
target.write("\n")

#17 More Files

from sys import argv
from os.path import exists
a.py, from_file1, to_file2 = argv
print ("Copying from %s to %s" % (from_file1, to_file2))
in_file = open(from_file1)
data = in_file.read()
print ("size of file in byte is %s" % len(data))
print ("File is exist? %r" % exists(to_file2))
print ("Ready, hit RETURN to continue, CTRL- C to abort.")
input()
out_file = open(to_file2, 'w')
out_file.write(data)
print ("DONE!!!!!!.")
out_file.close()
in_file.close()

#18 Names, Variables, Code, Functions

def print_two(*args):
     arg1, arg2 = args
     print ("arg1: %r, arg2: %r" % (arg1, arg2))
def print_two_again(arg1, arg2):
     print ("arg1: %r, arg2: %r" % (arg1, arg2)
def print_one(arg1):
     print ("arg1: %r" % arg1)
def print_none():
     print ("I got nothin'.")

def print_3(*args):
    arg1, arg2, arg3 = args
    print("arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3))
def print_2(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2)
def print_1(arg1):
    print("arg1: %r" % arg1)
def print_0():
    print("I got nothin'.")
print_two("Brijesh","Mayank")
print_two_again("Brijesh","Mayank")
print_one("Number1!!!!!!! :) ")
print_none()
print_3("Amisha","Ayushi", "Divya")
print_2("Amisha","Ayushi")
print_1("Number1!!!!!!! :) ")
print_none()

#19 Functions and Variables

def nut_and_barry(nut_count, number_of_Barry):
    print ("You have %d nut!" % nut_count)
    print ("You have %d number of barry!" % number_of_Barry)
    print ("people that's enough for a party!")
    print ("Get a beer.\n")
print ("give function numbers directly:")
nut_and_barry(40, 60)
print ("OR, we can use variables from our script:")
amount_of_nut = 71
amount_of_barry = 80
nut_and_barry(amount_of_nut, amount_of_barry)
print ("We can calculate:")
nut_and_barry(13 + 10, 6 + 5)
print ("And we can combine the two, variables and math:")
nut_and_barry(amount_of_nut + 100, amount_of_barry + 1000)

#20 Functions and Files

from sys import argv
script, input_file = argv
def print_all(f):
    print (f.read())
def rewind(f):
     f.seek(0)
def print_a_line(line_count, f):
     print (line_count, f.readline())
current_file = open(input_file)
print ("First let's print the whole file:\n")
print_all(current_file)
print ("Now let's rewind, kind of like a tape.")
rewind(current_file)
print ("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

#21 Functions Can Return Something
def add(a, b):
     print ("ADDING %d + %d" % (a, b))
     return a + b
def subtract(a, b):
     print ("SUBTRACTING %d - %d" % (a, b))
     return a - b
def multiply(a, b):
     print ("MULTIPLYING %d * %d" % (a, b))
     return a * b
def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b
print ("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

#24 More Practice
print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
poem = """
 \tThe lovely world
 with logic so firmly planted
 cannot discern \n the needs of love
 nor comprehend passion from intuition
 and requires an explanation
 \n\t\twhere there is none.
 """
print ("- - - - - - - - - - - - - - ")
print (poem)
print ("- - - - - - - - - - - - - - ")

#30 if else

people = 30
cars = 40
buses = 15
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
   else:
    print("We can't decide.")
if buses > cars:
     print("That's too many buses.")
elif buses < cars:

      print("Maybe we could take the buses.")
else:
      print("We still can't decide.")
if people > buses:
     print("Alright, let's just take the buses.")
else:
     print("Fine, let's stay home then.")

#31 Making Decision

print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")
door = input("> ")
if door == "1":
   print ("There's a giant bear here eating a cheese cake. What do you do?")
   print ("1. Take the cake.")
   print ("2. Scream at the bear.")

bear =input("> ")

if bear == "1":
    print ("The bear eats your face off. Good job!")
elif bear == "2":
     print ("The bear eats your legs off. Good job!")
else:
     print("Well, doing %s is probably better. Bear runs away." % bear)
elif door = "2":
     print ("You stare into the endless abyss at Cthulhu's retina.")
     print ("1. Blueberries.")
     print ("2. Yellow jacket clothespins.")
     print ("3. Understanding revolvers yelling melodies.")
insanity = input("> ")
if insanity == "1" or insanity == "2":
     print ("Your body survives powered by a mind of jello. Good job!")
else:
     print( "The insanity rots your eyes into a pool of muck. Good job!")
     print ("You stumble around and fall on a knife and die. Good job!")























