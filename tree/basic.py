#!/usr/bin/env python2
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def inOrder(node):
  if node != None:
    inOrder(node.left)
    # print(node.val)
    inOrder(node.right)

def inOrder2(node):
  stack, res = [], []
  current = node

  while current or stack:
    while current:
      stack.append(current)
      current = current.left
    
    current = stack.pop()
    res.append(current.val)
    current = current.right
  # print(res)
  return res

def preOrder(root):
  if root is None:
      return []
  stack,result = [root,], []
  
  while stack:
      root = stack.pop()
      if root is not None:
          result.append(root.val)
          if root.right is not None:
              stack.append(root.right)

          if root.left is not None:
              stack.append(root.left)
  print(result)
  return result

root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

	# 	           4 
	# 	       /       \ 
	# 	      5	        6 
	#       /  \      /   \ 
  #      7   None  None  None
  #     / \
  # None   None

inOrder(root)
inOrder2(root)
preOrder(root)