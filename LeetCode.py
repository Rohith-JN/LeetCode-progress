class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])

    def plusOne(self, digits):
        num = int(''.join(map(str,digits))) + 1
        res = [int(x) for x in str(num)]
        return res

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        if s[::-1] == s:
            return True
        else:
            return False
        
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1,len(nums)):
            ans ^= nums[i]
        return ans

    def merge(self, nums1, m: int, nums2, n: int):
        nums1 = nums1[0:m]
        nums2 = nums2[0:n]
        nums1 = nums1 + nums2
        nums1.sort()
        print(nums1)

solution = Solution()
solution.merge([1], 1, [], 0)