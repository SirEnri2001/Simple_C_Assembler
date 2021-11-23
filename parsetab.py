
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ProgramANDASSIGN AUTO BOOLAND BOOLOR BREAK CASE CHAR CONST CONTINUE DECIMAL DEFAULT DIVIDEASSIGN DO DOUBLE ELSE ENUM EQUAL EXTERN FLOAT FOR GOTO GRTREQL ID IF INT LESSEQL LONG LSHIFT LSHIFTASSIGN MODASSIGN MULASSIGN NEQUAL NUMBER ORASSIGN PLUSASSIGN PLUSSLF REGISTER RETURN RSHIFT RSHIFTASSIGN SHORT SIGNED SIZEOF STATIC STRINGLITERAL STRUCT SUBASSIGN SUBSLF SWITCH TYPEDEF UNION UNSIGNED VOID VOLATILE WHILE XORASSIGNEMPTY : SEMI : ';' COMMA : ',' ASSIGNOP : '=' RELOP : '>'\n    | '<'\n    | GRTREQL\n    | LESSEQL\n    | EQUAL\n    | NEQUAL PLUS : '+' MINUS : '-' STAR : '*' DIV : '/' AND : BOOLAND OR : BOOLOR DOT : '.' NOT : '!' TYPE : INT\n\t| FLOAT LP : '(' RP : ')' LB : '[' RB : ']' LC : '{' RC : '}' Program : ExtDefList ExtDefList : ExtDef ExtDefList\n\t| EMPTYFunHead : Specifier FunDecExtDecHead : Specifier VarDecExtDecHead : Specifier FunDecExtDecList : ExtDecList COMMA VarDec\n        | ExtDecHeadExtDecList : ExtDecList COMMA FunDecExtDef : ExtDecList SEMIExtDef : Specifier SEMIExtDef : FunHead CompSt Specifier : TYPE\n\t| StructSpecifier StructSpecifier : STRUCT OptTag LC DefList RC\n\t| STRUCT Tag OptTag : ID\n\t| EMPTYTag : IDVarDec : ID\n\t| VarDec LB NUMBER RB FunDec : ID LP VarList RP\n\t| ID LP RP VarList : ParamDec COMMA VarList\n\t| ParamDec ParamDec : Specifier VarDec CompSt : LC DefList StmtList RC StmtList : Stmt StmtList\n\t| EMPTYStmt : RETURN Exp SEMIFlowCtrl : IF LP Exp RP Stmt\n\t| IF LP Exp RP Stmt ELSE Stmt\n\t| WHILE LP Exp RP StmtStmt : Exp SEMI\n\t| CompSt\n\t| SEMI\n\t| FlowCtrlDefList : Def SEMI DefList\n\t| EMPTYDef : DecListDecHead : Specifier DecDecList : DecHead\n     | DecList COMMA DecDec : VarDec\n\t| VarDec ASSIGNOP ExpPrefixedExp : STAR Exp\n    | '&' ExpPrefixedExp : MINUS Exp\n    \t| NOT Exp\n    \t| PLUS Exp\n    \t| PLUSSLF Exp\n    \t| SUBSLF Exp\n    \t| LP TYPE RP ExpExp : LP Exp RPExp : ID\n\t| NUMBERExp : DECIMAL\n\t| STRINGLITERALExp : Exp ASSIGNOP Exp\n\t| Exp AND Exp\n\t| Exp OR Exp\n\t| Exp RELOP Exp\n\t| Exp PLUS Exp\n\t| Exp MINUS Exp\n\t| Exp STAR Exp\n\t| Exp DIV Exp\n\t| FuncCall\n\t| PrefixedExpExp : Exp LB Exp RB\n\t| Exp DOT IDFuncCall : ID LP Args RP\n\t| ID LP RPArgs : Exp COMMA Args\n\t| Exp"
    
