class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cursor=dummy=ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1,cursor=list1.next,list1
            else:
                cursor.next = list2
                list2,cursor=list2.next,list2

        if list1 or list2:
            cursor.next = list1 if list1 else list2

        return dummy.next
        
        