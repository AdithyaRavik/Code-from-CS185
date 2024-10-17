from TreeNodeBST import TreeNode
from TreeNodeBST import BinarySearchTree
from queueDS import Queue

def sort(alist):
    a = BinarySearchTree()
    for i in alist:
        a[i] = str(i)
    recurse(a.root)

def recurse(root):
    if root is not None:
        recurse(root.left_child)
        print(str(root.key))
        recurse(root.right_child)
# Our initial for loop in 'sort' takes O(n) to populate our tree. However,our
# recursive method takes longer, as it runs item in our list --> since we know the
# height = log n, and it runs for every entry (n entries), we have a time of n logn
#or n height.

def inRange(treeNode, lo, hi):
    if treeNode is not None:
        inRange(treeNode.left_child,lo, hi)
        if treeNode.key < hi and treeNode.key > lo:
            print(treeNode.key)
        inRange(treeNode.right_child,lo, hi)

def levelOrderTraversal(treeNode):
    depth = -1
    tree = Queue()
    tree.enqueue([treeNode])
    while(tree.size()!= 0 ):
        depth += 1
        nodes = tree.dequeue()
        temp = []
        print(str(depth)+ ':' , end = '\n')
        for i in nodes:
            print(str(i), end = '\n')
            if i.left_child != None:
                temp.append(i.left_child)
            if i.right_child != None:
                temp.append(right_child)
        tree.enqueue(temp)
        print()
def levelOrder_tester():
    c = BinarySearchTree()
    alist = [40,30,80,27,100]
    for i in alist:
        c[i] = str(i)
    levelOrderTraversal(c[2])
#levelOrder_tester()
def inRange_tester():
    a = BinarySearchTree()
    alist = [40,30,80,27,100]
    for i in alist:
        a[i] = str(i)
inRange(a.root,70,100) #Expected: 80
inRange(a.root,30,80) # Expected: 40
inRange(a.root,0,90) #Expected: 27 30 40 80
inRange(a.root,40,80) #Expected: blank
#inRange_tester()
def sort_tester():
    alist = [40,30,80,27,100]
    sort(alist)
#sort_tester()

def twoChild(TreeNode):
    if TreeNode is None:
        return 0

    if TreeNode.right_child and TreeNode.left_child:
        return 1+ twoChild(TreeNode.right_child) + twoChild(TreeNode.left_child)

    return twoChild(TreeNode.right_child)+ twoChild(TreeNode.left_child)



