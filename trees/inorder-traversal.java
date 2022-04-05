List<Integer> function getInorderTraversal(TreeNode root) {
    
    List<Integer> result = new List()

    Stack<TreeNode> nodeStack = new Stack()

    TreeNode node = root

    while(node is not null or nodeStack is not empty){

        while(node is not null){
            // pre order operation

            nodeStack.add(node)
            node = node.left
        }
        node = nodeStack.pop()

        // in order code
        result.add(node.val)

        node = node.right

    }
    return result
}
