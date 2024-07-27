class Solution:
    def addTwoNumbers(self, l1, l2) :
        new_l1 = reversed(l1)
        new_l2 = reversed(l2)

        new_l1 = self.convertToNum(new_l1)
        new_l2 = self.convertToNum(new_l2)

        res_num = new_l1 + new_l2

        return [int(digit) for digit in str(res_num)]

    def convertToNum(self, lis):
        return int(''.join(map(str, lis)))


soln = Solution.addTwoNumbers([2,4,3], [5,6,4])
print(soln)