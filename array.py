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

