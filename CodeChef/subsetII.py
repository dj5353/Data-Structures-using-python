# def subsets(nums):
#     res = []
#     backtrack(res, [], nums, 0)
#     return res

# def backtrack(res, temp, nums, start):
#     temp.sort()
#     if temp not in res:
#         res.append(temp)
#     for i in range(start, len(nums)):
#         backtrack(res, temp + [nums[i]], nums, i + 1)

# print(subsets([1, 2, 2]))

