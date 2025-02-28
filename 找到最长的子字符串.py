"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

找到最长的子字符串。

基本思路是逐个遍历若不在new里则添加进里面，如果在new里则表示已经发生了重复，那么会对比目前的new与之前保存的子字符串长度哪个较大，
保存较大的。新的new则为发生重复的字符串直到最后+新数据。`pkwk`遍历到第二个k时new此时会变成`wk`。

因为是子字符串并不是子序列，所以这样做是可行的。

时间复杂度 O(n)

测试用例：
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #check if s is empty, then return 0
        if not s:
            return 0
        #define a list newStr to save char , put s[0] to initialize it
        newStr=s[0]
        #define a int to save max length
        max_length=0

        for i in s:
            if i not in newStr:
                newStr+=i
                continue
            #if not enter if section , then it means repeated char happened. 
            #you should do 2 things here 
            #1. save the current max length
            #2. cut out the first repeated char and append new 
            max_length=max(max_length,len(newStr))
            newStr=newStr[newStr.index(i)+1:]+i
        #这里之所以重复这句，是因为最后一个不重复的字符，无法在for循环中计入
        max_length=max(max_length,len(newStr))
        return max_length

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bu"))
