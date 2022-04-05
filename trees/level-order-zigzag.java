List<List<Integer>> function getZigZagLevelOrder(TreeNode root) {    

    // make result array
    List<List<Integer>> result = new List()
    boolean flip = false

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
           foreach (child in node.children) {
               nodeQueue.add(child)
           }
        }
        if(flip) temp.reverse()
        result.add(temp)

        flip = not flip
    }

    return result

}


