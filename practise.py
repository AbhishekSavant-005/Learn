'''print("Hey,",end="and")
print("Abhi")

print("Hey, Abhi")'''
# print("hello","World",sep="**\n")
# print("hello**")
# print("world")
'''a=input("Enter value\n")
print(a)
a=14
b=2.9
print("{a}+{b}={c}".format(a=a,b=b,c=a+b))'''
# a1= int(input("Enter the value:\n"))
# char = float(a1)
# print(type(char))
# s = input("Enter the string:\n")
# c= s.reverse()
# if(len(s)==0):
#     print("Empty string")
# else:
#     if(s==c):
#         print('palindrome')
#     else:
#         print('not palindrom')
# a= int(input("Enter the number:\n"))
# print(a*a)
# a=input("Enter the string:\n")
# c= len(a)
# # length of string
# if(c!=0):
#     for i in range(0,c,1):
#         print(a[i])
# else:
#     print("empty string")
#   round off to 2 digits after decimal point
# num= float(input("Enter the number:\n"))
# num= round(num,2)
#  print(num)

# printing factorial numbers
'''a=int(input("Enter the number:\n"))
 i=a
 fact=1
 while i>=1:
   fact*=i
   i=i-1
 print("Factorial of",a,"is",fact)
 '''
 
 #fibannoci numbers
'''
number=int(input("Enter the number:\n"))
a=0
b=1
print(a,b,sep='\n')
for i in range(0,number):
  sum=a+b
  a=b
  b=sum
  
  print(sum)
'''
# standard form
'''fibannocci_numbers= int(input("Enter the numbers:\n"))
first_number=0
second_number=1
if fibannocci_numbers==1:
  print(first_number)
elif fibannocci_numbers==2:
  print (first_number,second_number,sep='\n')
elif fibannocci_numbers>=3:
  print(first_number,second_number,sep='\n')
  for i in range (0,fibannocci_numbers):
   sum_of_two_numbers=first_number+second_number
   first_number=second_number
   second_number=sum_of_two_numbers
   print(sum_of_two_numbers)'''
   
   #string reversal by using list slicing concept
'''word= input("Enter anything:\n")
print(word)
print(word[::-1])'''

#string formattig 
'''name= 'Abhishek'
usn='2vd20cs003'
branch='CS'
print("student details are:\n")
          # different type of string formatting
print("the student name is ",name,'and usn is '+usn+f'and from the branch {branch}')
print(f"Student name is {name} and usn is {usn} and from the branch {branch}")'''

# printing the date difference with the help of string slicing
'''day="printing the required date in dd-mm-yyyy format"
print(day)
date =int(input("Enter the date:\n"))
month=int(input("Enter the month:\n"))
year=int(input("Enter the year:\n"))

date1=int(input("Enter the current date:\n"))
month1=int(input("Enter the current month:\n"))
year1=int(input("Enter the current year:\n"))

print(f"Difference is: {date1-date}{month1-month}-{year1-year}")'''

# printing vowels after readig vowels from console
'''word=input("enter the word:\n")
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
n=len(word)
if n==0:
  print('empty string')
else:
  for i in word:
    if i in vowels:
      count+=1
print(f"number of vowels are {count} in {word}")'''

# printing number of vowels after reading vowels from console
'''word= input('word?:\n')
for vowel in ['a','e','i','o','u']:
  count=0
  for letter in word:
    if letter.lower()==vowel:
      count +=1
  print(f'{vowel}-{count}')
  
  Another method
  word=input("Enter word:\n")
vowel='a,e,i,o,u,A,E,I,O,U'
count=0
for char in word:
  if char in vowel:
    count+=1
print(count)
  '''
  
# to print words and number of words in given sentence using split()
'''sentence= input("Enter the sentence:\n")
list_of_words_in_sentence= sentence.split()
print(list_of_words_in_sentence)
 print(len(list_of_words_in_sentence))'''

''' sentence=input("Enter sentence:\n")
 list=sentence.split()
 for word in list:
   if(list==sentence):
     print("Words are repeated")
   else:
     print(word)'''


#   This function checks if a given number is an Armstrong number.

#   An Armstrong number is a number that is equal to the sum of the cubes of its digits.

#   For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.
'''
input_number=int(input("Enter the number:\n"))
temp=input_number
sum=0
while temp>0:
  digit=temp%10
  sum+=digit**3
  temp//=10
if input_number==sum:
  print(f"Given number {input_number} is armstrong number")
else:
  print ( f"{input_number} is not an armstrong number ")'''
  
# to print sum of odd or even digits from given number
'''num=int(input("Enter the number:\n"))
sum1=0
sum2=0
while num>0:
  digit=num%10
  if digit%2==0:
    sum1+=digit
  elif digit%2!=0 :
    sum2+=digit
  num=num//10
print ("Sum of Even Digits:",sum1,"\nSum Of Odd Digits:",sum2 )'''

# printing reverse of given number
'''num=int(input("Enter the number:\n"))
reversed_number=0
while num>0:
  digits=num%10
  reversed_number=(reversed_number*10)+digits
  num//=10
print("Given number's reversed number is",reversed_number,sep=('\n'))'''

# printing largest,smallest, sum of given number
'''num=int(input("Enter the number:\n"))
l_num=0
s_num=0
sum=0
while num>0:
  digit=num%10
  if digit>l_num:
    l_num=digit
  elif digit<s_num:
    s_num=digit
  sum+= digit
  num//=10

print(sum,l_num,s_num)'''

# to print minimum, maximum, average of the given number
'''
n= int(input("Enter count of number: "))
total=0.0
count=0
min=n
max=n
print("Enter the number")

while count<n:
 num=int(input())
 count+=1
 if min>num:
   min=num
 elif max<num:
   max = num
 else:
   total=total+num
   avg=total/count
   
print('min:',min,'max:',max,'average:'avg)'''

# to read list from user input and finding max n  min elements
# n=int(input('Enter the number of elements:\n'))
# l=[]
# for i in range(n):
#   l.append(int(input()))
# min_element=l[0]
# max_element=l[0]  
# for number in l:
#   if min_element>number:
#     min_element=number
#   elif max_element<number:
#     max_element=number
# print(f'Elements are:{l}\nMin number is {min_element} and Maximum number is {max_element}')

#  to read list from usr input and printing sum of elements from list
# n=int(input())
# l=[]

# for i in range (n):
#   l.append(int(input()))

# sum=0
# for  digit in range(n):
#   sum+=l[digit]
# print('elements are:',l)
# print(f'sum is:{sum}')
# avg=sum/n
# print(f'avg is:{avg}')

# to read input from user input and printing sub array of odd elements in the list
n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
for digit in l:
  if digit % 2 !=0:
    