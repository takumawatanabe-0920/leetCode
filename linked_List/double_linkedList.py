#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None

  def createList(self, array):
    length_ = len(array)
    start = self.head
    i = 0
    current = start 
    while (length_ > i):
      createNode = Node(array[i])
      if i == 0:
        start = createNode
        current = start
      else:
        current.next = createNode
        createNode.prev = current
        current = current.next
      i += 1
    
    self.head = start
    return start

  def printList(self):
    current = self.head
    print(current)
    linked_list = ''
    while current:
      linked_list += (str(current.val) + " ")
      current = current.next

    print(linked_list)

  def _countList(self):
    current = self.head
    count = 0
    while current:
      current = current.next
      count += 1
    return count

  def insert(self, val, index):
    list_count = self._countList()
    current = self.head
    createNode = Node(val)

    # 先頭への挿入
    if index == 1:
      createNode.next = current
      current.prev = createNode
      self.head = createNode
      return self.head
    # 末尾への挿入
    # + 1はまだ存在していない要素であるため（挿入予定）
    if list_count + 1 == index:
      # 末尾までpointer
      while current.next != None:
        current = current.next

      current.next = createNode
      createNode.prev = current
      return self.head

    # 通常の挿入
    i = 1
    # 前のnodeにアクセス
    while index - 1 > i:
      current = current.next
      i += 1
    # current.nextが上書きされるので、current.nextを退避
    targetNode = current.next

    createNode.next = targetNode
    targetNode.prev = createNode
    # current.nextを上書き
    current.next = createNode
    createNode.prev = current

    return self.head

  def delete(self, index):
    list_count = self._countList()
    i = 1
    current = self.head
    
    if index > list_count:
      return current

    # 先頭の削除
    if index == 1:
      self.head = current.next
      return  self.head

    # 末尾への削除
    # 末尾が存在しているから + 1にしない
    if index == list_count:
      while current.next != None and current.next.next != None:
        current = current.next
      current.next = None
      return self.head
    
    # 通常の削除
    while index - 1 > i:
      current = current.next
      i += 1

    prevNode = current
    targetNode = current.next
    nextNode = targetNode.next

    # targetNodeをpointerから外す
    # prevNodeとnextNodeを紐づける処理
    nextNode.prev = prevNode
    prevNode.next = nextNode

    return self.head
    
arr = [1, 2, 5, 3, 2]
llist = LinkedList()
llist.createList(arr)
llist.insert(8, 4)
llist.delete(6)
llist.printList()
