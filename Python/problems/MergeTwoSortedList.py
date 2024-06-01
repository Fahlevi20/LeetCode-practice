class ListNode:
 def __init__(self, val=0,next=None):
  self.val=val
  self.next=next

def MergeTwo(list1:ListNode,list2:ListNode):
 dummy = ListNode()
 tail=dummy

 while list1 and list2:
  if list1.val < list2.val
   print(list1)
   tail.next(list1)
  else:
   tail.next=list2
   tail = tail.next
 

list1 = [1,2,4], list2 = [1,3,4]

MergeTwo(list1,list2)
