class Solution(object):
    def isPalindrome(self, s):
        new_word =''
        for ch in s:
            if ('A'<=ch <='Z') or ('a'<=ch <='z') or (ch.isdigit()==True):
                new_word +=ch
        new_word = new_word.lower()
        n = len(new_word)
        for i in range(n//2):
            if (new_word[i]!=new_word[n-i-1]):
                return False
        return True    

        