from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    """
    2196. Create Binary Tree From Descriptions

    Build a node map in one pass, wiring left/right children as we go.
    Root is the only value that never appears as a child.
    """
    nodes = {}
    children = set()

    for parent, child, is_left in descriptions:
      if parent not in nodes:
        nodes[parent] = TreeNode(parent)
      if child not in nodes:
        nodes[child] = TreeNode(child)
      if is_left:
        nodes[parent].left = nodes[child]
      else:
        nodes[parent].right = nodes[child]
      children.add(child)

    for val, node in nodes.items():
      if val not in children:
        return node
