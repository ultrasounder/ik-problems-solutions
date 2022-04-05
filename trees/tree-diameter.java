int function getTreeDiameter(TreeNode root) {
    int maxDiameter = 0
    if(root is null) return maxDiameter

    int function getTreeDiameterHelper(TreeNode node) {

        if(node.left is null and node.right is null) return 0

        int lmax = 0
        int rmax = 0

        if(node.left is not null) 
            lmax = getTreeDiameterHelper(node.left) + 1

        if(node.right is not null)
            rmax = getTreeDiameterHelper(node.right) + 1
        
       // maxDiameter = Math.max((lmax+rmax), maxDiameter)

	// or use ternary operator
        maxDiameter =
         ((lmax + rmax) > maxDiameter)? lmax + rmax : maxDiameter

        return Math.max(lmax, rmax)
        
    }
    getTreeDiameterHelper(root)
    return maxDiameter

}
