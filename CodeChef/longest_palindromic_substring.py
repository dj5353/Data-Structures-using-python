def longestPalindrome(s):
    palindrome = ""
    for i in range(len(s)):
        len1 = len(getlongestpalindrome(s,i,i))
        if len1 > len(palindrome):#odd set
            palindrome = (getlongestpalindrome(s,i,i))
        len2 = len(getlongestpalindrome(s,i,i+1))
        if(len2 > len(palindrome)):#even set
            palindrome = (getlongestpalindrome(s,i,i+1))
    return palindrome

def getlongestpalindrome(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1 : r]

print(longestPalindrome("cbba"))