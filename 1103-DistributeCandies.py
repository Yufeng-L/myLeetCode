# 依次分糖果
# hard code 对位置进行遍历，若最后一次candies数量小于0，返回并修复正确数量
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # length = num_people
        res = num_people*[0]
        count = 1
        while (candies != 0):
            for i in range(num_people):
                res[i] = res[i] + count
                candies = candies - count
                if candies < 0:
                    res[i] = res[i] + candies
                    return res

                count += 1
        
        return res

