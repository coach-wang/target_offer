'''
排序一个长度为n的数组需要O(nlogn)的时间
使用哈希表可以使时间复杂度减小到O（n），但需要O(n)的空间复杂度
这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
函数返回True/False
'''
class Solution:
    def duplicate(self, numbers, duplication):
        if len(numbers) == 0:
            print('数组为空')
            return False
        n = len(numbers)
        for i in numbers:
            if i < 0 or i > n-1:
                print('值%d不在范围内'%i)
                return False
        Flag = True
        for i in range(n):
            while i != numbers[i]:
                m = numbers[i]
                if m == numbers[m]:
                    Flag = False
                    break
                numbers[i], numbers[m] = numbers[m], numbers[i]
            if Flag == False:
                break
        if Flaf == True:
            print('未找到重复数字')
            return False
        else:
            duplication[0] = numbers[i]
            return True
