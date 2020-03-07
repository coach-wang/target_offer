class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not isinstance(s, str):
            print('非字符串')
            return
        lis = list(s)
        lis_rep = []
        for i in lis:
            if i == ' ':
                lis_rep.extend('%20')
            else:
                lis_rep.append(i)
        return ''.join(map(str,lis_rep))
