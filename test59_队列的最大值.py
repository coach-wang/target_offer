#1 滑动窗口的最大值
#01  暴力法
class Solution:
    def maxInWindows(self, num, size):
        maxInWindows = []
        if len(num) >= size and size >= 1:
            for i in range(len(num)-size+1):
                maxInWindows.append(max(num[i:i+size]))
        return maxInWindows

#02 双端队列法
'''
在队列里存入数字在数组中的下标，而不是数值，
当一个数字与当前处理的数字下标之差大于或等于滑动窗口的大小时，这个数字已从窗口滑出，可从队列中删除
'''
class Solution:
    def maxInWindows(self, num, size):
        i = 0 #i是当前窗口中的最后一个数字下标
        queue = []
        res = []
        while size > 0 and size <= num and i < len(num):
            if len(queue) > 0 and i - size + 1 > queue[0]:#判断queue[0]是否还在当前窗口中
                queue.pop(0) 
            while len(queue) > 0 and num[queue[-1]] < num[i]:#注意这里用while不是if
                queue.pop()     #如果有num[i]更大，那么目前队列中的队尾数字不可能成为最大值的下标，删除它
            queue.append(i)
            if i >= size - 1:#i = size - 1 时，第一个窗口建立完成，开始记录最大下标
                res.append(num[queue[0]])
            i += 1
        return res
