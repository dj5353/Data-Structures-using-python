#The strip() method returns a copy of the string with both leading and trailing characters removed
#  (based on the string argument passed)
#Python String. split() split() method returns a list of strings after breaking
#  the given string by the specified separator
def reverseWords(s):
    res = list(reversed(s.strip().split()))
    res1 = ""
    for i in res:
        res1 += i+" "
    return res1

print(reverseWords(" hello          my name is divit "))
