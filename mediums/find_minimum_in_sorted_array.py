'''
The solution is to reverse the entire array, then reverse *again* the array from i = 0 to k - 1 (aka, the portion of the array that had to wrap around because i + 2 > len(nums)), and then reverse the elements after that *didn't* have to curl around. Somehow... it works. 
The original solution I had, although intuitive, takes up O(N) time because you have to duplicate the array if you're going to manipulate an element directly without storing it.
Bummer.
'''


def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        # reverse the array
        l, r = 0, len(nums) - 1
        while l < r:
            swap(nums, l, r)
            l += 1
            r -= 1
        
        l, r = 0, k - 1

        while l < r:
            swap(nums, l, r)
            l += 1 
            r -= 1
        
        l, r = k, len(nums) - 1

        while l < r:
            swap(nums, l, r)
            l += 1
            r -= 1

        """ 
        [1, 2, 3, 4, 5, 6, 7]
        shift is 2
        [7, 6, 5, 4, 3, 2, 1]
        [6, 7, 1, 2, 3, 4, 5]
        print(nums)
        """
