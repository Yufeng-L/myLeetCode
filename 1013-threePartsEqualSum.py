class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 本题也可用双指针做
        # runtime: 99.32%
        # memory: 98.29%
        partition,Sum,count = sum(A)/3,0,0
        checksum = partition
        for ele in A:
            # 写这个是为了类似[10,-10,10,-10,10,-10,10,-10]的case,遍历到最后的元素之前count已经等于3了 但是后面加起来是等于partition.
            if count == 3:
                checksum += ele
                continue
            Sum += ele
            if Sum == partition:
                count += 1
                Sum = 0
        return count == 3 and checksum == partition
        