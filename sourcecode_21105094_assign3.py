# Assignment 3

#Ques 1

print('                Program 1')
input_str=input('Enter a word or a sentence(give space between words and puctuation marks): \n').lower()
a=input_str.split()   #Storing the words of a sentence in a list 'a'
t1=tuple(input_str)   #Storing the characters of word in a tuple 't1' 
b=list()              #Creating empty lists 'b' and 'c'
c=list()
#Checking for spaces in the input string and printing the number of occurrences of each word
if (' ' in input_str) == True:
    for i in a:
        if i not in b:
            b.append(i)
    for j in range(0,len(b)):
        d=b[j]
        print(d,' occurs ',input_str.count(d),' times ')
    print("Note: If you want frequency of every charachter,remove the space between words and any unexpected space at start or end(if there)") 
#Checking if input string is a single word and printing the number of occurrences of each character
elif (' ' in input_str) == False: 
    for i in t1:
        if i not in c:
            c.append(i)
    for j in range(0,len(c)):
        d=c[j]
        print(d,' occurs ',input_str.count(d),' times ')
else:
    print('Error')

#Ques2

print('                Program 2')
day1 =int(input('Enter day(from 1 to 31): '))
month1 =int(input('Enter month(from 1 to 12): '))
year1 =int(input('Enter year(from 1800 to 2025): '))
a=year1%4        #Remainder when the year entere is divided by 4
b=year1%400      #Remainder when the year entere is divided by 100
if day1<=27 and day1>=1:
  if month1<=12 and month>=1:
    day2= day1+1
    month2= month1
    year2= year1
  else:
    day2='-'
    month2='-'
    year2='-'
    print("Error in month ")
elif day1==28:
  if month1==2 and a==0:
     if year1%100 ==0 and b==0:
       day2= 29
       month2= 2
       year2= year1
     elif year1%100 ==0 and b!=0 :
       day2= 1
       month2= 3
       year2= year1
     else:
         day2= 29
         month2= 2
         year2= year1
  elif month1==2 and a!=0:
     day2= 1
     month2= 3
     year2= year1
  elif month1<=12 and month1>=1 and month1!=2:
     day2= 29
     month2= month1
     year2= year1
  else:
     day2='-'
     month2='-'
     year2='-'
     print("Error in month")
elif day1==29:
  if month1!=2 and month1>=1 and month1<=12:
     day2=30
     month2= month1
     year2= year1
  elif month1==2 and a==0:
       if year1%100 ==0 and b==0:
         day2= 1
         month2= 3
         year2= year1
       elif year1%100 ==0 and b!=0 :
         day2='-'
         month2='-'
         year2='-'
         print('Error: This year is not a leap year, therefore has only 28 days in Feb')
       else:
         day2= 1
         month2= 3
         year2= year1 
  elif month1==2 and a!=0:
     day2='-'
     month2='-'
     year2='-'
     print('Error: This year is not a leap year, therefore has only 28 days in Feb')
  else:
     day2='-'
     month2='-'
     year2='-'
     print("Error in month")
elif day1==30:
  if month1<=7 and month1>=1 and month1%2==0:
     day2=1
     month2= month1+1
     year2= year1
  elif month1<=7 and month1>=1 and month1%2!=0:
     day2= 31
     month2= month1
     year2= year1
  elif month1>7 and month1<=12 and month1%2==0:
     day2= 31
     month2= month1
     year2= year1
  elif month1>7 and month1<=12 and month1%2!=0:
     day2= 1
     month2= month1+1
     year2= year1
  else:
      day2='-'
      month2='-'
      year2='-'
      print("Error in month")
elif day1==31:
  if month1<=7 and month1>=1 and month1%2!=0:
     day2= 1
     month2= month1+1
     year2= year1
  elif month1<=7 and month1>=1 and month1%2==0:
     print('Error: There are 30 days in the month entered')
  elif month1>7 and month1<12 and month1%2==0:
     day2= 1
     month2= month1+1
     year2= year1
  elif month1>7 and month1<12 and month1%2!=0:
     print('Error: There are 30 days in the month entered')
  elif month1==12:
     day2= 1
     month2= 1
     year2= year1 +1
  else:
     day2='-'
     month2='-'
     year2='-'
     print("Error in month")
else:
     day2='-'
     month2='-'
     year2='-'
     print("Error in date(especially in day and/or month)")
print('Next date(dd,mm,yyyy) is: \n',day2,',',month2,',',year2)

#Ques 3

print('                Program 3')
input_numb= input('Enter a list of numbers separated by commas: \n')
a1= input_numb.split(',')     #Storing the numbers entered after separating them about the commas in list 'a1'
b1= list()                    #Creating empty lists 'b1' and 'c1'
c1= list()
#Storing the numbers in list 'b1' without repitition
for j in range(0,len(a1)):
    if int(a1[j]) not in b1:
        b1.append(int(a1[j]))
#Storing the squares of numbers in list 'c1'
b2= sorted(b1)
for k in range(0,len(b2)):
    c1.append(b2[k]**2)
square= zip(b2,c1)            #Combining the numbers and their squares in tuple form
print('Squares of the corresponding numbers: \n',list(square))

#Ques 4

