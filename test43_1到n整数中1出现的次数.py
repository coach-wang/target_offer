class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        tmp = n
        res = 0
        base = 1 #位数，1表示各位，10表示十位
        while tmp:
            last = tmp % 10  #取出当前位的值
            tmp = tmp // 10
            res += tmp * base  #temp*base得到该位出现的次数
            if last == 1:#如果这位数是1，那还要算上这位数1出现的次数
                # 举例： 1141的百位
            # 上面temp * base即1 * 100算出的是1000前百位为1的个数，1100到1141百位上的1没统计到，因此最终结果还要加上42个
                res += n % base + 1
            elif last > 1:#如果这位数大于1，那么这位数上1还出现了base次
                # 举例： 1141的十位
            # 上面temp * base即11 * 10算出的是1100前十位为1的个数，1100后还有10个没统计到
                res += base
            base *= 10
        return res
