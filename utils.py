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
    _fakeCode = []

    def __init__(self, optr, sub_node_list: list):
        super(Node, self).__init__(sub_node_list)
        self.optr = optr
        self.nodeType = "Generic"
        self._fakeCode = []

    def __repr__(self):
        msg: str = "<" + self.nodeType + " optr='" + self.optr + "'>"
        for node in self.child_node_list:
            msg = msg + "\n" + str(node)
        msg = msg + "\n</" + self.nodeType + ">"
        return msg

    def set_program(self):
        pass

    def start_program(self, su: StorageUnit):
        self.storage_unit = su
        self.set_program()
        for node in self.child_node_list:
            node.start_program(self.storage_unit)

    def set_fakeCode(self):
        pass

    def generate_fakeCode(self):
        self.set_fakeCode()
        print(self._fakeCode)
        for node in self.child_node_list:
            node.generate_fakeCode()


class ExtNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "Ext"
        self.type_leaf = None
        self.id_leaf = None

    def set_program(self):
        if self.optr == 'extdec':
            self.type_leaf = self.child_node_list[0]
            self.id_leaf = self.child_node_list[1]
            self.storage_unit.add_static(self.id_leaf.val, self.type_leaf.val, self.type_leaf.size)
        if self.optr == 'extdef_func':
            new_su = StorageUnit(self.storage_unit)
            self.storage_unit = new_su
            self.id_leaf = self.child_node_list[0].id
            print(self.child_node_list)

    def set_fakeCode(self):
        if self.optr == 'extdec':
            return
        if self.optr == 'extdef_func':
            self._fakeCode.append('_globl '+self.id_leaf.val)


class CalcNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "Calc"
        self._asm = ""

    def set_program(self):
        self.val = 'T' + str(t_seq)

    def set_fakeCode(self):
        self.type = self.child_node_list[0].type # Simple implicit type convert
        if self.optr=='=':
            self._fakeCode.append("{}{} {},{}".format(
                instruction_table[self.optr],instr_suffix[self.child_node_list[0].type],
                self.child_node_list[0].val,self.child_node_list[1].val
            ))


class PrefixCalcNode(CalcNode):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "PrefixCalc"

    def set_program(self):
        self.val = 'T'+str(t_seq)


class MemNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "MemNode"

    def set_program(self):
        pass


class FunDefNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "FunDef"
        self.retType = None
        self.id = None

    def set_program(self):
        self.retType = self.child_node_list[0]
        self.id = self.child_node_list[1].child_node_list[0]
        print(self.id)


class LocalDecNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "LocalDec"
        self.initVal = None

    def set_program(self):
        type_leaf = self.child_node_list[0]
        id_leaf = self.child_node_list[1]
        if id_leaf.optr is not None and id_leaf.optr == 'init_assign':
            self.init_val = id_leaf.child_node_list[1]
            id_leaf = id_leaf.child_node_list[0]
        self.storage_unit.add_local(id=id_leaf.val, type=type_leaf.val, size=type_leaf.size)

    def get_fakecode(self):
        pass


class FunDecNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "FunDec"



class CompStmtNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "CompStmt"

    def set_program(self):
        new_su = StorageUnit(self.storage_unit)
        self.storage_unit = new_su


class Leaf(Node):
    def __init__(self, type, val):
        super(Leaf, self).__init__('', [])
        self.nodeType = type
        self.val = val

    def __str__(self):
        return "<" + str(self.nodeType) + " val='" + str(self.val) + "'/>"


class IdLeaf(Leaf):
    def __init__(self, val):
        super().__init__("Identifier", val)

    def set_program(self):
        pass

declared_type = {}

size_table = {
    'int': 8,
    'float' : 8,
    'double' : 8,
    'pointer' : 8
}

instr_suffix = {
    'int':'l'
}

instruction_table = {
    '=':'mov',
    '+':'add',
    '-':'sub',
    '*':'imul',
    '/':'idiv'
}

class TypeLeaf(Leaf):
    size: int

    def __init__(self, val):
        super().__init__("Type", val)
        global declared_type
        self.size = size_table[val]
        declared_type[val] = self

    def set_program(self):
        pass

    @classmethod
    def getType(cls,val):
        global declared_type
        try:
            typeObj = declared_type[val]
        except KeyError:
            typeObj = TypeLeaf(val)
            declared_type[val] = typeObj
        return typeObj


class TreeOptimizer:
    def DeleteNone(self, root: Node):
        for node in root.child_node_list:
            if type(node) == Leaf and node.nodeType == 'none':
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
