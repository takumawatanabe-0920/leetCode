#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
      self.head = ListNode(0)
      # pointer用 そしてl1とl2をmergeする
      current = self.head

      while l1 and l2:
        if l1.val >= l2.val:
          # current.nextに小さい方のlistを挿入
          current.next = l2
          # l2を進める
          l2 = l2.next
        else:
          current.next = l1
          l1 = l1.next
        # listを挿入したcurrent.nextのpointerを進める
        current = current.next

      # 長さが違うListの場合、マージ仕切れないnodeが存在する。なので、それぞれのnodeがなくなるまでマージする。
      while l1:
        current.next = l1
        l1 = l1.next
        current = current.next

      while l2:
        current.next = l2
        l2 = l2.next
        current = current.next

      return self.head.next

    # 同じnodeに再び通過したら、true
    def hasCycle(self, head):
        setNode = set()
        while head:
          # valが同じだけど違うnodeの可能性があるので、valではなくnodeのインスタンスを入れる必要がある。インスタンスのIDが同じだったら、ループがあるlistであると言える。
          if head in setNode:
            return True
          setNode.add(head)
          head = head.next
            
        return False

    def hasCycle2(self, head):
        if head is None:
          return False
        slow = head
        fast = head.next
        # slowとfastのインスタンスを比較している
        while slow != fast:
          # firstがNoneになるというのは、サークルではない。サークルはtailがない
          if fast is None or fast.next is None:
              return False
          slow = slow.next
          fast = fast.next.next

        # slowとfastのインスタンスが同じインスタンスだったらwhileを抜けてTrue
        return True

    def reverseList(self, head):
      current = head
      prev = None

      while current:
        # step1 pointerを進めるために、変数を保持しておく
        nextNode = current.next
        # step2 currentのnextNodeにprevNodeを代入する
        current.next = prev
        # step3 prevに次のroop用にcurrentを代入 && reverseされたnodeが入っている
        prev = current
        # step4
        current = nextNode
      
      return prev



l1_1 = ListNode(1)
l1_2= ListNode(1)
l1_3 = ListNode(4)
l1_4 = ListNode(6)
l1_5 = ListNode(8)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = l1_4

l2_1 = ListNode(1)
l2_2= ListNode(5)
l2_3 = ListNode(6)

l2_1.next = l2_2
l2_2.next = l2_3

print(l1_1, l2_1)

s = Solution()
# result = s.mergeTwoLists(l1_1, l2_1)
result2 = s.hasCycle(l1_1)
# result3 = s.reverseList(l2_1)
print(result2)

# while result3 != None:
#   print(result3.val)
#   result3 = result3.next