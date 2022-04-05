TreeNode function arrayToBst(int[] input) {
    TreeNode function arrayToBstHelper(int[] input, int s, int e){

        if(s > e) return null

        int mid = s + (e-s) / 2

        TreeNode root = new TreeNode(input[mid])

        root.left = arrayToBstHelper(input, s, mid - 1)
        root.right = arrayToBstHelper(input, mid + 1, e)

        return root
    }
    return arrayToBstHelper(input, 0, input.length-1)
}


TreeNode function arrayToBst(int[] preOrder, int[] inOrder) {

    Map<int, int> ioMap = new Map()

    for(int i = 0; i < inorder.length; i++){
        ioMap.put(io[i], i)
    }

    TreeNode function arrayToBstHelper(int[] po, int pos, int poe,
                                       int[] io, int ios, int ioe){

        if(pos > poe) return null                                        
        

        TreeNode root = new TreeNode(po[pos])
        int rootIdx = ioMap.get(po[pos]) // O(1)

        int count = rootIdx - ios

        root.left = arrayToBstHelper(po, pos + 1, pos + count,
                                     io, ios, rootIdx - 1)

        root.right = arrayToBstHelper(po, pos + count + 1, poe,
                                      io, rootIdx + 1, ioe)

        return root
    }
    return arrayToBstHelper(preorder, 0, preorder.length-1, inorder, 0, inorder.length - 1)
}
