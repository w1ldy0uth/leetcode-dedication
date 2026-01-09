class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

/**
 * 865. Smallest Subtree with all the Deepest Nodes
 *
 * We must traverse tree in post-order to determine which subtree could contain the lowest common ancestor (LCA).
 * At each step we check heights of subtrees, and when we hit the equal heights, we found the answer.
 * @param root the root of tree.
 * @returns the height of LCA.
 */
function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
  function dfs(node: TreeNode | null): [number, TreeNode | null] {
    if (!node) return [-1, null];

    const [leftHeight, leftNode] = dfs(node.left);
    const [rightHeight, rightNode] = dfs(node.right);

    const currentHeight = 1 + Math.max(leftHeight, rightHeight);

    if (leftHeight > rightHeight) return [currentHeight, leftNode];
    if (rightHeight > leftHeight) return [currentHeight, rightNode];

    return [currentHeight, node];
  }
  return dfs(root)[1];
}
