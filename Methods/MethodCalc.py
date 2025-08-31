def addnumbers(nums1,nums2):
  print('the addition of the two numbers is',(nums1+nums2))

def substractnums(nums1,nums2):
  print('the difference is ',(nums1-nums2))

def multiplynums(nums1,nums2):
  print('the multiplictaion is',(nums1*nums2))

def dividenums(nums1,nums2):
  print('the division is',(nums1/nums2))

print('welcome to the calculator bot!:)')
print('Enter your username to proceed')
name=input()
print('Enter the first number which you want to add,substact,multiply or divide below',name)
no1=int(float(input()))
print('input the second number which you want to add,substact,multiply or divide below',name )
no2=int(float(input()))
print("have fun with your math",name)
print('Input 1 for addition')
print('Input 2 for substraction')
print('Input 3 for multiplication')
print('Input 4 for division')
choice =input()
if choice=='1':
  addnumbers(no1,no2)

if choice=='2':
  substractnums(no1,no2)

if choice=='3':
  multiplynums(no1,no2)

if choice=='4':
  dividenums(no1,no2)
  