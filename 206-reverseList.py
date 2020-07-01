# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 前驱pre 后继next
        if not head: return None
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
        # 递归
        # if head  == None or head.next == None:
        #     return head
        # nextNode = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return nextNode

        #以下链接为实现翻转链表讲解 忘了可去看看
        # https://blog.csdn.net/weixin_39561100/article/details/79818949