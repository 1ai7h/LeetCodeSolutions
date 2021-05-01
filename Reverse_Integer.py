class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x == '0':
            return '0'
        else:
            x = x[::-1]
            x = x.lstrip('0')
            for i in x:
                if i == '-':
                    x = x.rstrip('-')
                    x = '-' + x
                    break
            x = int(x)
            if (abs(x) > (2 ** 31 - 1)):
                return '0'
            else:
                return x



