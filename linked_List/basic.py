#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    current = self.head
    print(current)
    linked_list = ''
    while current:
      linked_list += (str(current.val) + " ")
      current = current.next

    print(linked_list)
  
  def insert(self, val, pos):
    insertNode = Node(val)
    if pos == 0:
      insertNode.next = self.head
      self.head = insertNode
      return

    # 挿入する前のNodeを取得
    prev = self._getPrevNode(pos)
    # prev.nextを退避
    nextNode = prev.next
    # prev.nextを退避
    prev.next = insertNode
    insertNode.next = nextNode
  
  def delete(self, targeVal):
    current = self.head
    if current == None:
      return
    if current.val == targeVal:
      self.head = current.next
      current = None
      return
    # nextのNodeがkeyと一緒になるまで進める
    while current.next.val != targeVal:
      current = current.next

    targetNode = current.next
    current.next = targetNode.next
    targetNode = None

  def _getPrevNode(self, index):
    count = 1
    current = self.head
    while index > count:
      current = current.next
      count += 1
    return current

first_node = Node(5)
second_node = Node(2)
third_node = Node(1)
four_node = Node(3)

linked_List = LinkedList()
linked_List.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = four_node


linked_List.insert(3, 2)
linked_List.delete(2)
linked_List.printList()