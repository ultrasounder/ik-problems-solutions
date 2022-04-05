List<List<Integer>> function getSumPaths(TreeNode root, int sum) {
    List<List<Integer>> result = new List()

    if(root is null) return results

    function hasPathSumHelper(TreeNode node, int sum, Stack slate) {
        slate.push(node.val)

        if(node.left is null and node.right is null){    
            if(sum == node.val){
                result.add(slate.copy()) // O(N)
            }
            slate.pop()
            return
        }        

        if(node.left is not null) hasPathSumHelper(node.left,
             sum - node.val, slate)
        if(node.right is not null) hasPathSumHelper(node.right, 
            sum - node.val, slate)

        slate.pop()
    }
    hasPathSumHelper(root, sum, new Stack())

    return result
        
}
