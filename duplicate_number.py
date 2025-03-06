def removeDuplicates(nums):
        result = [nums[0]]
        for i in range(0,len(nums)-1):
            if i != len(nums)-1:
                if (nums[i] != nums[i+1]):
                    result.append(nums[i+1])
        k=len(result)
        a=len(nums)-len(result)
        for i in range(a-1):
             result.append('_')
        return k, result   

nums=[1,1,2,2,3,4,5,6,6,7,7,8,8,8,9,9]
print(removeDuplicates(nums))