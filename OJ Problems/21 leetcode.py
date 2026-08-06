class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        for i in list1:
            new_list.append(i)
        for j in list2:
            new_list.append(j)
        new_list.sort()
        return new_list