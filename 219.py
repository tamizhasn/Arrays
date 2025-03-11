def containsNearbyDuplicate(nums, k):
        indices={}
        for i,num in enumerate(nums):
            if num in indices:
                if i-indices[num] <= k:
                    return True
                
            indices[num]=i
        return False
nums=[1,2,3,1,2,3]
k=3
containsNearbyDuplicate(nums, k)
