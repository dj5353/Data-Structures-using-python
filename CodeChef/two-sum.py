hash_map = {}
def two_sum(nums,target):
    for i,j in enumerate(nums):
        hash_map[j] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in hash_map and hash_map[complement] != i):
            return [i,hash_map[complement]]
            


print(two_sum([3,2,4],target = 6))