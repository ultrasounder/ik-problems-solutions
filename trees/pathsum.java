boolean function hasPathSum(TreeNode root, int sum) {
    boolean pathSumFlag = false

    if(root is null) return pathSumFlag

    function hasPathSumHelper(TreeNode node, int sum) {
        if(pathSumFlag) return

        if(node.left is null and node.right is null){    
            pathSumFlag = (sum == node.val)
            return
        }

        if(node.left is not null) hasPathSumHelper(node.left,
             sum - node.val)
        if(node.right is not null) hasPathSumHelper(node.right, 
            sum - node.val)
    }
    hasPathSumHelper(root, sum)

    return pathSumFlag
        
}
