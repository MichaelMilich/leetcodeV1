class Solution:
    def countBits(self, n: int) -> [int]:
        """
        Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
        Return an array output where output[i] is the number of 1's in the binary representation of i.
        """
        res = [0]
        res_num = [0]
        for x in range(1, n + 1):
            prev = res[-1]
            prev_num = res_num[-1]
            if prev_num % 2 == 0:
                res.append(prev + 1)
            else:
                res.append(res[x>>1])
            res_num.append(x)

        return res


