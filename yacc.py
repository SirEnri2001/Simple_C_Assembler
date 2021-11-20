from ply import yacc
from lex import tokens
from utils import *

start = 'Program'


def p_empty(p):
    '''EMPTY : '''
    p[0] = Leaf("none",'')


def p_semi(p):
    '''SEMI : ';' '''
    p[0] = p[1]


def p_comma(p):
    '''COMMA : ',' '''
    p[0] = p[1]


def p_assignop(p):
    '''ASSIGNOP : '=' '''
    p[0] = p[1]


def p_relop(p):
    '''RELOP : '>'
    | '<'
    | GRTREQL
    | LESSEQL
    | EQUAL
    | NEQUAL '''
    p[0] = p[1]


def p_plus(p):
    '''PLUS : '+' '''
    p[0] = p[1]


def p_minus(p):
    '''MINUS : '-' '''
    p[0] = p[1]


def p_star(p):
    '''STAR : '*' '''
    p[0] = p[1]


def p_div(p):
    '''DIV : '/' '''
    p[0] = p[1]


def p_and(p):
    '''AND : BOOLAND '''
    p[0] = p[1]


def p_or(p):
    '''OR : BOOLOR '''
    p[0] = p[1]


def p_dot(p):
    '''DOT : '.' '''
    p[0] = p[1]


def p_not(p):
    '''NOT : '!' '''
    p[0] = p[1]


def p_type(p):
    '''TYPE : INT
	| FLOAT '''
    p[0] = Leaf("type_specifier",p[1])


def p_lp(p):
    '''LP : '(' '''
    pass


def p_rp(p):
    '''RP : ')' '''
    pass


def p_lb(p):
    '''LB : '[' '''
    pass


def p_rb(p):
    '''RB : ']' '''
    pass


def p_lc(p):
    '''LC : '{' '''
    pass


def p_rc(p):
    '''RC : '}' '''
    pass


def p_Program(p):
    '''Program : ExtDefList '''
    print("Compiler Start")
    p[0] = Node('ExtDefList',[p[1]])


def p_ExtDefList(p):
    '''ExtDefList : ExtDef ExtDefList
	| EMPTY'''
    if len(p)==2:
        p[0] = p[1]
    if len(p)==3:
        p[0] = Node(optr="append", sub_node_list=[p[1], p[2]])

def p_FunHead(p):
    '''FunHead : Specifier FunDec'''
    p[0] = Node('funhead_def',[p[1],p[2]])

def p_ExtDef_ExtDecList(p):
    '''ExtDef : Specifier ExtDecList SEMI'''
    p[0] = Node(optr="ext_dec",sub_node_list=[p[1],p[2]])


def p_ExtDef_Specifier(p):
    '''ExtDef : Specifier SEMI'''
    p[0] = Node(optr="specifier_dec", sub_node_list=[p[1]])

def p_ExtDef_FunDef(p):
    '''ExtDef : FunHead CompSt '''
    p[0] = Node(optr="ext_func_def", sub_node_list=[p[1], p[2]])

def p_ExtDecList(p):
    '''ExtDecList : VarDec
	| VarDec COMMA ExtDecList
	| FunDec
	| FunDec COMMA ExtDecList'''
    if len(p)==4:
        p[0] = Node(optr="append",sub_node_list=[p[1],p[3]])
    elif len(p)==2:
        p[0] = p[1]


def p_Specifier(p):
    '''Specifier : TYPE
	| StructSpecifier '''
    p[0] = p[1]


def p_StructSpecifier(p):
    '''StructSpecifier : STRUCT OptTag LC DefList RC
	| STRUCT Tag '''
    if len(p)==3:
        p[0] = Node('struct',[p[2]])
    elif len(p)==6:
        p[0] = Node('struct',[p[2],p[4]])


def p_OptTag(p):
    '''OptTag : ID
	| EMPTY'''
    p[0] = Leaf('OptTag',p[1])


def p_Tag(p):
    '''Tag : ID'''
    p[0] = Leaf('Tag',p[1])


def p_VarDec(p):
    '''VarDec : ID
	| VarDec LB NUMBER RB '''
    if len(p)==2:
        p[0]=Leaf("ID",p[1])
    elif len(p)==5:
        p[0] = Node('array_dec',[p[1], Leaf('NUMBER', p[3])])


