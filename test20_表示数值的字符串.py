#方法1
class Solution:
    # s字符串
    def isNumeric(self, s):
        sign = False   #符号
        decimal = False  #小数点
        hasE = False  #E
        for i in range(len(s)):
            if (s[i] == 'e' or s[i] == 'E'):
                #e后面一定要接数字
                if i == len(s)-1:
                    return False
                #不能同时有两个E
                if hasE == True:
                    return False
                hasE =True
            elif (s[i] == '+' or s[i] == '-'):
                #第二次出现+-符号必须紧跟e之后
                if sign and (s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                #第一次出现+-符号，且不是在字符串开头，则也不许紧跟在e之后
                elif (sign == False and i > 0 and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                sign = True
            elif (s[i] == '.'):
                #e后面不接小数点，小数点不出现两次
                if hasE or decimal:
                    return False
                #第一位不是小数点
                if i == 0:
                    return False
                decimal = True
            #非法字符
            elif(s[i] < '0' or s[i] >'9'):
                return False
        return True

#方法2，用try偷鸡
class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            p = float(s)
            return True
        except:
            return False