_lr_action_items = {'$end':([0,1,2,3,4,14,15,17,19,23,89,90,],[-1,0,-27,-1,-29,-28,-36,-2,-37,-38,-53,-26,]),'INT':([0,3,15,17,18,19,23,24,25,35,36,43,58,78,87,89,90,],[11,11,-36,-2,-3,-37,-38,11,-25,11,-21,11,11,11,11,-53,-26,]),'FLOAT':([0,3,15,17,18,19,23,24,25,35,36,43,58,78,87,89,90,],[12,12,-36,-2,-3,-37,-38,12,-25,12,-21,12,12,12,12,-53,-26,]),'STRUCT':([0,3,15,17,18,19,23,24,25,35,36,43,78,87,89,90,],[13,13,-36,-2,-3,-37,-38,13,-25,13,-21,13,13,13,-53,-26,]),';':([5,6,8,9,10,11,12,17,20,21,22,24,25,27,28,30,31,32,37,38,39,40,41,46,48,51,54,55,56,57,59,60,61,62,66,67,78,80,81,82,84,85,86,89,90,92,93,118,119,120,123,124,125,126,127,128,130,132,133,134,135,136,137,138,139,140,142,143,146,150,151,152,153,155,156,158,159,160,161,],[17,17,-34,-39,-40,-19,-20,-2,-32,-31,-46,-1,-25,-42,-45,-33,-35,-46,17,17,-65,-66,-68,-49,-22,17,17,-62,-61,-63,-81,-82,-83,-84,-93,-94,-1,-67,-70,-46,-47,-24,-48,-53,-26,17,-60,-76,-74,-72,-73,-75,-77,-78,-64,-69,-41,-56,-85,-86,-87,-88,-89,-90,-91,-92,-96,-80,-98,-71,-95,-79,-97,17,17,-57,-59,17,-58,]),',':([5,8,20,21,22,30,31,32,40,41,46,47,48,59,60,61,62,66,67,80,81,82,84,85,86,88,118,119,120,123,124,125,126,128,133,134,135,136,137,138,139,140,142,143,146,147,150,151,152,153,],[18,-34,-32,-31,-46,-33,-35,-46,18,-68,-49,18,-22,-81,-82,-83,-84,-93,-94,-67,-70,-46,-47,-24,-48,-52,-76,-74,-72,-73,-75,-77,-78,-69,-85,-86,-87,-88,-89,-90,-91,-92,-96,-80,-98,18,-71,-95,-79,-97,]),'ID':([6,9,10,11,12,13,16,17,18,24,25,27,28,34,36,37,39,42,48,49,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,79,89,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,117,121,122,127,129,130,132,144,154,155,156,158,159,160,161,],[22,-39,-40,-19,-20,28,32,-2,-3,-1,-25,-42,-45,-23,-21,59,-65,82,-22,82,59,59,-62,-61,-63,59,59,59,59,59,59,59,59,-13,-12,-18,-11,-1,82,-53,-26,-60,59,59,59,59,59,59,59,59,59,142,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,-17,59,59,59,-64,59,-41,-56,59,59,59,59,-57,-59,59,-58,]),'{':([7,13,17,20,24,25,26,28,29,37,39,46,48,51,55,56,57,78,86,89,90,93,127,132,155,156,158,159,160,161,],[25,-1,-2,-30,-1,-25,25,-43,-44,25,-65,-49,-22,25,-62,-61,-63,-1,-48,-53,-26,-60,-64,-56,25,25,-57,-59,25,-58,]),')':([11,12,35,36,45,47,48,59,60,61,62,66,67,82,84,85,88,115,116,117,118,119,120,123,124,125,126,131,133,134,135,136,137,138,139,140,142,143,145,146,147,148,149,151,152,153,157,],[-19,-20,48,-21,48,-51,-22,-81,-82,-83,-84,-93,-94,-46,-47,-24,-52,48,48,48,-76,-74,-72,-73,-75,-77,-78,-50,-85,-86,-87,-88,-89,-90,-91,-92,-96,-80,48,-98,-100,48,48,-95,-79,-97,-99,]),'RETURN':([17,24,25,37,39,48,51,55,56,57,78,89,90,93,127,132,155,156,158,159,160,161,],[-2,-1,-25,53,-65,-22,53,-62,-61,-63,-1,-53,-26,-60,-64,-56,53,53,-57,-59,53,-58,]),'NUMBER':([17,18,24,25,33,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,44,-23,-21,60,-65,-22,60,60,-62,-61,-63,60,60,60,60,60,60,60,60,-13,-12,-18,-11,-1,-53,-26,-60,60,60,60,60,60,60,60,60,60,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,60,60,60,-64,60,-56,60,60,60,60,-57,-59,60,-58,]),'DECIMAL':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,61,-65,-22,61,61,-62,-61,-63,61,61,61,61,61,61,61,61,-13,-12,-18,-11,-1,-53,-26,-60,61,61,61,61,61,61,61,61,61,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,61,61,61,-64,61,-56,61,61,61,61,-57,-59,61,-58,]),'STRINGLITERAL':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,62,-65,-22,62,62,-62,-61,-63,62,62,62,62,62,62,62,62,-13,-12,-18,-11,-1,-53,-26,-60,62,62,62,62,62,62,62,62,62,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,62,62,62,-64,62,-56,62,62,62,62,-57,-59,62,-58,]),'IF':([17,24,25,37,39,48,51,55,56,57,78,89,90,93,127,132,155,156,158,159,160,161,],[-2,-1,-25,68,-65,-22,68,-62,-61,-63,-1,-53,-26,-60,-64,-56,68,68,-57,-59,68,-58,]),'WHILE':([17,24,25,37,39,48,51,55,56,57,78,89,90,93,127,132,155,156,158,159,160,161,],[-2,-1,-25,69,-65,-22,69,-62,-61,-63,-1,-53,-26,-60,-64,-56,69,69,-57,-59,69,-58,]),'(':([17,18,22,24,25,32,34,36,37,39,48,51,53,55,56,57,58,59,63,64,65,68,69,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,36,-1,-25,36,-23,-21,36,-65,-22,36,36,-62,-61,-63,36,36,36,36,36,36,36,36,36,36,36,-13,-12,-18,-11,-1,-53,-26,-60,36,36,36,36,36,36,36,36,36,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,36,36,36,-64,36,-56,36,36,36,36,-57,-59,36,-58,]),'&':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,70,-65,-22,70,70,-62,-61,-63,70,70,70,70,70,70,70,70,-13,-12,-18,-11,-1,-53,-26,-60,70,70,70,70,70,70,70,70,70,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,70,70,70,-64,70,-56,70,70,70,70,-57,-59,70,-58,]),'PLUSSLF':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,72,-65,-22,72,72,-62,-61,-63,72,72,72,72,72,72,72,72,-13,-12,-18,-11,-1,-53,-26,-60,72,72,72,72,72,72,72,72,72,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,72,72,72,-64,72,-56,72,72,72,72,-57,-59,72,-58,]),'SUBSLF':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,73,-65,-22,73,73,-62,-61,-63,73,73,73,73,73,73,73,73,-13,-12,-18,-11,-1,-53,-26,-60,73,73,73,73,73,73,73,73,73,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,73,73,73,-64,73,-56,73,73,73,73,-57,-59,73,-58,]),'*':([17,18,24,25,34,36,37,39,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,73,74,75,76,77,78,85,89,90,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,115,117,118,119,120,121,122,123,124,125,126,127,129,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,74,-65,-22,74,74,74,-62,-61,-63,74,-81,-82,-83,-84,74,74,74,-93,-94,74,74,74,74,-13,-12,-18,-11,-1,-24,-53,-26,74,-60,74,74,74,74,74,74,74,74,74,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,74,74,74,74,74,74,74,74,74,74,74,-64,74,-56,74,74,74,74,74,74,74,74,74,-96,-80,74,-98,74,74,74,74,-95,74,-97,74,74,74,-57,-59,74,-58,]),'-':([17,18,24,25,34,36,37,39,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,73,74,75,76,77,78,85,89,90,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,115,117,118,119,120,121,122,123,124,125,126,127,129,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,75,-65,-22,75,75,75,-62,-61,-63,75,-81,-82,-83,-84,75,75,75,-93,-94,75,75,75,75,-13,-12,-18,-11,-1,-24,-53,-26,75,-60,75,75,75,75,75,75,75,75,75,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,75,75,75,75,75,75,75,75,75,75,75,-64,75,-56,75,75,75,75,75,75,75,75,75,-96,-80,75,-98,75,75,75,75,-95,75,-97,75,75,75,-57,-59,75,-58,]),'!':([17,18,24,25,34,36,37,39,48,51,53,55,56,57,58,63,64,65,70,71,72,73,74,75,76,77,78,89,90,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,117,121,122,127,129,132,144,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,76,-65,-22,76,76,-62,-61,-63,76,76,76,76,76,76,76,76,-13,-12,-18,-11,-1,-53,-26,-60,76,76,76,76,76,76,76,76,76,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,76,76,76,-64,76,-56,76,76,76,76,-57,-59,76,-58,]),'+':([17,18,24,25,34,36,37,39,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,73,74,75,76,77,78,85,89,90,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,115,117,118,119,120,121,122,123,124,125,126,127,129,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,],[-2,-3,-1,-25,-23,-21,77,-65,-22,77,77,77,-62,-61,-63,77,-81,-82,-83,-84,77,77,77,-93,-94,77,77,77,77,-13,-12,-18,-11,-1,-24,-53,-26,77,-60,77,77,77,77,77,77,77,77,77,-4,-15,-16,-5,-6,-7,-8,-9,-10,-14,77,77,77,77,77,77,77,77,77,77,77,-64,77,-56,77,77,77,77,77,77,77,77,77,-96,-80,77,-98,77,77,77,77,-95,77,-97,77,77,77,-57,-59,77,-58,]),'}':([17,24,25,37,39,43,50,51,52,55,56,57,78,83,89,90,91,93,127,132,158,159,161,],[-2,-1,-25,-1,-65,-1,90,-1,-55,-62,-61,-63,-1,90,-53,-26,-54,-60,-64,-56,-57,-59,-58,]),'ELSE':([17,55,56,57,89,90,93,132,158,159,161,],[-2,-62,-61,-63,-53,-26,-60,-56,160,-59,-58,]),'[':([21,22,30,32,48,54,59,60,61,62,66,67,81,82,84,85,88,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[34,-46,34,-46,-22,34,-81,-82,-83,-84,-93,-94,34,-46,-47,-24,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-96,-80,-98,34,34,34,34,-95,34,-97,]),']':([44,48,59,60,61,62,66,67,85,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,151,152,153,],[85,-22,-81,-82,-83,-84,-93,-94,-24,-76,-74,-72,-73,-75,-77,-78,-85,-86,-87,-88,-89,-90,-91,-92,85,-96,-80,-98,-95,-79,-97,]),'=':([48,54,59,60,61,62,66,67,81,82,84,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,104,-81,-82,-83,-84,-93,-94,104,-46,-47,-24,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,-96,-80,-98,104,104,104,104,-95,104,-97,]),'BOOLAND':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,105,-81,-82,-83,-84,-93,-94,-24,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,-96,-80,-98,105,105,105,105,-95,105,-97,]),'BOOLOR':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,106,-81,-82,-83,-84,-93,-94,-24,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,-96,-80,-98,106,106,106,106,-95,106,-97,]),'>':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,107,-81,-82,-83,-84,-93,-94,-24,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,-96,-80,-98,107,107,107,107,-95,107,-97,]),'<':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,108,-81,-82,-83,-84,-93,-94,-24,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,-96,-80,-98,108,108,108,108,-95,108,-97,]),'GRTREQL':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,109,-81,-82,-83,-84,-93,-94,-24,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,-96,-80,-98,109,109,109,109,-95,109,-97,]),'LESSEQL':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,110,-81,-82,-83,-84,-93,-94,-24,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,-96,-80,-98,110,110,110,110,-95,110,-97,]),'EQUAL':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,111,-81,-82,-83,-84,-93,-94,-24,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,-96,-80,-98,111,111,111,111,-95,111,-97,]),'NEQUAL':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,112,-81,-82,-83,-84,-93,-94,-24,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,-96,-80,-98,112,112,112,112,-95,112,-97,]),'/':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,113,-81,-82,-83,-84,-93,-94,-24,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,-96,-80,-98,113,113,113,113,-95,113,-97,]),'.':([48,54,59,60,61,62,66,67,85,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,],[-22,114,-81,-82,-83,-84,-93,-94,-24,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,-96,-80,-98,114,114,114,114,-95,114,-97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'ExtDefList':([0,3,],[2,14,]),'ExtDef':([0,3,],[3,3,]),'EMPTY':([0,3,13,24,37,43,51,78,],[4,4,29,39,52,39,52,39,]),'ExtDecList':([0,3,],[5,5,]),'Specifier':([0,3,24,35,43,78,87,],[6,6,42,49,42,42,49,]),'FunHead':([0,3,],[7,7,]),'ExtDecHead':([0,3,],[8,8,]),'TYPE':([0,3,24,35,43,58,78,87,],[9,9,9,9,9,116,9,9,]),'StructSpecifier':([0,3,24,35,43,78,87,],[10,10,10,10,10,10,10,]),'SEMI':([5,6,37,38,51,54,92,155,156,160,],[15,19,55,78,55,93,132,55,55,55,]),'COMMA':([5,40,47,147,],[16,79,87,154,]),'FunDec':([6,16,],[20,31,]),'VarDec':([6,16,42,49,79,],[21,30,81,88,81,]),'CompSt':([7,37,51,155,156,160,],[23,56,56,56,56,56,]),'LC':([7,26,37,51,155,156,160,],[24,43,24,24,24,24,24,]),'OptTag':([13,],[26,]),'Tag':([13,],[27,]),'LB':([21,30,54,81,88,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[33,33,102,33,33,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'LP':([22,32,37,51,53,58,59,63,64,65,68,69,70,71,72,73,94,95,96,97,98,99,100,101,102,117,121,122,129,144,154,155,156,160,],[35,35,58,58,58,58,117,58,58,58,121,122,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'DefList':([24,43,78,],[37,83,127,]),'Def':([24,43,78,],[38,38,38,]),'DecList':([24,43,78,],[40,40,40,]),'DecHead':([24,43,78,],[41,41,41,]),'VarList':([35,87,],[45,131,]),'RP':([35,45,115,116,117,145,148,149,],[46,86,143,144,146,153,155,156,]),'ParamDec':([35,87,],[47,47,]),'StmtList':([37,51,],[50,91,]),'Stmt':([37,51,155,156,160,],[51,51,158,159,161,]),'Exp':([37,51,53,58,63,64,65,70,71,72,73,94,95,96,97,98,99,100,101,102,117,121,122,129,144,154,155,156,160,],[54,54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,147,54,54,54,]),'FlowCtrl':([37,51,155,156,160,],[57,57,57,57,57,]),'PLUS':([37,51,53,54,58,63,64,65,70,71,72,73,92,94,95,96,97,98,99,100,101,102,115,117,118,119,120,121,122,123,124,125,126,129,133,134,135,136,137,138,139,140,141,144,147,148,149,150,152,154,155,156,160,],[63,63,63,98,63,63,63,63,63,63,63,63,98,63,63,63,63,63,63,63,63,63,98,63,98,98,98,63,63,98,98,98,98,63,98,98,98,98,98,98,98,98,98,63,98,98,98,98,98,63,63,63,63,]),'MINUS':([37,51,53,54,58,63,64,65,70,71,72,73,92,94,95,96,97,98,99,100,101,102,115,117,118,119,120,121,122,123,124,125,126,129,133,134,135,136,137,138,139,140,141,144,147,148,149,150,152,154,155,156,160,],[64,64,64,99,64,64,64,64,64,64,64,64,99,64,64,64,64,64,64,64,64,64,99,64,99,99,99,64,64,99,99,99,99,64,99,99,99,99,99,99,99,99,99,64,99,99,99,99,99,64,64,64,64,]),'STAR':([37,51,53,54,58,63,64,65,70,71,72,73,92,94,95,96,97,98,99,100,101,102,115,117,118,119,120,121,122,123,124,125,126,129,133,134,135,136,137,138,139,140,141,144,147,148,149,150,152,154,155,156,160,],[65,65,65,100,65,65,65,65,65,65,65,65,100,65,65,65,65,65,65,65,65,65,100,65,100,100,100,65,65,100,100,100,100,65,100,100,100,100,100,100,100,100,100,65,100,100,100,100,100,65,65,65,65,]),'FuncCall':([37,51,53,58,63,64,65,70,71,72,73,94,95,96,97,98,99,100,101,102,117,121,122,129,144,154,155,156,160,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'PrefixedExp':([37,51,53,58,63,64,65,70,71,72,73,94,95,96,97,98,99,100,101,102,117,121,122,129,144,154,155,156,160,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'NOT':([37,51,53,58,63,64,65,70,71,72,73,94,95,96,97,98,99,100,101,102,117,121,122,129,144,154,155,156,160,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'Dec':([42,79,],[80,128,]),'RB':([44,141,],[84,151,]),'RC':([50,83,],[89,130,]),'ASSIGNOP':([54,81,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[94,129,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'AND':([54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'OR':([54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'RELOP':([54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'DIV':([54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'DOT':([54,92,115,118,119,120,123,124,125,126,133,134,135,136,137,138,139,140,141,147,148,149,150,152,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'Args':([117,154,],[145,157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','yacc.py',14),
  ('SEMI -> ;','SEMI',1,'p_semi','yacc.py',19),
  ('COMMA -> ,','COMMA',1,'p_comma','yacc.py',24),
  ('ASSIGNOP -> =','ASSIGNOP',1,'p_assignop','yacc.py',29),
  ('RELOP -> >','RELOP',1,'p_relop','yacc.py',34),
  ('RELOP -> <','RELOP',1,'p_relop','yacc.py',35),
  ('RELOP -> GRTREQL','RELOP',1,'p_relop','yacc.py',36),
  ('RELOP -> LESSEQL','RELOP',1,'p_relop','yacc.py',37),
  ('RELOP -> EQUAL','RELOP',1,'p_relop','yacc.py',38),
  ('RELOP -> NEQUAL','RELOP',1,'p_relop','yacc.py',39),
  ('PLUS -> +','PLUS',1,'p_plus','yacc.py',44),
  ('MINUS -> -','MINUS',1,'p_minus','yacc.py',49),
  ('STAR -> *','STAR',1,'p_star','yacc.py',54),
  ('DIV -> /','DIV',1,'p_div','yacc.py',59),
  ('AND -> BOOLAND','AND',1,'p_and','yacc.py',64),
  ('OR -> BOOLOR','OR',1,'p_or','yacc.py',69),
  ('DOT -> .','DOT',1,'p_dot','yacc.py',74),
  ('NOT -> !','NOT',1,'p_not','yacc.py',79),
  ('TYPE -> INT','TYPE',1,'p_type','yacc.py',84),
  ('TYPE -> FLOAT','TYPE',1,'p_type','yacc.py',85),
  ('LP -> (','LP',1,'p_lp','yacc.py',90),
  ('RP -> )','RP',1,'p_rp','yacc.py',95),
  ('LB -> [','LB',1,'p_lb','yacc.py',100),
  ('RB -> ]','RB',1,'p_rb','yacc.py',105),
  ('LC -> {','LC',1,'p_lc','yacc.py',110),
  ('RC -> }','RC',1,'p_rc','yacc.py',115),
  ('Program -> ExtDefList','Program',1,'p_Program','yacc.py',120),
  ('ExtDefList -> ExtDef ExtDefList','ExtDefList',2,'p_ExtDefList','yacc.py',126),
  ('ExtDefList -> EMPTY','ExtDefList',1,'p_ExtDefList','yacc.py',127),
  ('FunHead -> Specifier FunDec','FunHead',2,'p_FunHead','yacc.py',135),
  ('ExtDecHead -> Specifier VarDec','ExtDecHead',2,'p_ExtDecHead','yacc.py',140),
  ('ExtDecHead -> Specifier FunDec','ExtDecHead',2,'p_ExtDecHead_Fun','yacc.py',145),
  ('ExtDecList -> ExtDecList COMMA VarDec','ExtDecList',3,'p_ExtDecList','yacc.py',150),
  ('ExtDecList -> ExtDecHead','ExtDecList',1,'p_ExtDecList','yacc.py',151),
  ('ExtDecList -> ExtDecList COMMA FunDec','ExtDecList',3,'p_ExtDecList_Fun','yacc.py',159),
  ('ExtDef -> ExtDecList SEMI','ExtDef',2,'p_ExtDef_ExtDecList','yacc.py',164),
  ('ExtDef -> Specifier SEMI','ExtDef',2,'p_ExtDef_Specifier','yacc.py',169),
  ('ExtDef -> FunHead CompSt','ExtDef',2,'p_ExtDef_FunDef','yacc.py',174),
  ('Specifier -> TYPE','Specifier',1,'p_Specifier','yacc.py',179),
  ('Specifier -> StructSpecifier','Specifier',1,'p_Specifier','yacc.py',180),
  ('StructSpecifier -> STRUCT OptTag LC DefList RC','StructSpecifier',5,'p_StructSpecifier','yacc.py',185),
  ('StructSpecifier -> STRUCT Tag','StructSpecifier',2,'p_StructSpecifier','yacc.py',186),
  ('OptTag -> ID','OptTag',1,'p_OptTag','yacc.py',194),
  ('OptTag -> EMPTY','OptTag',1,'p_OptTag','yacc.py',195),
  ('Tag -> ID','Tag',1,'p_Tag','yacc.py',200),
  ('VarDec -> ID','VarDec',1,'p_VarDec','yacc.py',205),
  ('VarDec -> VarDec LB NUMBER RB','VarDec',4,'p_VarDec','yacc.py',206),
  ('FunDec -> ID LP VarList RP','FunDec',4,'p_FunDec','yacc.py',214),
  ('FunDec -> ID LP RP','FunDec',3,'p_FunDec','yacc.py',215),
  ('VarList -> ParamDec COMMA VarList','VarList',3,'p_VarList','yacc.py',223),
  ('VarList -> ParamDec','VarList',1,'p_VarList','yacc.py',224),
  ('ParamDec -> Specifier VarDec','ParamDec',2,'p_ParamDec','yacc.py',232),
  ('CompSt -> LC DefList StmtList RC','CompSt',4,'p_CompSt','yacc.py',237),
  ('StmtList -> Stmt StmtList','StmtList',2,'p_StmtList','yacc.py',242),
  ('StmtList -> EMPTY','StmtList',1,'p_StmtList','yacc.py',243),
  ('Stmt -> RETURN Exp SEMI','Stmt',3,'p_Stmt_return','yacc.py',251),
  ('FlowCtrl -> IF LP Exp RP Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',256),
  ('FlowCtrl -> IF LP Exp RP Stmt ELSE Stmt','FlowCtrl',7,'p_FlowCtrl','yacc.py',257),
  ('FlowCtrl -> WHILE LP Exp RP Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',258),
  ('Stmt -> Exp SEMI','Stmt',2,'p_Stmt','yacc.py',269),
  ('Stmt -> CompSt','Stmt',1,'p_Stmt','yacc.py',270),
  ('Stmt -> SEMI','Stmt',1,'p_Stmt','yacc.py',271),
  ('Stmt -> FlowCtrl','Stmt',1,'p_Stmt','yacc.py',272),
  ('DefList -> Def SEMI DefList','DefList',3,'p_DefList','yacc.py',277),
  ('DefList -> EMPTY','DefList',1,'p_DefList','yacc.py',278),
  ('Def -> DecList','Def',1,'p_Def','yacc.py',286),
  ('DecHead -> Specifier Dec','DecHead',2,'p_DecHead','yacc.py',291),
  ('DecList -> DecHead','DecList',1,'p_DecList','yacc.py',296),
  ('DecList -> DecList COMMA Dec','DecList',3,'p_DecList','yacc.py',297),
  ('Dec -> VarDec','Dec',1,'p_Dec','yacc.py',305),
  ('Dec -> VarDec ASSIGNOP Exp','Dec',3,'p_Dec','yacc.py',306),
  ('PrefixedExp -> STAR Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',314),
  ('PrefixedExp -> & Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',315),
  ('PrefixedExp -> MINUS Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',319),
  ('PrefixedExp -> NOT Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',320),
  ('PrefixedExp -> PLUS Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',321),
  ('PrefixedExp -> PLUSSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',322),
  ('PrefixedExp -> SUBSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',323),
  ('PrefixedExp -> LP TYPE RP Exp','PrefixedExp',4,'p_PrefixedExp','yacc.py',324),
  ('Exp -> LP Exp RP','Exp',3,'p_Exp_par','yacc.py',332),
  ('Exp -> ID','Exp',1,'p_Exp_Single','yacc.py',337),
  ('Exp -> NUMBER','Exp',1,'p_Exp_Single','yacc.py',338),
  ('Exp -> DECIMAL','Exp',1,'p_Exp_Single_Constant','yacc.py',343),
  ('Exp -> STRINGLITERAL','Exp',1,'p_Exp_Single_Constant','yacc.py',344),
  ('Exp -> Exp ASSIGNOP Exp','Exp',3,'p_Exp','yacc.py',350),
  ('Exp -> Exp AND Exp','Exp',3,'p_Exp','yacc.py',351),
  ('Exp -> Exp OR Exp','Exp',3,'p_Exp','yacc.py',352),
  ('Exp -> Exp RELOP Exp','Exp',3,'p_Exp','yacc.py',353),
  ('Exp -> Exp PLUS Exp','Exp',3,'p_Exp','yacc.py',354),
  ('Exp -> Exp MINUS Exp','Exp',3,'p_Exp','yacc.py',355),
  ('Exp -> Exp STAR Exp','Exp',3,'p_Exp','yacc.py',356),
  ('Exp -> Exp DIV Exp','Exp',3,'p_Exp','yacc.py',357),
  ('Exp -> FuncCall','Exp',1,'p_Exp','yacc.py',358),
  ('Exp -> PrefixedExp','Exp',1,'p_Exp','yacc.py',359),
  ('Exp -> Exp LB Exp RB','Exp',4,'p_Exp_Mem','yacc.py',367),
  ('Exp -> Exp DOT ID','Exp',3,'p_Exp_Mem','yacc.py',368),
  ('FuncCall -> ID LP Args RP','FuncCall',4,'p_FuncCall','yacc.py',376),
  ('FuncCall -> ID LP RP','FuncCall',3,'p_FuncCall','yacc.py',377),
  ('Args -> Exp COMMA Args','Args',3,'p_Args','yacc.py',385),
  ('Args -> Exp','Args',1,'p_Args','yacc.py',386),
]
