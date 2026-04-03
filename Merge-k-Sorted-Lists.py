import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for linked_list in lists:
            node = linked_list
            while node:
                heapq.heappush_max(pq, node.val)
                node = node.next
        last_node = None
        while len(pq):
            value = heapq.heappop_max(pq)
            last_node = ListNode(value, last_node)
        return last_node