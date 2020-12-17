class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self,root:TreeNode)->TreeNode:
        if root:
            # 保存一开始的左子树
            tmp = root.left
            root.left = self.mirrorTree(root.right)
            root.right = self.mirrorTree(tmp)
            return root
        return None

class BuildTree:
    def __init__(self, x):
        self.preIndex = x
        self.tree=[]
    def find(self,inOrder:list,begain:int,end:int,val:int):
        for i in range(begain,end+1):
            if inOrder[i]==val:
                return i
        return -1
    def BuildTreeWithPreAndInOrder(self,preOrder:list,inOrder:list,begain:int,end:int)->TreeNode:
        if begain>end:
            return None
        root = TreeNode(preOrder[self.preIndex])
        nodeIndex = self.find(inOrder,begain,end,preOrder[self.preIndex])
        # print('begain:'+str(begain)+'end:'+str(end))
        # print("pre: " + str(preOrder[self.preIndex]))
        # print("nodeIndex: " + str(nodeIndex))
        if nodeIndex == -1:
            return None
        self.preIndex+=1
        root.left = self.BuildTreeWithPreAndInOrder(preOrder,inOrder,begain,nodeIndex-1)
        root.right = self.BuildTreeWithPreAndInOrder(preOrder,inOrder,nodeIndex+1,end)
        return root
    def PreTraversalTree(self,root:TreeNode):
        if root:
            self.tree.append(root.val)
            self.PreTraversalTree(root.left)
            self.PreTraversalTree(root.right)
    def InTraversalTree(self,root:TreeNode):
        if root:
            self.InTraversalTree(root.left)
            self.tree.append(root.val)
            self.InTraversalTree(root.right)
    def PrintTree(self,root:TreeNode):
        self.PreTraversalTree(root)
        print(self.tree)
        self.tree=[]
        self.InTraversalTree(root)
        print(self.tree)

if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    b=BuildTree(0)
    root = b.BuildTreeWithPreAndInOrder(preorder,inorder,0,len(inorder)-1)
    print('Before the tree is :')
    b.PrintTree(root)
    b.tree=[]
    print('After the tree is :')
    s=Solution()
    afterroot=s.mirrorTree(root)
    b.PrintTree(afterroot)
