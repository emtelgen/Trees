#INSERTION SORT

def insertionSort(nums):

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                for j in range(i, 0, -1):
                    if nums[i] < nums[j-1]:
                        nums[i], nums[j-1] = nums[j-1], nums[i]
                        i = j-1