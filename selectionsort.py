#SELECTION SORT ALGORITHM

def selectionSort(nums):

        for i in range(len(nums)):
            minimum_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minimum_index]:
                    minimum_index = j

            nums[i], nums[minimum_index] = nums[minimum_index], nums[i]
