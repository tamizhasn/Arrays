nums=[1,2,3,3,4,5,6,7,7]
nums.sort()
n=len(nums)

index=0
for i in range(n-1):
    if nums[i] !=nums[i+1]:
            nums[index]=nums[i]
            index +=1

print(nums)