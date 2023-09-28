numbers = [5, 2, 13, 7, 6, 4]
index=0
max=numbers[index]
min=numbers[index]
sum=0
while index<len(numbers):
    sum = sum + numbers[index]
    if numbers[index]>max:
        max=numbers[index]
    if numbers[index]<min:
        min=numbers[index]
    index=index+1
sum=sum-max-min
print(sum)
print(max)
print(min)

mass=[1,2,3,4,5,6,7,8,9,10]
index = 0
sum=0
while index<len(mass):
    sum=sum+mass[index]
    index+=1
sred=sum/len(mass)
print(sred)

numbers = [5, 2, 13, 7, 6, 4]
index=0
max=numbers[index]
min=numbers[index]
while index<len(numbers):
    if numbers[index]>max:
        max=numbers[index]
    if numbers[index]<min:
        min=numbers[index]
    index=index+1
sum=sum-max-min
print(numbers.index(max))
print(numbers.index(min))



