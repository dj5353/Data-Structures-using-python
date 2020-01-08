#index at which sum of left and  sum of right values are equal (pivot index exclusive)
def dominantIndex(nums):
        left_sum = 0 
        total = sum(nums)
        for i in range(0,len(nums)):
            if left_sum == (total - left_sum - nums[i]):
               return i 
            left_sum += nums[i]
        else:
            return -1 
print(dominantIndex([1,7,3,6,5,6]))