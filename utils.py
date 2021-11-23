import traceback

from Program import *

t_seq = 1
l_seq = 1

code_integrate = []

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
        self.nodeType = "Generic"
        self.fakeCode = []
        self.fakeCode_post = []
        self.targetCode = []
        self.targetCode_post = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
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

    def get_fakeCode(self) -> list:
        return self.fakeCode

    def generate_fakeCode(self):
        global code_integrate
        fakeCode = self.get_fakeCode()
        if fakeCode is not None:
            code_integrate.extend(fakeCode)
        for node in self.child_node_list:
            node.generate_fakeCode()
        fakeCode = self.get_fakeCode_post()
        if fakeCode is not None:
            code_integrate.extend(fakeCode)
        return code_integrate

    def get_fakeCode_post(self) -> list:
        return self.fakeCode_post

    def get_targetCode(self) -> list:
        return self.targetCode

    def generate_targetCode(self):
        global code_integrate
        targetCode = self.get_fakeCode()
        if targetCode is not None:
            code_integrate.extend(targetCode)
        for node in self.child_node_list:
            node.generate_fakeCode()
        targetCode = self.get_fakeCode_post()
        if targetCode is not None:
            code_integrate.extend(targetCode)
        return code_integrate

    def get_targetCode_post(self) -> list:
        return self.targetCode_post

class ProgramNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "Program"

    def set_program(self):
        pass

    def get_fakeCode(self):
        for node in self.child_node_list:
            pass
        return self.fakeCode


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

    def get_fakeCode(self) -> list:
        if self.optr == 'extdec':
            self.fakeCode.append('.globl ' + self.child_node_list[0].id.val)
        if self.optr == 'extdef_func':
            self.fakeCode.append('.globl ' + self.child_node_list[0].id.val)
        return self.fakeCode


class CalcNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "Calc"

    def set_program(self):
        global t_seq
        self.val = 'T' + str(t_seq)
        t_seq = t_seq+1

    def get_fakeCode_post(self) -> list:
        post = []
        self.type = self.child_node_list[0].type  # Simple implicit type convert
        try:
            post.append(
                "{} = {} {} {}".format(self.val, self.child_node_list[0].val, self.optr, self.child_node_list[1].val))
            '''if self.optr in ['+', '-', '*']:
                self.fakeCode.append("{}{} {},{}".format(
                    instruction_table[self.optr], instr_suffix[self.child_node_list[0].type],
                    self.child_node_list[0].val, self.child_node_list[1].val
                ))'''
        except KeyError as e:
            print("Compiler Error: Key Error in Calc\n\toptr: {}, type: {}".format(
                self.optr, self.child_node_list[0].type
            ))
        post.extend(self.fakeCode_post)
        self.fakeCode_post = post
        return self.fakeCode_post


class RelopCalcNode(CalcNode):
    pass


class LogicNode(CalcNode):
    pass


prefix_instruction_table = {
    '-': 'neg'
}

conditional_jmp_table = {
    '==': 'je',
    '!=': 'jne',
    '>': 'jg',
    '>=': 'jge',
    '<': 'jl',
    '<=': 'jle'
}


class PrefixCalcNode(CalcNode):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "PrefixCalc"

    def get_fakeCode(self):
        self.type = self.child_node_list[0].type  # Simple implicit type convert
        if self.optr == '=':
            self.fakeCode.append("{}{} {}".format(
                prefix_instruction_table[self.optr], instr_suffix[self.child_node_list[0].type],
                self.child_node_list[0].val
            ))
        return self.fakeCode


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

    def get_fakeCode(self):
        self.fakeCode.append("{}:".format(self.child_node_list[1].child_node_list[0].val))
        return self.fakeCode


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

    def get_fakeCode(self):
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


class StmtNode(Node):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "Stmt"

    def set_program(self):
        pass

    def get_fakeCode_post(self):
        post = []
        if self.optr == 'return':
            if self.child_node_list[0] is not None:
                post.append('retVal = {}'.format(self.child_node_list[0].val))
            post.append('ret')
        post.extend(self.fakeCode_post)
        self.fakeCode_post = post
        return self.fakeCode_post


class FlowCtrlNode(StmtNode):
    def __init__(self, optr, sub_node_list: list):
        super().__init__(optr, sub_node_list)
        self.nodeType = "FlowCtrl"

    def set_program(self):
        pass

    def get_fakeCode(self):
        global l_seq
        if self.optr=='if':
            label = "L{}".format(l_seq)
            l_seq = l_seq+1
            self.child_node_list[1].fakeCode.append("cmp {},0".format(self.child_node_list[0].val))
            self.child_node_list[1].fakeCode.append("je {}".format(label))
            self.fakeCode_post.append("{}:".format(label))
        if self.optr=='if_else':
            label1 = "L{}".format(l_seq)
            label2 = "L{}".format(l_seq+1)
            l_seq = l_seq + 2
            self.child_node_list[1].fakeCode.append("cmp {},0".format(self.child_node_list[0].val))
            self.child_node_list[1].fakeCode.append("je {}".format(label1))
            self.child_node_list[2].fakeCode.append("jmp {}".format(label2))
            self.child_node_list[2].fakeCode.append("{}:".format(label1))
            self.fakeCode_post.append("{}:".format(label2))
        if self.optr=='while':
            label1 = "L{}".format(l_seq)
            label2 = "L{}".format(l_seq + 1)
            l_seq = l_seq + 2
            self.child_node_list[1].fakeCode.append("{}:".format(label1))
            self.child_node_list[1].fakeCode.append("cmp {},0".format(self.child_node_list[0].val))
            self.child_node_list[1].fakeCode.append("je {}".format(label2))
            self.fakeCode_post.append("jmp {}".format(label1))
            self.fakeCode_post.append("{}:".format(label2))
        return self.fakeCode

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
        self.name = val
        self.field = None

    def set_program(self):
        self.field = self.storage_unit.get(self.name)
        self.type = self.field.type


declared_type = {}

size_table = {
    'int': 8,
    'float': 8,
    'double': 8,
    'pointer': 8
}

instr_suffix = {
    'int': 'l'
}

instruction_table = {
    '=': 'mov',
    '+': 'add',
    '-': 'sub',
    '*': 'imul',
    '/': 'idiv'
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
    def getType(cls, val):
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
