from bintree import binnode

class Binst(binnode):
     
    def search(self, nodevalue):
      current_node = self
      previous_node = self
      while(current_node): 
        if nodevalue == current_node.value:
            break
        elif nodevalue< current_node.value:
            previous_node = current_node
            current_node = current_node.lchild
        else:
            previous_node = current_node
            current_node = current_node.rchild
      if current_node:
          return (True, current_node)
      else:
          return (False, previous_node)
          
    def insert(self, value):
        binst = Binst(value)
        location = self.search(binst.value)
        if location[0]:
            return "there already exists one same value"
        else:
            insert_location =  location[1]
            
            if insert_location.value< binst.value:
                insert_location.rchild = binst
                binst.parent = insert_location
            else:
                insert_location.lchild = binst
                binst.parent = insert_location

            insert_location.updateheightabove()
        

    def change_parent(self, old_binnode, new_binnode ):
        if old_binnode.parent:
         if new_binnode:
           new_binnode.parent = old_binnode.parent
         if old_binnode.parent.value > old_binnode.value:
             old_binnode.parent.lchild = new_binnode
         else:
             old_binnode.parent.rchild = new_binnode
        else:
         pass
    
    def find_leftmostchild(self, binnode):
        current_node  = binnode
        while(current_node):
            current_node = current_node.lchild

    def remove(self, binnode_value):
        # 这里remove完了以后没有做高度更新很显然是不对劲的。。
        result  =  self.search(binnode_value)
        if  result[0]:
            deleted_node = result[1]
            update_node = deleted_node.parent
            if  not  (deleted_node.rchild):
                self.change_parent(deleted_node, deleted_node.lchild)
            elif  not (deleted_node.lchild):
                self.change_parent(deleted_node, deleted_node.rchild)
            else:
                new_node = self.find_leftmostchild(deleted_node.rchild).value
                deleted_node.value =new_node.value
                self.change_parent(new_node,new_node.rchild)
            if update_node:
                update_node.updateheightabove()
            if not self.avlbalanced():
                self.three_plus_four([update_node,update_node.child(), update_node.child().child()],subtrees)
        else:
            new_node = self.find_leftmostchild(deleted_node.rchild)
            return 'there exist no node to be deleted'
    #首先你要搞清楚为啥会失衡，因为插入和删除操作确实导致节点高度的变化从个人导致整个avl数不再满足左右高度最多只相差1，但是由于每次插入和删除操作都是基于叶子节点才来的，所以
    #如果是插入，插在none-type上面一旦发生了失衡也一定不是发生在父亲节点，而是祖父节点。。这就是为啥如果发生了失衡，一定会存在祖孙三代节点的原因。
    #然后3+4的算法实在解释说，如果我想让树结构是重新平衡一定会要找一个左右平衡的，同时还要满足中序遍历，所以就有了3+4 （祖孙三代提出来重新拍成父子结构，然后4棵子树为了满足中序遍历结果重新排序）

    def avlbalanced(self):
        current_node = self
        if binnodebalanced(current_node):
           answer  =   current_node.rchild.avlbalanced() and  current_node.lchild.avlbalanced()
        else:
           return False
        return answer


    def three_plus_four(self,nodes, subtrees):
      for i in range(len(nodes) -1):
        for j in range(len(nodes) - i):
            if nodes[j].value > nodes[j+1].value:
                midd = nodes[j+1]
                nodes[j+1] = nodes[j]
                nodes[j] = midd
      for i in range(len(subtrees) -1):
        for j in range(len(subtrees) - i):
           
            if nodes[j].value > nodes[j+1].value:
                midd = nodes[j+1]
                nodes[j+1] = nodes[j]
                nodes[j] = midd     
      nodes[1].lchild = nodes[0]
      nodes[1].rchild = nodes[2]
      for i in range(len(subtrees)):
         if subtrees[i]:
             continue
         else:
             if subtrees[i].value> nodes[1].value:
                 if subtrees[i].value > nodes[2].value:
                     nodes[2].value.rchild = subtrees[i]
                     subtrees[i].parent = nodes[2]
                 else:
                     nodes[2].value.lchild = subtrees[i]
                     subtrees[i].parent = nodes[2]    
             else:
                 if subtrees[i].value > nodes[0].value:
                     nodes[0].value.rchild = subtrees[i]
                     subtrees[i].parent = nodes[0]
                 else:
                     nodes[0].value.lchild = subtrees[i]
                     subtrees[i].parent = nodes[0]   
    #  注意其实subtree也要满足中序遍历的法则而且只有4个位置可以放置，这个问题想清楚了就很简单了
    
def binnodebalanced(binnode):
        if -2 < status(binnode.lchild) - status(binnode.rchild) <2 :
            return True
        else:
            return False
def status(binnode):
    if binnode:
        return binnode.height
    else:
        return -1
if __name__ == "__main__":
    binnode = Binst(3) 
    binnode.middletraverse()
    print(binnode.insert(2))
    print('insert',status(binnode))
    binnode.middletraverse()
    binnode.remove(2)
    binnode.middletraverse()
    print('remove',status(binnode))
