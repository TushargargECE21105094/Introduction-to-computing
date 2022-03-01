#Assignment 4

#Ques 1
print("                    Ques 1")
def TowerofHanoi(n,source,final,helper):
    if n==1:
        print("Move disk 1 from",source,"to",final)
        return
    TowerofHanoi(n-1,source,helper,final)
    print("Move disk",n,"from",source,"to",final)
    TowerofHanoi(n-1,helper,final,source)
print('''Three disks are in 'A' rod initially and will be in 'B' rod finally .\n''')
#Calling function TowerofHanoi
TowerofHanoi(3,'A','B','C')
print('''


''')

#Ques 2
print("                    Ques 2")
#Ques 2 1)
print("Using recursions 1")
def pt(n,list1):
    if n==0:
        return
    
    pt(n-1,list1)
    
    a=len(list1)
    list2=list1.copy()
    list1.append(1)
    for count in range(0,a):
        if count==0:
            list1[0]=1
        else:
            list1[count]=list2[count]+list2[count-1]
    pp(list1)
def pp(list01):
    print((' '*(n+2-len(list01))),end='')
    for item in list01:
        print(item,"  ",end='')
    print()
n=int(input('Enter number of rows to be printed: '))
initial_list=[]
pt(n,initial_list)
print('''

''')

#Ques 2 2)
print("Using recursions 2")
def pasc_tri(n):
    if n==1:
        return [[1]]             #Base case termination condition 
    else:
        result= pasc_tri(n-1)
        #Calculating current row using info from previous row
        curr_row= [1]           
        prev_row= result[-1]     #Take from end of 'result'
        for i in range(len(prev_row)-1):
            curr_row.append(prev_row[i]+prev_row[i+1])
        curr_row= curr_row+[1]
        result.append(curr_row)
        return result
m= int(input("Enter number of rows to be printed: "))
triangle = pasc_tri(m)
for row in triangle:
    print(((m-len(row))*' '),end='')
    for item in row:
        if (item>=100):           # for better clarity in triangle we can adjust spaces between numbers in a row
          print(item,' ',end='')  # here it is done for triangle with number of rows till 13
        elif (item>=10):
          print(item,'  ',end='')
        else:
          print(item,'   ',end='')
    print()    
print('''

''')

#Ques 2 3)
print("Using iterations")
n= int(input("Enter number of rows to be printed: "))
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(' ',end='')
    c=1                           #First element is always 1
    for k in range(1,i+1):
        print(' ',c,end='')       #First value in a line is always 1 
        c=c*(i-k)//k              #using Binomial Coefficient
    print()
print('''


''')

#Ques 3
print("                    Ques 3")
numb1= int(input('Enter first number: '))
numb2= int(input('Enter second number(should be non-zero): '))
quot_rem= divmod(numb1,numb2)
print(" Quoteint is: ",quot_rem[0])
print(" Remiander is: ",quot_rem[1])

 #Part a)
call= callable(divmod)
if call==True:
    print('Function is callable.')
elif call==False:
    print('Function is not callable.')
    
 #Part b)
if quot_rem[0]==0 and quot_rem[1]==0:
    print('Both Quotient and Remainder are zero.')
elif quot_rem[0]!=0 and quot_rem[1]==0:
    print('Remainder is zero but Quotient is non zero.')
elif quot_rem[0]==0 and quot_rem[1]!=0:
    print('Quotient is zero but Remainder is non zero.')
else:
    print('Both Quotient and Remainder are non zero.')
    
 #Part c)
list1=list((quot_rem))
list1 =list1+[4,5,6]
t1=tuple(list1)
print('New result :',t1)
greater_than_4=[]
for value in range(len(t1)):
    if t1[value]>4:
       greater_than_4.append(t1[value])
print('Values greater than 4 are:\n',tuple(greater_than_4))

 #Part d)
set_form= set(tuple(greater_than_4))
print('After converting to Set datatype:\n',set_form)

 #Part e)
immutable_set=frozenset(set_form)
print('Immutable Set:\n',immutable_set)

 #Part f)
largest=max(set_form) 
print("Largest value in the set: ",largest)
print("Hash value of the largest value in the set:",hash(largest))
print('''


''')

#Ques 4
print("                    Ques 4")
class Student():
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        print(f"Object created for {self.name}")
    def details(self):
        print("Name of student",self.name)
        print("Roll no. of student",self.rollno)
    def __del__(self):
        print(f"Object deleted for {self.name}")
student4= Student("Rahul Garg",53)
student3= Student("Manushi Jain",49)
student2= Student("Jagdish Mishra",25)
student1= Student("Anmol Gupta",17)
student1.details()
student2.details()
student3.details()
student4.details()
del student1
del student2
del student3
del student4
print('''


''')

#Ques 5
print("                    Ques 5")
class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    def info(self):
        print("Name of Employee",self.name)
        print("Salary of Employee",self.salary)
    def __del__(self):
        print(f"{self.name}'s record is deleted")
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
employee1.info()
employee2.info()
employee3.info()
employee1.salary = 70000
print("The updated salary of Mehak is 70000.")
del employee3
print('''


''')

#Ques 6
print("                    Ques 6")
init_word= input("Enter a word:").lower()
test_word= input("Enter a new meaningful word to test your friendship:").lower()
t1=tuple(init_word)  #Storing each letter of the word in a tuple
t2=tuple(test_word)
set_a=set(t1)       #Making Set to avoid repetition of letters
set_b=set(t2)
if set_a==set_b:  #Cheking if all letters are same in both the words
     #ASking the shopkeeper whether the new word has some meaning or not and printing the result accordingly
      meaning_check= input("Please enter whether the new word has meaning or not(Y or N): ")
      if meaning_check== 'Y':
            print("WOW! You and your friend passed the friendship test.")
      elif meaning_check== 'N':
            print("OOPS! You and your friend failed the friendship test.") 
      else:
            print('''Error :Please enter a valid input.''')
            print(" 'Y' or 'N' is the only valid input.")
else:
    print("OOPS! You and your friend failed the friendship test.")
print('''


''')

    
    
    
