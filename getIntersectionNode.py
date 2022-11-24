# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #set pointers
        a = headA
        b = headB
        #loop while they dont intersect
        while a != b:
            a = a.next if a else headB  
            # move a to the next value in a list. 
            # If you hit the end move the pointer to the b list

            b = b.next if b else headA # same for b

        # Eventually the two pointers will meet at the intersection ending the loop
        # and returning the intersection point.

        return a
