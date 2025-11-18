# Arithmatic Operators
num1 = 3
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)
print(num1**num2)

#compound Assignment operators
num = 10
num+=5
print(num)

#comparision/relational operators
num1 = 3
num2 = 2
print(num1>num2)

#logical operators
a = 10
b = 5
c = 3
d = 8
res_and = a>b and b<c
print(res_and)
res_or = a>b or b<c
print(res_or)
res_not = a<b
print(res_not)

#membership operators
text = "python is easy"
is_z_present = "z" in text
print(is_z_present)

#identity operator
num1 = 10
num2 = 10
print(num1 is num2)  

#bitwise operator
a = 5
b = 3

resand = a&b
print(resand)

resor = a|b
print(resor)

resxor = a^b
print(resxor)

resnot = ~b
print(resnot)

b = 3
print(3<<2)
print(3<<1)
print(3<<3)

print(3>>2)
print(3>>1)
print(8>>2)