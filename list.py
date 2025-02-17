number = [1,2,3,4,5,6,7,8,9,10]


fruits = ['apple', 'banana','cherry']

maxed_list = [1,2,3,'apple','banana','orange', True]

number[3] = 2
number.remove(2)
print(number[3])

squared_number = [num**2 for num in number]
print(squared_number)


for i in range(2,4   ):
    print(f"Multipletion of number{i}:")
    
    for j in range(1,11):
        result = i * j
        print(f"{i} x {j} =",result)
    print('')