print('                Program 4')
input_grade= int(input('Enter grade points: '))
points=[4,5,6,7,8,9,10]
grade=['D','C','+C','B','+B','A','+A']
performance=['Poor','Below Average','Average','Good','Very Good','Excellent','Outstanding']
if input_grade<4 or input_grade>10:
    print('Error: Input grades are out of range. Should be from 4 to 10.')
#Printing the grade and performance corresponding to input points
else:
    for j in range(0,len(points)):
       if input_grade==points[j]:
         print('Your Grade is %s and %s Performance.'%(grade[j],performance[j]))

#Ques 5

print('                Program 5')
times=int(input('Enter number of lines to be printed: '))
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if (times>=1) and (times<=13):
  for n in range(1,times+1):
      d=' '*(n)+alphabets[0:(2*times-2*n+1)]     #Adjusting the initial spacing and number of characters to be printed in each line
      print(d)
elif times==0:
    print("")
else:
    print('Error: Number of lines must be between 1 and 13')

#Ques 6

print('                Program 6')
details= dict()
n=0
while n==0:
    ques1 =input("Do you want to make an entry? (type 'Y' for 'Yes' and 'N' for 'No') \n")
    n+=1
print('''Note:
1) SIDs are positive numbers.
2) All names must be written with capital first letter.
3) Full name should be written, especially if more than one students have same first and middle name(if there).
4) No two(or more) students should be assigned the same SID. 
''')
if ques1=='Y':
  sid= int(input('Enter SID: '))
  name= input('Enter Name: ')
  details[sid]=name
  while (n>=1)==True:
      ques=input("Do you want to make another entry? (type 'Y' for 'Yes' and 'N' for 'No') \n")
      if ques=='Y':
        sid= int(input('Enter SID: '))
        name= input('Enter Name: ')
        details[sid]=name
      elif ques=='N':
          print('OK')
          break
      else:
          print("Error: You have to type 'Y' or 'N' only")
elif ques1=='N':
    print('OK')
else:
    print("Error: You have to type 'Y' or 'N' only")
    
# Part a)
print("     Part a) ")
print("Details of student(s) : \n",details)

# Part b)    
print("     Part b) ")
details_sort_names={}
keys1= list(details.keys())
keys1.sort()
values1=list(details.values())
values1.sort()
for index1 in range(0,len(values1)):
    for index2 in range(0,len(keys1)):
        if details[keys1[index2]]==values1[index1]:
          details_sort_names[keys1[index2]]=values1[index1]
print('Details of student(s) after sorting by names: \n',details_sort_names)

#Part c)     
print("     Part c) ")
details_sort_sid={}
for index in  range(0,len(keys1)):
   details_sort_sid[keys1[index]]=details[keys1[index]]
print('Details of student(s) after sorting by sid: \n',details_sort_sid)

#Part d)     
print("     Part d) ")
print('Search details of a student: \n')
search_name= int(input('Write SID of the student: \n'))
for position in range(0,len(keys1)):
    if search_name==keys1[position]:
        a=details[keys1[position]]
        print('Name of the student is : \n',a)
    elif search_name!=keys1[position]:
        continue
if (search_name in keys1)==True:
    print('')
elif (search_name in keys1)==False:
    print('''Error: This SID hasn't been entered by the user yet.
       Enter it first.''')
else:
    print('Error')

#Ques 7

print('                Program 7')
input_numb=int(input('Enter the number of terms to be displayed in sequence: '))
fib_seq=[]                                    #Creating an empty list 'fib_seq'
fib_seq.append(0)
fib_seq.append(1)
for n in range (2,input_numb):
    nth_term= fib_seq[n-1] + fib_seq[n-2]     #Property/Formula for fibonacci sequence
    fib_seq.append(nth_term)
print("Fibonacci sequence (till",input_numb,"terms) :")
sum1= 0
for terms in fib_seq:
    print(terms)
    sum1+= terms                              #Calculating sum of series
print("Average of the above sequence's series is :",(sum1/input_numb))

#Ques 8

print('                Program 8')
set1= {1,2,3,4,5}
set2= {2,4,6,8}
set3= {1,5,9,13,17}
set4= set1^set2
set5= ((set1-set2-set3)|(set2-set1-set3)|(set3-set1-set2))
set6= (set1|set2|set3)-((set1-set2-set3)|(set2-set1-set3)|(set3-set1-set2))-(set1&set2&set3)
list1=[]
list2=[]
print('Given sets :\n','Set1 :',set1)
print(' Set2 :',set2)
print(' Set3 :',set3)
#Part a)
print("     Part a) ")
print('Set of elements that are in Set1 and Set2 but not in both :\n',set4)
#Part b)
print("     Part b) ")
print('Set of elements that are in only one of Set1,Set2 and Set3 :\n',set5)
#Part c)
print("     Part c) ")
print('Set of elements that are in exactly two of Set1,Set2 and Set3 :\n',set6)
#Part d)
print("     Part d) ")
for k in range(1,11):
   if k not in set1:
     list1.append(k)
print('Set of integers from 1 to 10 that are not in Set1 :\n',set(list1))
#Part e)
print("     Part e) ")
for l in range(1,11): 
   if l not in (set1|set2|set3):  
     list2.append(l)
print('Set of integers from 1 to 10 that are not in Set1,Set2 and Set3 :\n',set(list2))


