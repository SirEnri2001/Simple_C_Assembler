
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "Programleft(left[left.rightUPLUSUMINUSrightMEMADDRleft+-left*/ANDASSIGN AUTO BOOLAND BOOLOR BREAK CASE CHAR CONST CONTINUE DECIMAL DEFAULT DIVIDEASSIGN DO DOUBLE ELSE ENUM EQUAL EXTERN FLOAT FOR GOTO GRTREQL ID IF INT LESSEQL LONG LSHIFT LSHIFTASSIGN MODASSIGN MULASSIGN NEQUAL NUMBER ORASSIGN PLUSASSIGN PLUSSLF PRINT REGISTER RETURN RSHIFT RSHIFTASSIGN SHORT SIGNED SIZEOF STATIC STRINGLITERAL STRUCT SUBASSIGN SUBSLF SWITCH TYPEDEF UNION UNSIGNED VOID VOLATILE WHILE XORASSIGNEMPTY : RELOP : '>'\n    | '<'\n    | GRTREQL\n    | LESSEQL\n    | EQUAL\n    | NEQUAL TYPE : INT\n    | SHORT\n    | CHAR\n    | LONG\n\t| FLOAT\n\t| DOUBLEProgram : ExtDefList ExtDefList : ExtDef ExtDefList\n\t| EMPTYFunHead : Specifier FunDecExtDecHead : Specifier VarDecExtDecList : ExtDecList ',' VarDec\n        | ExtDecHeadExtDef : ExtDecList ';' ExtDef : Specifier ';' ExtDef : FunHead CompSt Specifier : TYPE\n\t| StructSpecifier StructSpecifier : STRUCT OptTag '{' DefList '}'\n\t| STRUCT Tag OptTag : ID\n\t| EMPTYTag : IDVarDec : ID\n    | '(' VarDec ')'\n\t| VarDec '[' NUMBER ']'\n\t| FunDecVarDec : '*' VarDecFunDec : ID '(' VarList ')'\n\t| ID '(' ')' VarList : ParamDec ',' VarList\n\t| ParamDec ParamDec : Specifier VarDec CompSt : '{' DefList StmtList '}' StmtList : Stmt StmtList\n\t| EMPTYStmt : RETURN Exp ';' Stmt : PRINT '(' Exp ')' ';' FlowCtrl : IF '(' Exp ')' Stmt\n\t| IF '(' Exp ')' Stmt ELSE Stmt\n\t| WHILE '(' Exp ')' StmtStmt : Exp ';'\n\t| CompSt\n\t| ';'\n\t| FlowCtrlDefList : Def ';' DefList\n\t| EMPTYDef : DecListDecHead : Specifier DecDecList : DecHead\n     | DecList ',' DecDec : VarDec\n\t| VarDec '=' ExpPrefixedExp : '*' Exp %prec MEM\n    | '&' Exp %prec ADDR SubTypeSpecifier : EMPTY\n    | '(' SubTypeSpecifier ')' SubTypeSpecifier : '*' SubTypeSpecifier\n    | SubTypeSpecifier '[' NUMBER ']' SubTypeSpecifier : SubTypeSpecifier '(' TypeList ')'\n    | SubTypeSpecifier '(' ')' TypeSpecifier : TYPE SubTypeSpecifierTypeList : TypeSpecifier\n    | TypeList ',' TypeSpecifier PrefixedExp : '-' Exp %prec UMINUS\n    \t| '+' Exp %prec UPLUS\n    \t| PLUSSLF Exp\n    \t| SUBSLF Exp\n    \t| '(' TypeSpecifier ')' ExpExp : '(' Exp ')' Exp : IDExp : NUMBERExp : DECIMALExp : STRINGLITERALExp : Exp '=' Exp\n\t| Exp '+' Exp\n\t| Exp '-' Exp\n\t| Exp '*' Exp\n\t| Exp '/' Exp\n\t| FuncCall\n\t| PrefixedExpExp : Exp BOOLAND Exp\n    \t| Exp BOOLOR Exp\n    \t| '!' ExpExp : Exp RELOP ExpExp : Exp '[' Exp ']'\n\t| Exp '.' IDFuncCall : ID '(' Args ')'\n\t| ID '(' ')' Args : Exp ',' Args\n\t| Exp"
    
