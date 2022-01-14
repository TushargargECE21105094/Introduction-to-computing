#ASSIGNMENT 1

#PROGRAM 1
#Calculating average of three numbers entered by user
numb1 =float(input("Enter first number:"))
numb2 =float(input("Enter second number:"))
numb3 =float(input("Enter third number:"))
avg =(numb1+numb2+numb3)/3
print("Average is=",avg)

#PROGRAM 2
#Calculating a person's income tax 
print('''Tax Rate =0.2
Standard Deduction =10000
Dependent Deduction per dependent member =3000''')
tax_rate =0.2
standard_deduction =10000
dependent_deduction =3000
gross_income =float(input("enter gross income:"))
number_of_dependents =int(input("enter number of dependent persons:"))
taxable_income =gross_income-standard_deduction-(dependent_deduction*number_of_dependents)
tax =taxable_income*tax_rate
print("Taxable Income:",taxable_income)
print("Tax applicable:",tax)

#PROGRAM 3
#Storing information of a student
print("Student=[SID,Name,Gender,Dept. name,CGPA]")
student=[21105094,'Tushar Garg','M','ECE',7.8]
print("Student=",student)

#PROGRAM 4
#Making a list of marks of 5 students and sorting marks
Marks=[89,53,18,45,56]
print("List before sorting",Marks)
Marks.sort()
print("List after sorting",Marks)

#PROGRAM 5
#a) REMOVING ELEMENT IN LIST
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)

#b) <1> REMOVING AND REPLACING ELEMENT IN LIST
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)
color.pop(3)
print(color)
color.insert(3,'Purple')
print(color)
#b) <2> REMOVING AND REPACING ELEMENT IN LIST
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['Purple']
print(color)

