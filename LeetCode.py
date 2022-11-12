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

    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def isValid(self, s: str):
        parantheses = {")": "(", "}": "{", "]" : "["}
        stack = []
        for i in s:
            if i in parantheses.values():
                stack.append(i)
            elif stack and parantheses[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []

solution = Solution()
