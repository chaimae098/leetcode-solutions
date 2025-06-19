class Solution:
    #smt diff
    ## my first leetcode problem
    def intToRoman(self, num):
        if not type(num) is int :
            raise TypeError("The value should be an interger.")
        try :
            if num >= 1 and num <= 3999 :
                print("The value is correct .")    
        except: 
            print("The value is incorrect .")
        dict ={
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        result =""
        for value  in sorted(dict.keys(), reverse=True):
            count = num // value 
            if count > 0 :
                result += dict[value] * count 
                num -= value * count 
        return result         

s = Solution()
print(s.intToRoman(3749))

        