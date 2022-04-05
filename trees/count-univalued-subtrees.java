int function countUnivalSubtrees(TreeNode root) {
    
    int uvCount = 0
    if(root is null) return uvCount

    boolean function countUnivalSubtreesHelper(TreeNode node) {
        
        if(node.left is null and node.right is null){
            uvcount++
            return true
        }

        flag = true

        if(node.left is not null){
            flag = countUnivalSubtreesHelper(node.left) and
              (node.val == node.left.val)
        }
        if(node.right is not null){
            flag = countUnivalSubtreesHelper(node.right) and
               (node.val == node.right.val) and flag
        }

        if(flag) uvcount ++

        return (flag)
    }
    countUnivalSubtreesHelper(root)
    return uvCount
}
