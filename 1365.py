def smallerNumbersThanCurrent(self, nums):
        county=[]
        temp=0
        for i in nums:
            for j in range(len(nums)):
                if i>nums[j]:
                    temp += 1
            county.append(temp)
            temp=0
        return county