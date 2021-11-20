
class Node:
    child_node_list = []
    optr = None

    def __init__(self,optr,sub_node_list: list):
        self.optr = optr
        self.child_node_list = sub_node_list

    def __str__(self):
        msg:str = "<node optr='"+self.optr+"'>"
        for node in self.child_node_list:
            msg = msg + "\n" + str(node)
        msg = msg + "\n</node>"
        return msg


class Leaf(Node):
    type = ''
    val = None

    def __init__(self,type,val):
        super(Leaf, self).__init__('',[])
        self.type = type
        self.val = val

    def __str__(self):
        return "<leaf val='"+str(self.val)+"' type='"+str(self.type)+"'/>"


class CallStackTree:
    def onCallStart(self):
        pass

    def onCallEnd(self):
        pass


class TreeOptimizer:
    def DeleteNone(self, root: Node):
        for node in root.child_node_list:
            if type(node) == Leaf and node.type=='none':
                root.child_node_list.remove(node)
        for node in root.child_node_list:
            self.DeleteNone(node)

    def PromotionNodes(self,root: Node):
        is_clean = False
        while not is_clean:
            is_clean = True
            for node in root.child_node_list:
                if not type(node) == Leaf and node.optr=='append':
                    is_clean = False
                    for node2 in node.child_node_list:
                        root.child_node_list.append(node2)
                    root.child_node_list.remove(node)
        for node in root.child_node_list:
            self.PromotionNodes(node)

