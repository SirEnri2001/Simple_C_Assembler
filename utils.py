from Program import *

t_seq = 1


class BaseNode:
    child_node_list = []
    val = None

    def __init__(self, sub_node_list: list):
        self.child_node_list = sub_node_list

    def __str__(self):
        msg: str = "<node" + ">"
        for node in self.child_node_list:
            msg = msg + "\n" + str(node)
        msg = msg + "\n</node>"
        return msg


class ProcessNode(BaseNode):
    pass


class Node(BaseNode):
    optr = None
    type = ""
    storage_unit: StorageUnit

    def __init__(self, optr, sub_node_list: list):
        super(Node, self).__init__(sub_node_list)
        self.optr = optr
        self.type = "Generic"

    def __str__(self):
        msg: str = "<" + self.type + " optr='" + self.optr + "'>"
        for node in self.child_node_list:
            msg = msg + "\n" + str(node)
        msg = msg + "\n</" + self.type + ">"
        return msg

    def set_program(self):
        pass

    def start_program(self, su: StorageUnit):
        self.storage_unit = su
        self.set_program()
        for node in self.child_node_list:
            node.start_program(self.storage_unit)


class ExtNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "Ext"

    def set_program(self):
        if self.optr == 'extdec':
            type_leaf = self.child_node_list[0]
            id_leaf = self.child_node_list[1]
            self.storage_unit.add_static(id_leaf.val, type_leaf.val, type_leaf.size)
        if self.optr == 'extdef_func':
            new_su = StorageUnit(self.storage_unit)
            self.storage_unit = new_su


class CalcNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "Calc"
        self._asm = ""

    def set_program(self):
        pass
        #self._asm = self.optr + ' ' + self.child_node_list[0].val + ',' + self.child_node_list[1].val



class PrefixCalcNode(CalcNode):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "PrefixCalc"

    def set_program(self):
        pass


class MemNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "MemNode"

    def set_program(self):
        pass


class FunDefNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "FunDef"

    def set_program(self):
        pass


class LocalDecNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "LocalDec"

    def set_program(self):
        type_leaf = self.child_node_list[0]
        id_leaf = self.child_node_list[1]
        init_val = None
        if id_leaf.optr is not None and id_leaf.optr == 'init_assign':
            init_val = id_leaf.child_node_list[1]
            id_leaf = id_leaf.child_node_list[0]
        self.storage_unit.add_local(id=id_leaf.val, type=type_leaf.val, size=type_leaf.size)
        self._asm = 'movl'


class CompStmtNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.type = "CompStmt"

    def set_program(self):
        new_su = StorageUnit(self.storage_unit)
        self.storage_unit = new_su


class Leaf(Node):
    def __init__(self, type, val):
        super(Leaf, self).__init__('', [])
        self.type = type
        self.val = val

    def __str__(self):
        return "<" + str(self.type) + " val='" + str(self.val) + "'/>"


class IdLeaf(Leaf):
    def __init__(self, val):
        super().__init__("Identifier", val)

    def set_program(self):
        pass


class TypeLeaf(Leaf):
    size: int

    def __init__(self, val, size: int):
        super().__init__("Type", val)
        self.size = size

    def set_program(self):
        pass


class TreeOptimizer:
    def DeleteNone(self, root: Node):
        for node in root.child_node_list:
            if type(node) == Leaf and node.type == 'none':
                root.child_node_list.remove(node)
        for node in root.child_node_list:
            self.DeleteNone(node)

    def PromotionNodes(self, root: Node):
        is_clean = False
        while not is_clean:
            is_clean = True
            for node in root.child_node_list:
                if not type(node) == Leaf and node.optr == 'append':
                    is_clean = False
                    for node2 in node.child_node_list:
                        root.child_node_list.append(node2)
                    root.child_node_list.remove(node)
        for node in root.child_node_list:
            self.PromotionNodes(node)

    def PromotionNodesSpecified(self, root: Node, spec: list):
        is_clean = False
        while not is_clean:
            is_clean = True
            for node in root.child_node_list:
                if not type(node) == Leaf and node.optr in spec:
                    for node2 in node.child_node_list:
                        if not type(node2) == Leaf and node2.optr in spec:
                            root.child_node_list.insert(root.child_node_list.index(node), node2)
                            node.child_node_list.remove(node2)
                            is_clean = False
                            break
        for node in root.child_node_list:
            self.PromotionNodesSpecified(node, spec)