_lr_action_items = {'$end':([0,1,2,3,4,18,19,21,27,87,],[-1,0,-14,-1,-16,-15,-21,-22,-23,-41,]),'INT':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[11,11,-21,-22,-23,11,11,11,11,11,11,-41,11,11,]),'SHORT':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[12,12,-21,-22,-23,12,12,12,12,12,12,-41,12,12,]),'CHAR':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[13,13,-21,-22,-23,13,13,13,13,13,13,-41,13,13,]),'LONG':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[14,14,-21,-22,-23,14,14,14,14,14,14,-41,14,14,]),'FLOAT':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[15,15,-21,-22,-23,15,15,15,15,15,15,-41,15,15,]),'DOUBLE':([0,3,19,21,27,28,37,46,60,78,85,87,154,172,],[16,16,-21,-22,-23,16,16,16,16,16,16,-41,16,16,]),'STRUCT':([0,3,19,21,27,28,37,46,78,85,87,],[17,17,-21,-22,-23,17,17,17,17,17,-41,]),';':([5,6,8,9,10,11,12,13,14,15,16,22,23,24,28,30,31,33,34,35,39,40,41,42,43,44,49,52,54,57,58,61,62,63,64,65,66,70,71,78,80,81,83,84,87,89,90,112,113,114,115,118,119,120,121,122,124,126,127,128,129,130,131,132,133,134,136,138,145,149,150,151,152,157,159,160,161,168,169,173,175,],[19,21,-20,-24,-25,-8,-9,-10,-11,-12,-13,-34,-18,-31,-1,-27,-30,-19,-31,-34,-35,58,78,-54,-55,-57,-37,-32,58,90,-51,-50,-52,-78,-79,-80,-81,-87,-88,-1,-56,-59,-33,-36,-41,126,-49,-73,-72,-61,-91,-62,-74,-75,-53,-58,-26,-44,-82,-83,-84,-85,-86,-89,-90,-92,-94,-77,-96,-60,-93,161,-76,-95,58,58,-45,-46,-48,58,-47,]),',':([5,8,11,12,13,14,15,16,22,23,24,33,34,35,39,43,44,49,50,52,63,64,65,66,70,71,80,81,83,84,86,110,112,113,114,115,118,119,120,122,127,128,129,130,131,132,133,134,136,138,140,141,143,145,146,149,150,152,156,157,163,164,165,166,170,171,174,],[20,-20,-8,-9,-10,-11,-12,-13,-34,-18,-31,-19,-31,-34,-35,79,-57,-37,85,-32,-78,-79,-80,-81,-87,-88,-56,-59,-33,-36,-40,-1,-73,-72,-61,-91,-62,-74,-75,-58,-82,-83,-84,-85,-86,-89,-90,-92,-94,-77,-69,-63,-1,-96,158,-60,-93,-76,-65,-95,172,-68,-70,-64,-66,-67,-71,]),'ID':([6,9,10,11,12,13,14,15,16,17,20,25,26,28,30,31,40,42,45,51,54,56,58,60,61,62,67,68,69,72,75,76,77,78,79,87,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,116,117,121,123,124,126,139,158,159,160,161,168,169,173,175,],[24,-24,-25,-8,-9,-10,-11,-12,-13,31,34,34,34,-1,-27,-30,63,-54,34,34,63,63,-51,63,-50,-52,63,63,63,63,63,63,63,-1,34,-41,-49,63,63,63,63,63,63,63,63,63,136,-2,-3,-4,-5,-6,-7,63,63,63,63,-53,63,-26,-44,63,63,63,63,-45,-46,-48,63,-47,]),'(':([6,9,10,11,12,13,14,15,16,20,24,25,26,28,30,31,34,40,42,45,51,54,56,58,59,60,61,62,63,67,68,69,72,73,74,75,76,77,78,79,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,111,116,117,121,123,124,126,139,140,141,142,143,155,156,158,159,160,161,164,166,168,169,170,171,173,175,],[25,-24,-25,-8,-9,-10,-11,-12,-13,25,37,25,25,-1,-27,-30,37,60,-54,25,25,60,60,-51,107,60,-50,-52,111,60,60,60,60,116,117,60,60,60,-1,25,-41,-49,60,60,60,60,60,60,60,60,60,-2,-3,-4,-5,-6,-7,60,142,60,60,60,-53,60,-26,-44,60,154,-63,142,142,154,-65,60,60,60,-45,-68,-64,-46,-48,-66,-67,60,-47,]),'*':([6,9,10,11,12,13,14,15,16,20,25,26,28,30,31,40,42,45,51,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,79,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,121,123,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,142,143,145,146,147,148,149,150,152,157,158,159,160,161,168,169,173,175,],[26,-24,-25,-8,-9,-10,-11,-12,-13,26,26,26,-1,-27,-30,69,-54,26,26,69,69,94,-51,69,-50,-52,-78,-79,-80,-81,69,69,69,-87,-88,69,69,69,69,-1,26,-41,94,-49,69,69,69,69,69,69,69,69,69,-2,-3,-4,-5,-6,-7,69,94,143,69,94,94,94,94,69,69,94,94,94,-53,69,-26,-44,94,94,94,-85,-86,94,94,94,94,-94,94,-77,69,143,143,-96,94,94,94,94,-93,94,-95,69,69,69,-45,-46,-48,69,-47,]),'{':([7,17,22,28,29,31,32,40,42,49,54,58,61,62,78,84,87,90,121,126,159,160,161,168,169,173,175,],[28,-1,-17,-1,46,-28,-29,28,-54,-37,28,-51,-50,-52,-1,-36,-41,-49,-53,-44,28,28,-45,-46,-48,28,-47,]),'[':([11,12,13,14,15,16,22,23,24,33,34,35,38,39,49,52,57,63,64,65,66,70,71,81,83,84,86,89,108,110,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,145,146,147,148,149,150,152,155,156,157,164,166,170,171,],[-8,-9,-10,-11,-12,-13,-34,36,-31,36,-31,-34,36,-35,-37,-32,99,-78,-79,-80,-81,-87,-88,36,-33,-36,36,99,99,-1,-73,-72,-61,99,-62,99,99,99,-83,-84,-85,-86,99,99,99,99,-94,99,-77,153,-63,-1,-1,-96,99,99,99,99,-93,99,153,-65,-95,-68,-64,-66,-67,]),')':([11,12,13,14,15,16,34,35,37,38,39,48,49,50,52,63,64,65,66,70,71,83,84,86,108,109,110,111,112,113,114,115,118,119,120,125,127,128,129,130,131,132,133,134,136,137,138,140,141,142,143,144,145,146,147,148,150,152,154,155,156,157,163,164,165,166,167,170,171,174,],[-8,-9,-10,-11,-12,-13,-31,-34,49,52,-35,84,-37,-39,-32,-78,-79,-80,-81,-87,-88,-33,-36,-40,138,139,-1,145,-73,-72,-61,-91,-62,-74,-75,-38,-82,-83,-84,-85,-86,-89,-90,-92,-94,151,-77,-69,-63,-1,-1,157,-96,-98,159,160,-93,-76,164,166,-65,-95,171,-68,-70,-64,-97,-66,-67,-71,]),'RETURN':([28,40,42,54,58,61,62,78,87,90,121,126,159,160,161,168,169,173,175,],[-1,56,-54,56,-51,-50,-52,-1,-41,-49,-53,-44,56,56,-45,-46,-48,56,-47,]),'PRINT':([28,40,42,54,58,61,62,78,87,90,121,126,159,160,161,168,169,173,175,],[-1,59,-54,59,-51,-50,-52,-1,-41,-49,-53,-44,59,59,-45,-46,-48,59,-47,]),'NUMBER':([28,36,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,153,158,159,160,161,168,169,173,175,],[-1,47,64,-54,64,64,-51,64,-50,-52,64,64,64,64,64,64,64,-1,-41,-49,64,64,64,64,64,64,64,64,64,-2,-3,-4,-5,-6,-7,64,64,64,64,-53,64,-44,64,162,64,64,64,-45,-46,-48,64,-47,]),'DECIMAL':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,65,-54,65,65,-51,65,-50,-52,65,65,65,65,65,65,65,-1,-41,-49,65,65,65,65,65,65,65,65,65,-2,-3,-4,-5,-6,-7,65,65,65,65,-53,65,-44,65,65,65,65,-45,-46,-48,65,-47,]),'STRINGLITERAL':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,66,-54,66,66,-51,66,-50,-52,66,66,66,66,66,66,66,-1,-41,-49,66,66,66,66,66,66,66,66,66,-2,-3,-4,-5,-6,-7,66,66,66,66,-53,66,-44,66,66,66,66,-45,-46,-48,66,-47,]),'!':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,72,-54,72,72,-51,72,-50,-52,72,72,72,72,72,72,72,-1,-41,-49,72,72,72,72,72,72,72,72,72,-2,-3,-4,-5,-6,-7,72,72,72,72,-53,72,-44,72,72,72,72,-45,-46,-48,72,-47,]),'IF':([28,40,42,54,58,61,62,78,87,90,121,126,159,160,161,168,169,173,175,],[-1,73,-54,73,-51,-50,-52,-1,-41,-49,-53,-44,73,73,-45,-46,-48,73,-47,]),'WHILE':([28,40,42,54,58,61,62,78,87,90,121,126,159,160,161,168,169,173,175,],[-1,74,-54,74,-51,-50,-52,-1,-41,-49,-53,-44,74,74,-45,-46,-48,74,-47,]),'&':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,75,-54,75,75,-51,75,-50,-52,75,75,75,75,75,75,75,-1,-41,-49,75,75,75,75,75,75,75,75,75,-2,-3,-4,-5,-6,-7,75,75,75,75,-53,75,-44,75,75,75,75,-45,-46,-48,75,-47,]),'-':([28,40,42,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118,119,120,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,145,146,147,148,149,150,152,157,158,159,160,161,168,169,173,175,],[-1,68,-54,68,68,93,-51,68,-50,-52,-78,-79,-80,-81,68,68,68,-87,-88,68,68,68,68,-1,-41,93,-49,68,68,68,68,68,68,68,68,68,-2,-3,-4,-5,-6,-7,68,93,68,93,93,93,93,68,68,93,93,93,-53,68,-44,93,-83,-84,-85,-86,93,93,93,93,-94,93,-77,68,-96,93,93,93,93,-93,93,-95,68,68,68,-45,-46,-48,68,-47,]),'+':([28,40,42,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118,119,120,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,145,146,147,148,149,150,152,157,158,159,160,161,168,169,173,175,],[-1,67,-54,67,67,92,-51,67,-50,-52,-78,-79,-80,-81,67,67,67,-87,-88,67,67,67,67,-1,-41,92,-49,67,67,67,67,67,67,67,67,67,-2,-3,-4,-5,-6,-7,67,92,67,92,92,92,92,67,67,92,92,92,-53,67,-44,92,-83,-84,-85,-86,92,92,92,92,-94,92,-77,67,-96,92,92,92,92,-93,92,-95,67,67,67,-45,-46,-48,67,-47,]),'PLUSSLF':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,76,-54,76,76,-51,76,-50,-52,76,76,76,76,76,76,76,-1,-41,-49,76,76,76,76,76,76,76,76,76,-2,-3,-4,-5,-6,-7,76,76,76,76,-53,76,-44,76,76,76,76,-45,-46,-48,76,-47,]),'SUBSLF':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,111,116,117,121,123,126,139,158,159,160,161,168,169,173,175,],[-1,77,-54,77,77,-51,77,-50,-52,77,77,77,77,77,77,77,-1,-41,-49,77,77,77,77,77,77,77,77,77,-2,-3,-4,-5,-6,-7,77,77,77,77,-53,77,-44,77,77,77,77,-45,-46,-48,77,-47,]),'}':([28,40,42,46,53,54,55,58,61,62,78,82,87,88,90,121,126,161,168,169,175,],[-1,-1,-54,-1,87,-1,-43,-51,-50,-52,-1,124,-41,-42,-49,-53,-44,-45,-46,-48,-47,]),'=':([34,35,39,49,52,57,63,64,65,66,70,71,81,83,84,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[-31,-34,-35,-37,-32,91,-78,-79,-80,-81,-87,-88,123,-33,-36,91,91,-73,-72,-61,91,-62,91,91,91,-83,-84,-85,-86,91,91,91,91,-94,91,-77,-96,91,91,91,91,-93,91,-95,]),']':([47,63,64,65,66,70,71,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,138,145,150,152,157,162,],[83,-78,-79,-80,-81,-87,-88,-73,-72,-61,-91,-62,-74,-75,-82,-83,-84,-85,-86,-89,-90,-92,150,-94,-77,-96,-93,-76,-95,170,]),'/':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[95,-78,-79,-80,-81,-87,-88,95,95,95,95,95,95,95,95,95,95,95,95,-85,-86,95,95,95,95,-94,95,-77,-96,95,95,95,95,-93,95,-95,]),'BOOLAND':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[96,-78,-79,-80,-81,-87,-88,96,96,-73,-72,-61,96,-62,96,96,96,-83,-84,-85,-86,96,96,96,96,-94,96,-77,-96,96,96,96,96,-93,96,-95,]),'BOOLOR':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[97,-78,-79,-80,-81,-87,-88,97,97,-73,-72,-61,97,-62,97,97,97,-83,-84,-85,-86,97,97,97,97,-94,97,-77,-96,97,97,97,97,-93,97,-95,]),'.':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[100,-78,-79,-80,-81,-87,-88,100,100,-73,-72,-61,100,-62,100,100,100,-83,-84,-85,-86,100,100,100,100,-94,100,-77,-96,100,100,100,100,-93,100,-95,]),'>':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[101,-78,-79,-80,-81,-87,-88,101,101,-73,-72,-61,101,-62,101,101,101,-83,-84,-85,-86,101,101,101,101,-94,101,-77,-96,101,101,101,101,-93,101,-95,]),'<':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[102,-78,-79,-80,-81,-87,-88,102,102,-73,-72,-61,102,-62,102,102,102,-83,-84,-85,-86,102,102,102,102,-94,102,-77,-96,102,102,102,102,-93,102,-95,]),'GRTREQL':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[103,-78,-79,-80,-81,-87,-88,103,103,-73,-72,-61,103,-62,103,103,103,-83,-84,-85,-86,103,103,103,103,-94,103,-77,-96,103,103,103,103,-93,103,-95,]),'LESSEQL':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[104,-78,-79,-80,-81,-87,-88,104,104,-73,-72,-61,104,-62,104,104,104,-83,-84,-85,-86,104,104,104,104,-94,104,-77,-96,104,104,104,104,-93,104,-95,]),'EQUAL':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[105,-78,-79,-80,-81,-87,-88,105,105,-73,-72,-61,105,-62,105,105,105,-83,-84,-85,-86,105,105,105,105,-94,105,-77,-96,105,105,105,105,-93,105,-95,]),'NEQUAL':([57,63,64,65,66,70,71,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,136,137,138,145,146,147,148,149,150,152,157,],[106,-78,-79,-80,-81,-87,-88,106,106,-73,-72,-61,106,-62,106,106,106,-83,-84,-85,-86,106,106,106,106,-94,106,-77,-96,106,106,106,106,-93,106,-95,]),'ELSE':([58,61,62,87,90,126,161,168,169,175,],[-51,-50,-52,-41,-49,-44,-45,173,-48,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'ExtDefList':([0,3,],[2,18,]),'ExtDef':([0,3,],[3,3,]),'EMPTY':([0,3,17,28,40,46,54,78,110,142,143,],[4,4,32,42,55,42,55,42,141,141,141,]),'ExtDecList':([0,3,],[5,5,]),'Specifier':([0,3,28,37,46,78,85,],[6,6,45,51,45,45,51,]),'FunHead':([0,3,],[7,7,]),'ExtDecHead':([0,3,],[8,8,]),'TYPE':([0,3,28,37,46,60,78,85,154,172,],[9,9,9,9,9,110,9,9,110,110,]),'StructSpecifier':([0,3,28,37,46,78,85,],[10,10,10,10,10,10,10,]),'FunDec':([6,20,25,26,45,51,79,],[22,35,35,35,35,35,35,]),'VarDec':([6,20,25,26,45,51,79,],[23,33,38,39,81,86,81,]),'CompSt':([7,40,54,159,160,173,],[27,61,61,61,61,61,]),'OptTag':([17,],[29,]),'Tag':([17,],[30,]),'DefList':([28,46,78,],[40,82,121,]),'Def':([28,46,78,],[41,41,41,]),'DecList':([28,46,78,],[43,43,43,]),'DecHead':([28,46,78,],[44,44,44,]),'VarList':([37,85,],[48,125,]),'ParamDec':([37,85,],[50,50,]),'StmtList':([40,54,],[53,88,]),'Stmt':([40,54,159,160,173,],[54,54,168,169,175,]),'Exp':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,111,116,117,123,139,158,159,160,173,],[57,57,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,137,146,147,148,149,152,146,57,57,57,]),'FlowCtrl':([40,54,159,160,173,],[62,62,62,62,62,]),'FuncCall':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,111,116,117,123,139,158,159,160,173,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'PrefixedExp':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,111,116,117,123,139,158,159,160,173,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'Dec':([45,79,],[80,122,]),'RELOP':([57,89,108,112,113,114,115,118,119,120,127,128,129,130,131,132,133,134,135,137,146,147,148,149,152,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'TypeSpecifier':([60,154,172,],[109,165,174,]),'SubTypeSpecifier':([110,142,143,],[140,155,156,]),'Args':([111,158,],[144,167,]),'TypeList':([154,],[163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','yacc.py',20),
  ('RELOP -> >','RELOP',1,'p_relop','yacc.py',25),
  ('RELOP -> <','RELOP',1,'p_relop','yacc.py',26),
  ('RELOP -> GRTREQL','RELOP',1,'p_relop','yacc.py',27),
  ('RELOP -> LESSEQL','RELOP',1,'p_relop','yacc.py',28),
  ('RELOP -> EQUAL','RELOP',1,'p_relop','yacc.py',29),
  ('RELOP -> NEQUAL','RELOP',1,'p_relop','yacc.py',30),
  ('TYPE -> INT','TYPE',1,'p_type','yacc.py',34),
  ('TYPE -> SHORT','TYPE',1,'p_type','yacc.py',35),
  ('TYPE -> CHAR','TYPE',1,'p_type','yacc.py',36),
  ('TYPE -> LONG','TYPE',1,'p_type','yacc.py',37),
  ('TYPE -> FLOAT','TYPE',1,'p_type','yacc.py',38),
  ('TYPE -> DOUBLE','TYPE',1,'p_type','yacc.py',39),
  ('Program -> ExtDefList','Program',1,'p_Program','yacc.py',43),
  ('ExtDefList -> ExtDef ExtDefList','ExtDefList',2,'p_ExtDefList','yacc.py',49),
  ('ExtDefList -> EMPTY','ExtDefList',1,'p_ExtDefList','yacc.py',50),
  ('FunHead -> Specifier FunDec','FunHead',2,'p_FunHead','yacc.py',58),
  ('ExtDecHead -> Specifier VarDec','ExtDecHead',2,'p_ExtDecHead','yacc.py',63),
  ('ExtDecList -> ExtDecList , VarDec','ExtDecList',3,'p_ExtDecList','yacc.py',73),
  ('ExtDecList -> ExtDecHead','ExtDecList',1,'p_ExtDecList','yacc.py',74),
  ('ExtDef -> ExtDecList ;','ExtDef',2,'p_ExtDef_ExtDecList','yacc.py',87),
  ('ExtDef -> Specifier ;','ExtDef',2,'p_ExtDef_Specifier','yacc.py',92),
  ('ExtDef -> FunHead CompSt','ExtDef',2,'p_ExtDef_FunDef','yacc.py',97),
  ('Specifier -> TYPE','Specifier',1,'p_Specifier','yacc.py',102),
  ('Specifier -> StructSpecifier','Specifier',1,'p_Specifier','yacc.py',103),
  ('StructSpecifier -> STRUCT OptTag { DefList }','StructSpecifier',5,'p_StructSpecifier','yacc.py',108),
  ('StructSpecifier -> STRUCT Tag','StructSpecifier',2,'p_StructSpecifier','yacc.py',109),
  ('OptTag -> ID','OptTag',1,'p_OptTag','yacc.py',117),
  ('OptTag -> EMPTY','OptTag',1,'p_OptTag','yacc.py',118),
  ('Tag -> ID','Tag',1,'p_Tag','yacc.py',123),
  ('VarDec -> ID','VarDec',1,'p_VarDec','yacc.py',128),
  ('VarDec -> ( VarDec )','VarDec',3,'p_VarDec','yacc.py',129),
  ('VarDec -> VarDec [ NUMBER ]','VarDec',4,'p_VarDec','yacc.py',130),
  ('VarDec -> FunDec','VarDec',1,'p_VarDec','yacc.py',131),
  ('VarDec -> * VarDec','VarDec',2,'p_VarDec_pointer','yacc.py',140),
  ('FunDec -> ID ( VarList )','FunDec',4,'p_FunDec','yacc.py',144),
  ('FunDec -> ID ( )','FunDec',3,'p_FunDec','yacc.py',145),
  ('VarList -> ParamDec , VarList','VarList',3,'p_VarList','yacc.py',153),
  ('VarList -> ParamDec','VarList',1,'p_VarList','yacc.py',154),
  ('ParamDec -> Specifier VarDec','ParamDec',2,'p_ParamDec','yacc.py',162),
  ('CompSt -> { DefList StmtList }','CompSt',4,'p_CompSt','yacc.py',167),
  ('StmtList -> Stmt StmtList','StmtList',2,'p_StmtList','yacc.py',172),
  ('StmtList -> EMPTY','StmtList',1,'p_StmtList','yacc.py',173),
  ('Stmt -> RETURN Exp ;','Stmt',3,'p_Stmt_return','yacc.py',181),
  ('Stmt -> PRINT ( Exp ) ;','Stmt',5,'p_Stmt_print','yacc.py',185),
  ('FlowCtrl -> IF ( Exp ) Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',189),
  ('FlowCtrl -> IF ( Exp ) Stmt ELSE Stmt','FlowCtrl',7,'p_FlowCtrl','yacc.py',190),
  ('FlowCtrl -> WHILE ( Exp ) Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',191),
  ('Stmt -> Exp ;','Stmt',2,'p_Stmt','yacc.py',202),
  ('Stmt -> CompSt','Stmt',1,'p_Stmt','yacc.py',203),
  ('Stmt -> ;','Stmt',1,'p_Stmt','yacc.py',204),
  ('Stmt -> FlowCtrl','Stmt',1,'p_Stmt','yacc.py',205),
  ('DefList -> Def ; DefList','DefList',3,'p_DefList','yacc.py',209),
  ('DefList -> EMPTY','DefList',1,'p_DefList','yacc.py',210),
  ('Def -> DecList','Def',1,'p_Def','yacc.py',218),
  ('DecHead -> Specifier Dec','DecHead',2,'p_DecHead','yacc.py',223),
  ('DecList -> DecHead','DecList',1,'p_DecList','yacc.py',228),
  ('DecList -> DecList , Dec','DecList',3,'p_DecList','yacc.py',229),
  ('Dec -> VarDec','Dec',1,'p_Dec','yacc.py',237),
  ('Dec -> VarDec = Exp','Dec',3,'p_Dec','yacc.py',238),
  ('PrefixedExp -> * Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',246),
  ('PrefixedExp -> & Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',247),
  ('SubTypeSpecifier -> EMPTY','SubTypeSpecifier',1,'p_SubTypeSpecifier','yacc.py',251),
  ('SubTypeSpecifier -> ( SubTypeSpecifier )','SubTypeSpecifier',3,'p_SubTypeSpecifier','yacc.py',252),
  ('SubTypeSpecifier -> * SubTypeSpecifier','SubTypeSpecifier',2,'p_SubTypeSpecifier_Mem','yacc.py',259),
  ('SubTypeSpecifier -> SubTypeSpecifier [ NUMBER ]','SubTypeSpecifier',4,'p_SubTypeSpecifier_Mem','yacc.py',260),
  ('SubTypeSpecifier -> SubTypeSpecifier ( TypeList )','SubTypeSpecifier',4,'p_SubTypeSpecifier_function','yacc.py',268),
  ('SubTypeSpecifier -> SubTypeSpecifier ( )','SubTypeSpecifier',3,'p_SubTypeSpecifier_function','yacc.py',269),
  ('TypeSpecifier -> TYPE SubTypeSpecifier','TypeSpecifier',2,'p_TypeSpecifier','yacc.py',274),
  ('TypeList -> TypeSpecifier','TypeList',1,'p_TypeList','yacc.py',279),
  ('TypeList -> TypeList , TypeSpecifier','TypeList',3,'p_TypeList','yacc.py',280),
  ('PrefixedExp -> - Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',287),
  ('PrefixedExp -> + Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',288),
  ('PrefixedExp -> PLUSSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',289),
  ('PrefixedExp -> SUBSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',290),
  ('PrefixedExp -> ( TypeSpecifier ) Exp','PrefixedExp',4,'p_PrefixedExp','yacc.py',291),
  ('Exp -> ( Exp )','Exp',3,'p_Exp_par','yacc.py',299),
  ('Exp -> ID','Exp',1,'p_Exp_Id','yacc.py',304),
  ('Exp -> NUMBER','Exp',1,'p_Exp_Number','yacc.py',308),
  ('Exp -> DECIMAL','Exp',1,'p_Exp_Constant_decimal','yacc.py',313),
  ('Exp -> STRINGLITERAL','Exp',1,'p_Exp_Constant_string','yacc.py',318),
  ('Exp -> Exp = Exp','Exp',3,'p_Exp','yacc.py',324),
  ('Exp -> Exp + Exp','Exp',3,'p_Exp','yacc.py',325),
  ('Exp -> Exp - Exp','Exp',3,'p_Exp','yacc.py',326),
  ('Exp -> Exp * Exp','Exp',3,'p_Exp','yacc.py',327),
  ('Exp -> Exp / Exp','Exp',3,'p_Exp','yacc.py',328),
  ('Exp -> FuncCall','Exp',1,'p_Exp','yacc.py',329),
  ('Exp -> PrefixedExp','Exp',1,'p_Exp','yacc.py',330),
  ('Exp -> Exp BOOLAND Exp','Exp',3,'p_Exp_Logic','yacc.py',337),
  ('Exp -> Exp BOOLOR Exp','Exp',3,'p_Exp_Logic','yacc.py',338),
  ('Exp -> ! Exp','Exp',2,'p_Exp_Logic','yacc.py',339),
  ('Exp -> Exp RELOP Exp','Exp',3,'p_Exp_Relop','yacc.py',346),
  ('Exp -> Exp [ Exp ]','Exp',4,'p_Exp_Mem','yacc.py',351),
  ('Exp -> Exp . ID','Exp',3,'p_Exp_Mem','yacc.py',352),
  ('FuncCall -> ID ( Args )','FuncCall',4,'p_FuncCall','yacc.py',360),
  ('FuncCall -> ID ( )','FuncCall',3,'p_FuncCall','yacc.py',361),
  ('Args -> Exp , Args','Args',3,'p_Args','yacc.py',369),
  ('Args -> Exp','Args',1,'p_Args','yacc.py',370),
]
