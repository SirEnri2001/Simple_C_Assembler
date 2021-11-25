import re

from ply import yacc
from lex import tokens
from utils import *

start = 'Program'

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UPLUS','UMINUS')
)

def p_empty(p):
    '''EMPTY : '''
    p[0] = Leaf("none", '')

def p_relop(p):
    '''RELOP : '>'
    | '<'
    | GRTREQL
    | LESSEQL
    | EQUAL
    | NEQUAL '''
    p[0] = p[1]

def p_type(p):
    '''TYPE : INT
	| FLOAT '''
    p[0] = TypeLeaf.getType(p[1])

def p_Program(p):
    '''Program : ExtDefList '''
    print("Compiler Start")
    p[0] = ProgramNode('ExtDefList', [p[1]])


def p_ExtDefList(p):
    '''ExtDefList : ExtDef ExtDefList
	| EMPTY'''
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 3:
        p[0] = Node(optr="append", sub_node_list=[p[1], p[2]])


def p_FunHead(p):
    '''FunHead : Specifier FunDec'''
    p[0] = FunDefNode('funhead_def', [p[1], p[2]])


def p_ExtDecHead(p):
    '''ExtDecHead : Specifier VarDec'''
    p[0] = ExtNode('extdec', [p[1], p[2]])


def p_ExtDecHead_Fun(p):
    '''ExtDecHead : Specifier FunDec'''
    p[0] = ExtNode('extdec_fun', [p[1], p[2]])


def p_ExtDecList(p):
    '''ExtDecList : ExtDecList ',' VarDec
        | ExtDecHead'''
    if len(p) == 4:
        p[0] = ExtNode('extdec', [p[1].child_node_list[0], p[1], p[3]])
    else:
        p[0] = p[1]


def p_ExtDecList_Fun(p):
    '''ExtDecList : ExtDecList ',' FunDec'''
    p[0] = ExtNode('extdec_fun', [p[1].child_node_list[0], p[1], p[3]])


def p_ExtDef_ExtDecList(p):
    '''ExtDef : ExtDecList ';' '''
    p[0] = p[1]


def p_ExtDef_Specifier(p):
    '''ExtDef : Specifier ';' '''
    p[0] = Node(optr="specifier_dec", sub_node_list=[p[1]])


def p_ExtDef_FunDef(p):
    '''ExtDef : FunHead CompSt '''
    p[0] = ExtNode(optr="extdef_func", sub_node_list=[p[1], p[2]])


def p_Specifier(p):
    '''Specifier : TYPE
	| StructSpecifier '''
    p[0] = p[1]


def p_StructSpecifier(p):
    '''StructSpecifier : STRUCT OptTag '{' DefList '}'
	| STRUCT Tag '''
    if len(p) == 3:
        p[0] = Node('struct', [p[2]])
    elif len(p) == 6:
        p[0] = Node('struct', [p[2], p[4]])


def p_OptTag(p):
    '''OptTag : ID
	| EMPTY'''
    p[0] = Leaf('OptTag', p[1])


def p_Tag(p):
    '''Tag : ID'''
    p[0] = Leaf('Tag', p[1])


def p_VarDec(p):
    '''VarDec : ID
	| VarDec '[' NUMBER ']' '''
    if len(p) == 2:
        p[0] = Leaf("ID", p[1])
    elif len(p) == 5:
        p[0] = Node('array_dec', [p[1], Leaf('NUMBER', p[3])])


def p_FunDec(p):
    '''FunDec : ID '(' VarList ')'
	| ID '(' ')' '''
    if len(p) == 5:
        p[0] = Node('func_dec', [Leaf('ID', p[1]), p[3]])
    elif len(p) == 4:
        p[0] = Node('func_dec', [Leaf('ID', p[1])])


