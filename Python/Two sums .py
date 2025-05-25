# Write a program to find two numbers from list that add up to the target.

# nums=[2,7,11,15] , target=9

# Two sums :-

nums=[2,7,11,15]
target=9
for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j] == target):
                print(nums[i],"+",nums[j],"= target")
