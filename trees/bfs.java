List<List<Integer>> function getLevelOrder(TreeNode root) {    

    // make result array
    List<List<Integer>> result = new List()

    if(root is null) return result

    Queue<TreeNode> nodeQueue = new Queue()
    nodeQueue.add(root)

    
    while(nodeQueue is not empty){
        int queueSize = nodeQueue.size()
        List<Integer> temp = new List()

        for(i in range queueSize){

            TreeNode node = nodeQueue.remove()

            temp.add(node.val)

            // add children to the queue
            if(node.left is not null) nodeQueue.add(node.left)
            if(node.right is not null) nodeQueue.add(node.right)
        }
        result.add(temp)
    }

    return result

}
