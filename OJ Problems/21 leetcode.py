class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy is a placeholder node so we always have something to attach to
        # current tracks where we are in the merged list
        dummy = ListNode(0)
        current = dummy
        # walk both lists until one runs out
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1      # attach the smaller node
                list1 = list1.next        # advance list1 pointer
            else:
                current.next = list2      # attach the smaller node
                list2 = list2.next        # advance list2 pointer

            current = current.next        # move current forward
        # at least one list is now empty
        # attach whatever remains (it's already sorted)
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        # dummy.next is the actual head of our merged list
        return dummy.next