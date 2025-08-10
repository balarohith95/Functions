#convert a floating-point number to an inter in python

num=float(input("Enter a floating-point number: "))
print(int(num))

#convert a string "7" to int and multiply it by 5.
x=7
x=int(x)
result=x*5
print(result)

#convert an integer to float

num=int(input("Enter a number:"))
print(float(num))


#convert string '3.1415' to float and add 1.
x="3.1415"
convert=float(x)+1
print(convert)

#create a complex number from real and imaginary inputs
x=5
y=4
z= complex(x,y)
print(z)

#return square of a complex number using complex().
z=complex(5,4)
square=z**2
print(square)

#round 6.72849 to 2 decimal places.
num=6.72849
rounded=round(num,2)
print(rounded)

#round user-input float to nearest integer.
num = float(input("Enter a floating-point number: "))
rounded = round(num)
print(rounded)

#find min and max from[2,5,1,9,-3,6].

numbers=[2,5,1,9,-3,6]
min=min(numbers)
max=max(numbers)
print(min)
print(max)





#problems on pow()


sum= pow(2,5)
print(sum)




base=int(input("enter a base:"))
exponent=int(input("enter the exponent:"))
sum=pow(base, exponent )
print(sum)



sum=pow(2,3,5)
print(sum)

quotient, remainder = divmod(23, 5)
print("Quotient:", quotient)
print("Remainder:", remainder)




def get_quotient_remainder(a, b):
    quotient, remainder = divmod(a, b)
    return quotient, remainder

# Example usage
q, r = get_quotient_remainder(23, 5)
print("Quotient:", q)
print("Remainder:", r)




num=float(input("enter a number"))
value=abs(num)
print(value)


a=float(input("enter first number"))
b=float(input("enter second number"))
difference=abs(a-b)
print(difference)


x=int(input("enter a x- coordinate:"))
y=int(input("enter y-coodinate:"))
distance=abs(x)+abs(y)
print(distance)

#bonus

a=int(input("enter a number:"))
b=int(input("entera number:"))
multiply=a*b
print(multiply)


sum=pow(5,3)
div=sum/7
print(div)


# x=[-2,-8,3,7]
# largest_abs=max(x,key=abs)
# print("largest_abs:", abs(largest_abs))


x=float(input("enter a number:"))
y=round(x)
sum=pow(2,y)
print(y)
print(sum)

