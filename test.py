def subsetXORSum(nums):
    total_sum = 0
    dp = [0]  # Initial DP value for the empty subset

    for num in nums:
        new_dp = []
        for xor_val in dp:
            new_dp.append(xor_val ^ num)  # Include the current number in the subset
        dp.extend(new_dp)  # Combine new subsets with the previous subsets

    total_sum = sum(dp)
    return total_sum


# Example usage
nums = [1,3]
result = subsetXORSum(nums)
print("The sum of all subset XOR totals is:", result)
