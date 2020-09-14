#LC406
#先对身高进行排序（身高逆序,index顺序)，大的在前,依次插入.
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for i in people:
            #insert(index, element)
            ans.insert(i[1], i)
        return ans