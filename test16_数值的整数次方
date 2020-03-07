class Solution:
    def Power(self, base, exponent):
        # write code here
        global g_InvalidInput
        g_InvalidInput = False
        if base == 0 and exponent < 0:
            g_InvalidInput = True
            return 0.0
        result = 1.0
        flag = 0
        if exponent < 0:
            flag = 1
        #for i in range(abs(exponent)):
            #result *= base
        result = self.quick(abs(exponent), base)
        if flag == 1:
            result = 1.0 /result
        
        return result

    def quick(self, exponent, base):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        
        result = self.quick(exponent>>1, base)
        result = result * result
        if exponent & 0x1:
            result *= base
        return result
