#chuong trình máy tính thực hiện các phép tính cộng, trừ, nhân , chia
#phép cộng hai so
def add(x,y):
    return x + y
#phép trừ 2 so
def subtract(x,y):
    return x - y
#phép nhân 2 so
def multiply(x,y):
    return x*y
#phép chia 2 so
def divide(x,y):
    return x/y
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice =='2':
     print(num1,"-",num2,"=",subtract(num1,num2))
elif choice =='3':
     print(num1,"*",num2,"=",multiply(num1,num2))
elif choice =='4':
     print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")
