#All the question are from the blind 75 list

#1.Two Sum
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


#121. Best time to buy and sell stock
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    l = 0 #We are using two pointers left and right
    r = 1

    while r < len(prices): # loop over the list till we reach the end of the list, since r is ahead of l we use r here
        if prices[l] < prices[r]: # check if the price we buy if less and the price we sell is more
            profit = prices[r] - prices[l] # We calculate the profit 
            max_profit = max(max_profit, profit) # Calculating max profit
        else:
            l = r # if prices[l] is more than prices[r] then just shift the pointer because goal is to buy at the lowest so we shift l where r was 
        r += 1 # we just update r irrespective of any of the condition

    return max_profit

#217. Contains Duplicates
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) > len(set(nums)) #Set can only have unique elements
    # We can also use a hashmap by adding each number and if it comes again we just return True

#238. Product of Array except self
def productExceptSelf(self, nums: List[int]) -> List[int]: #We use a postfix and prefix method
    prefix = 1
    res=[] # We are calculating the prefix and postfix in the same array
    for i in range(len(nums)): # We go over the array and save the product of array before it eg[10, 5] the prefix of 5 is 10
        res.append(prefix)
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1): # We now go over from the back and do the same thing as prefix but from behind ie postfix
        res[i] *= postfix
        postfix *= nums[i]
    return res

#53. Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
    maxSum = nums[0] # We start the max sum with the first number in the array
    curSum = 0
    for n in nums:
        if curSum < 0: #We checking if cursum is less than 0 because if will just make the over all sum less eg. cursum = -3 and n is 4, 4 -3 = 1 
            curSum = 0 # We reset cursum see the above like making cursum 0 and then adding will be more so it will be 4 which is greater than 1 if we don't do this step
        curSum += n # Just adding
        maxSum = max(maxSum , curSum) 
    return maxSum

#152. Maximum Product Subarray
def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1 #We have current min and max because in multiplication -ve times -ve is +ve so we can have like -100 and after that -1 we have 100 now.
    for n in nums:
        if n == 0: # We reset the current min and max because 0 * anything is 0
            curMin, curMax = 1 , 1
            continue
        temp = curMax * n # We use temp becuase we are updating curMax so we save and use the old curMax and not the new one
        curMax = max(curMax * n , curMin * n , n) # Calculating the max 
        curMin = min(curMin* n, temp , n) # Calculating the min
        res = max(res, curMax) #Calculating the overall max 
    return res

#153. Find Minimum in Rotated Sorted Array
def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1 #We are solving this using two pointer one at the start and one at the end
    while l < r:
        m = (l + r)//2 #Caluculating the middle
        if nums[m] > nums[r]: #The array is sorted but rotated when we see middle is more than right then that means the pivot/lowest is on the right side
            l = m + 1
        else: #If not it is on the left side
            r = m
    return nums[l]

#33. Search in a rotated sorted array
def search(self, nums: List[int], target: int) -> int:
    l  , r = 0 , len(nums) - 1 #Similar to finding minimum in rotated sorted array
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1


