nums=[1,2,3,6,7,8,23,78,34,12]  

result = sum(nums)
print(result)  # sum of numbers in array

print(sorted(nums, reverse=True))  # ascending order of numbers in array

digitSum=[]
for number in nums:
    value=0
    for digit in str(number):
        value+=int(digit)
    digitSum.append(value)
index=nums.index(max(nums))
highest=nums[index]
print(highest)  # highest number for sum of digits

sqrtNum=[
    number ** 2 for number in nums
]

print (sqrtNum) # square root of numbers in array

even=[
    num for num in nums if num % 2 == 1
]
sum = sum(even)
print(sum) # sum of even numbers

print (even) # all even numbers

count=0
for i in range(0,len(nums)):
    if "3" in str(nums[i]):
        count+=1
print(count) # number of 3 in numbers in array



