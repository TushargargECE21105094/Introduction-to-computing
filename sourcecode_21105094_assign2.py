#Assignment 2

#Ques 1

print("               Program 1")
intro= "Python is a case sensitive language"
print("Input string :",intro)
#Finding length of a given string
print("               Part a)")
print("Length of the given string is :",len(intro))
#Reversing the order of a string
print("               Part b)")
reversed_intro= intro[34::-1]
print("Reversed string :",reversed_intro)
#Slicing a string
print("               Part c)")
sliced= intro[10:-9]
print("Slice :",sliced)
#Replacing words in a string
print("               Part d)")
new_intro_1= intro.replace("a case sensitive","object oriented")
print("String after a replacement :",new_intro_1)
#Finding index of a string in given one
print("               Part e)")
index_a= intro.find("a")
print('Index of "a" is :',index_a)
#Removing something from string 
print("               Part f)")
new_intro_2= intro.replace(" ","")
print("String after another replacement :",new_intro_2)

#Ques 2

print("               Program 2")
name= "Tushar garg"
sid= 21105094
dept= "ECE"
cgpa= 8.5
print('''Hey,%s here!
My SID is %d
I am from %s department and my CGPA is %f'''%(name ,sid ,dept ,cgpa))

#Ques 3

print("               Program 3")
#Applying bitwise operators
a=56
b=10
print("a&b:  ",a&b)
print("a|b:  ",a|b)
print("a^b:  ",a^b)
print("a<<2: ",a<<2,"\nb<<2: ",b<<2)
print("a>>2: ",a>>2,"\nb>>4: ",b>>4)

#Ques 4

#Finding the greatest among three numbers
x=int(input("Enter first number,x: "))
y=int(input("Enter second number,y: "))
z=int(input("Enter third number,z: "))
if x>y and x>z:
    print("x is greatest")
elif y>z:
    print("y is geatest")
else :
    print("z is greatest")

#Ques 5

input_str= input("Enter a string:\n")
if "name" in input_str:
    print("Yes")
else:
    print("No")

#Ques 6

length1= int(input("Enter first length: "))
length2= int(input("Enter second length: "))
length3= int(input("Enter third length: "))
if length1+length2>length3 and length2+length3>length1 and length1+length3>length2:
    print("Yes")
else:
    print("No")
