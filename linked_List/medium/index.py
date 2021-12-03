#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution:
  def __init__(self):
    self.head = None  
  
  def addTwoNumbers(self, l1, l2):
    dummy = ListNode(0)
    current = dummy
    # 次の計算に使う用
    carry = 0
    # l1, l2, carryがすべて計算に使えなくなるまでroot
    while l1 or l2 or carry > 0:
      # 桁ごとに計算
      total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
      # 割った整数部分を次の計算にも使う
      carry = total // 10
      # 次のpointerに10で割ったあまり
      current.next = ListNode(total % 10)
      current = current.next
      # l1あれば、pointerを進める
      if l1:
        l1 = l1.next
      # l2あれば、pointerを進める
      if l2:
        l2 = l2.next
    
    return dummy.next

l1_1 = ListNode(1)
l1_2= ListNode(2)
l1_3 = ListNode(4)
l1_4 = ListNode(6)
l1_5 = ListNode(8)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5

s = Solution()