def p_FunDec(p):
    '''FunDec : ID LP VarList RP
	| ID LP RP '''
    if len(p) == 5:
        p[0] = Node('func_dec',[Leaf('ID',p[1]),p[3]])
    elif len(p)==4:
        p[0] = Node('func_dec',[Leaf('ID',p[1])])


def p_VarList(p):
    '''VarList : ParamDec COMMA VarList
	| ParamDec '''
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==4:
        p[0] = Node('append',[p[1],p[3]])


def p_ParamDec(p):
    '''ParamDec : Specifier VarDec '''
    p[0] = Node("param_dec",[p[1],p[2]])


def p_CompSt(p):
    '''CompSt : LC DefList StmtList RC '''
    p[0] = Node('compst',[p[2],p[3]])


def p_StmtList(p):
    '''StmtList : Stmt StmtList
	| EMPTY'''
    if len(p) == 3:
        p[0] = Node('append',[p[1],p[2]])
    if len(p) == 2:
        p[0] = p[1]

def p_Stmt_return(p):
    '''Stmt : RETURN Exp SEMI'''
    p[0] = Node('return',[p[2]])

def p_FlowCtrl(p):
    '''FlowCtrl : IF LP Exp RP Stmt
	| IF LP Exp RP Stmt ELSE Stmt
	| WHILE LP Exp RP Stmt'''
    if p[1] == "if":
        if len(p) == 6:
            p[0] = Node('if',[p[3],p[5]])
        elif len(p)==8:
            p[0] = Node('if_else', [p[3], p[5], p[7]])
    elif p[1]=='while':
        p[0] = Node('while',[p[3],p[5]])

def p_Stmt(p):
    '''Stmt : Exp SEMI
	| CompSt
	| SEMI
	| FlowCtrl'''
    p[0] = p[1]

def p_DefList(p):
    '''DefList : Def DefList
	| EMPTY'''
    if len(p) == 3:
        p[0] = Node('append',[p[1],p[2]])
    elif len(p) == 2:
        p[0] = p[1]


def p_Def(p):
    '''Def : Specifier DecList SEMI '''
    p[0] = Node('def',[p[1],p[2]])


def p_DecList(p):
    '''DecList : Dec
	| Dec COMMA DecList '''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = Node('append',[p[1],p[3]])


def p_Dec(p):
    '''Dec : VarDec
	| VarDec ASSIGNOP Exp'''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = Node('init_assign', [p[1], p[3]])


def p_PrefixedExp(p):
    '''PrefixedExp : MINUS Exp
	| NOT Exp
	| PLUS Exp
	| STAR Exp
	| PLUSSLF Exp
	| SUBSLF Exp
	| LP TYPE RP Exp'''
    if len(p)==3:
        p[0] = Node(p[1]+"prefix",[p[2]])
    else:
        p[0] = Node('force_convert', [p[2]])

def p_Exp_par(p):
    '''Exp : LP Exp RP'''
    p[0] = p[1]

def p_Exp_Single(p):
    '''Exp : ID
	| NUMBER
	| DECIMAL
	| STRINGLITERAL'''
    p[0] = Leaf('SINGLE', p[1])

def p_Exp(p):
    '''Exp : Exp ASSIGNOP Exp
	| Exp AND Exp
	| Exp OR Exp
	| Exp RELOP Exp
	| Exp PLUS Exp
	| Exp MINUS Exp
	| Exp STAR Exp
	| Exp DIV Exp
	| Exp LB Exp RB
	| Exp DOT ID
	| PrefixedExp
	| FuncCall'''
    if len(p)==4:
        p[0] = Node(p[2], [p[1],p[3]])
    else:
        p[0] = p[1]


def p_FuncCall(p):
    '''FuncCall : ID LP Args RP
	| ID LP RP'''
    if len(p) == 5:
        p[0] = Node('call',[Leaf('ID',p[1]), p[3]])
    elif len(p)==4:
        p[0] = Node('call', [Leaf('ID',p[1])])


def p_Args(p):
    '''Args : Exp COMMA Args
	| Exp'''
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==4:
        p[0] = Node('',[p[1],p[3]])


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
int a, b(int a,int b),c;
int func1(){
    int a = 10, b = 20;
    puts("123123");
    puts("321321");
    printf("%d %d",a,b);
    return 1;
}

int func2(int a,int b,int c){
    return 3;
}

int main(){
    func1();
    func2(1,2,3);
    puts("hello world");
    return 0;
}
'''
node = parser.parse(s)
optimizer = TreeOptimizer()
optimizer.DeleteNone(node)
optimizer.PromotionNodes(node)
print(node)
