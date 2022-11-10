# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #create a dummy node pointing to the head

        lp = dummy #left pointer
        cur = head # current for the head 

        #get to the left value 
        for i in range(left-1):
            lp = cur #left pointer goes just before the reverse 
            cur = cur.next

        prev = None # set prev to none for the reverse 
        for i in range(right-left+1): # actual reverse
            nxt = cur.next #create a temp nxt node for the cur.next to point at
            cur.next = prev #current.next equals the previous (reverse)
            prev = cur #move previous over 
            cur = nxt  #move current over 

        #reattatch the reversed 
        lp.next.next = cur #first reverse value (pre reverse) next is the out of reverse current 
        lp.next = prev #left pointer (before reverse area) .next is the end of the reverse

        return dummy.next #return the head of the list 
