#Binary Search Iterative

def search(nums, target):
        
    high = len(nums)
    low = 0
    for i in range(len(nums)):
        middle = (high+low)/2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            low = middle
        else:
            high = middle

    return -1