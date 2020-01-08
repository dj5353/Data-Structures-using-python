def findMaxConsecutiveOnes(nums):
        count = 0
        res = []
        s= []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        else:
            for i in nums:
                if i == 1:
                    count += 1
                else:
                    res.append(count)
                    count = 0
            res.append(count)
            s = sorted(res)
            return s[-1]
print(findMaxConsecutiveOnes([1,1,1,1,0,0,0,1]))