def p_VarList(p):
    '''VarList : ParamDec ',' VarList
	| ParamDec '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = Node('append', [p[1], p[3]])


def p_ParamDec(p):
    '''ParamDec : Specifier VarDec '''
    p[0] = LocalDecNode("param_dec", [p[1], p[2]])


def p_CompSt(p):
    '''CompSt : '{' DefList StmtList '}' '''
    p[0] = CompStmtNode('compst', [p[2], p[3]])


def p_StmtList(p):
    '''StmtList : Stmt StmtList
	| EMPTY'''
    if len(p) == 3:
        p[0] = Node('append', [p[1], p[2]])
    if len(p) == 2:
        p[0] = p[1]


def p_Stmt_return(p):
    '''Stmt : RETURN Exp ';' '''
    p[0] = StmtNode('return', [p[2]])

def p_Stmt_print(p):
    '''Stmt : PRINT Exp ';' '''
    p[0] = StmtNode('print',[p[2]])

def p_FlowCtrl(p):
    '''FlowCtrl : IF '(' Exp ')' Stmt
	| IF '(' Exp ')' Stmt ELSE Stmt
	| WHILE '(' Exp ')' Stmt'''
    if p[1] == "if":
        if len(p) == 6:
            p[0] = FlowCtrlNode('if', [p[3], p[5]])
        elif len(p) == 8:
            p[0] = FlowCtrlNode('if_else', [p[3], p[5], p[7]])
    elif p[1] == 'while':
        p[0] = FlowCtrlNode('while', [p[3], p[5]])


def p_Stmt(p):
    '''Stmt : Exp ';'
	| CompSt
	| ';'
	| FlowCtrl'''
    p[0] = p[1]

def p_DefList(p):
    '''DefList : Def ';' DefList
	| EMPTY'''
    if len(p) == 4:
        p[0] = Node('append', [p[1], p[3]])
    elif len(p) == 2:
        p[0] = p[1]


def p_Def(p):
    '''Def : DecList'''
    p[0] = p[1]


def p_DecHead(p):
    '''DecHead : Specifier Dec'''
    p[0] = LocalDecNode('dec', [p[1], p[2]])


def p_DecList(p):
    '''DecList : DecHead
     | DecList ',' Dec'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = LocalDecNode('dec', [p[1].child_node_list[0], p[1], p[3]])


def p_Dec(p):
    '''Dec : VarDec
	| VarDec '=' Exp'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('init_assign', [p[1], p[3]])


def p_PrefixedExp_Mem(p):
    '''PrefixedExp : '*' Exp
    | '&' Exp'''
    p[0] = MemNode(p[1], [p[2]])

def p_PrefixedExp(p):
    '''PrefixedExp : '-' Exp %prec UMINUS
    	| '+' Exp %prec UPLUS
    	| PLUSSLF Exp
    	| SUBSLF Exp
    	| '(' TYPE ')' Exp'''
    if len(p) == 3:
        p[0] = PrefixCalcNode(p[1], [p[2]])
    else:
        p[0] = PrefixCalcNode('force_convert', [p[2]])


def p_Exp_par(p):
    '''Exp : '(' Exp ')' '''
    p[0] = p[2]


def p_Exp_Id(p):
    '''Exp : ID'''
    p[0] = IdLeaf(p[1])

def p_Exp_Number(p):
    '''Exp : NUMBER'''
    p[0] = Leaf('NUM', p[1])


def p_Exp_Constant(p):
    '''Exp : DECIMAL
	| STRINGLITERAL'''
    node = Leaf('CONST', p[1])
    p[0] = node


def p_Exp(p):
    '''Exp : Exp '=' Exp
	| Exp '+' Exp
	| Exp '-' Exp
	| Exp '*' Exp
	| Exp '/' Exp
	| FuncCall
	| PrefixedExp'''
    if len(p) == 4:
        p[0] = CalcNode(p[2], [p[1], p[3]])
    else:
        p[0] = p[1]

def p_Exp_Logic(p):
    '''Exp : Exp BOOLAND Exp
    	| Exp BOOLOR Exp
    	| '!' Exp'''
    if len(p) == 4:
        p[0] = LogicNode(p[2], [p[1], p[3]])
    else:
        p[0] = p[2]

def p_Exp_Relop(p):
    '''Exp : Exp RELOP Exp'''
    p[0] = RelopCalcNode(p[2], [p[1], p[3]])


def p_Exp_Mem(p):
    '''Exp : Exp '[' Exp ']'
	| Exp '.' ID'''
    if len(p) == 5:
        p[0] = MemNode('array_subfix', [p[1], p[3]])
    elif len(p) == 4:
        p[0] = MemNode('get_field', [p[1], p[3]])


def p_FuncCall(p):
    '''FuncCall : ID '(' Args ')'
	| ID '(' ')' '''
    if len(p) == 5:
        p[0] = Node('call', [Leaf('ID', p[1]), p[3]])
    elif len(p) == 4:
        p[0] = Node('call', [Leaf('ID', p[1])])


def p_Args(p):
    '''Args : Exp ',' Args
	| Exp'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = Node('', [p[1], p[3]])


# Error rule for syntax errors
def p_error(p):
    print(p)
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
s = '''
/* Here is my programme
 * Author : hanxinghua
 *
 */
 int func1(int i,int j){
    int a,b,c,d;
    return a*-b+c*d;
 }
 
int main(){
    int a = 1, b = 2,c=3;
    while(a<b){
        c = c + 3;
    }
    print(c);
    return 0;
}
'''
node = parser.parse(s)
storage_unit = StorageUnit(None)
optimizer = TreeOptimizer()
optimizer.DeleteNone(node)
optimizer.PromotionNodes(node)
optimizer.PromotionNodesSpecified(node, ["extdec", "extdec_fun"])
optimizer.PromotionNodesSpecified(node, ["dec"])
print(node)

node.start_program(storage_unit)
for code in node.generate_fakeCode():
    if re.match(".*[.:].*",code):
        print(code)
    else:
        print('\t'+code)
