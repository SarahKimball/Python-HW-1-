
def any_seven(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:
        if num == 7: 
            return True
    return False

print("should be true", any_seven([1, 2, 7, 4, 5]))
print("should be false", any_seven([1, 2, 4, 5]))
