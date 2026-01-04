#All the question are from the blind 75 list

#Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hsh =  {} #Using a hashmap
    diff = 0
    lst = []
    for i , j in enumerate(nums):
        diff = target - j #We are subtracting the target and current number(j) from the list
        if diff in hsh: #Now we are checking if diff is in the list because in the line above we have already calculaed the diff
            lst.append(i) # We are adding to list if we find a match
            lst.append(hsh[diff])

        hsh[j] = i #We are just adding to the hashmap
    return lst #returning the list
