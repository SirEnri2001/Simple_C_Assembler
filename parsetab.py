
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "Programleft+-left*/rightUPLUSUMINUSANDASSIGN AUTO BOOLAND BOOLOR BREAK CASE CHAR CONST CONTINUE DECIMAL DEFAULT DIVIDEASSIGN DO DOUBLE ELSE ENUM EQUAL EXTERN FLOAT FOR GOTO GRTREQL ID IF INT LESSEQL LONG LSHIFT LSHIFTASSIGN MODASSIGN MULASSIGN NEQUAL NUMBER ORASSIGN PLUSASSIGN PLUSSLF PRINT REGISTER RETURN RSHIFT RSHIFTASSIGN SHORT SIGNED SIZEOF STATIC STRINGLITERAL STRUCT SUBASSIGN SUBSLF SWITCH TYPEDEF UNION UNSIGNED VOID VOLATILE WHILE XORASSIGNEMPTY : RELOP : '>'\n    | '<'\n    | GRTREQL\n    | LESSEQL\n    | EQUAL\n    | NEQUAL TYPE : INT\n    | SHORT\n    | CHAR\n    | LONG\n\t| FLOAT\n\t| DOUBLEProgram : ExtDefList ExtDefList : ExtDef ExtDefList\n\t| EMPTYFunHead : Specifier FunDecExtDecHead : Specifier VarDecExtDecList : ExtDecList ',' VarDec\n        | ExtDecHeadExtDef : ExtDecList ';' ExtDef : Specifier ';' ExtDef : FunHead CompSt Specifier : TYPE\n\t| StructSpecifier StructSpecifier : STRUCT OptTag '{' DefList '}'\n\t| STRUCT Tag OptTag : ID\n\t| EMPTYTag : IDVarDec : ID\n    | '(' VarDec ')'\n\t| VarDec '[' NUMBER ']'\n\t| FunDecVarDec : '*' VarDecFunDec : ID '(' VarList ')'\n\t| ID '(' ')' VarList : ParamDec ',' VarList\n\t| ParamDec ParamDec : Specifier VarDec CompSt : '{' DefList StmtList '}' StmtList : Stmt StmtList\n\t| EMPTYStmt : RETURN Exp ';' Stmt : PRINT '(' Exp ')' ';' FlowCtrl : IF '(' Exp ')' Stmt\n\t| IF '(' Exp ')' Stmt ELSE Stmt\n\t| WHILE '(' Exp ')' StmtStmt : Exp ';'\n\t| CompSt\n\t| ';'\n\t| FlowCtrlDefList : Def ';' DefList\n\t| EMPTYDef : DecListDecHead : Specifier DecDecList : DecHead\n     | DecList ',' DecDec : VarDec\n\t| VarDec '=' ExpPrefixedExp : '*' Exp\n    | '&' ExpPrefixedExp : '-' Exp %prec UMINUS\n    \t| '+' Exp %prec UPLUS\n    \t| PLUSSLF Exp\n    \t| SUBSLF Exp\n    \t| '(' TYPE ')' ExpExp : '(' Exp ')' Exp : IDExp : NUMBERExp : DECIMAL\n\t| STRINGLITERALExp : Exp '=' Exp\n\t| Exp '+' Exp\n\t| Exp '-' Exp\n\t| Exp '*' Exp\n\t| Exp '/' Exp\n\t| FuncCall\n\t| PrefixedExpExp : Exp BOOLAND Exp\n    \t| Exp BOOLOR Exp\n    \t| '!' ExpExp : Exp RELOP ExpExp : Exp '[' Exp ']'\n\t| Exp '.' IDFuncCall : ID '(' Args ')'\n\t| ID '(' ')' Args : Exp ',' Args\n\t| Exp"
    
_lr_action_items = {'$end':([0,1,2,3,4,18,19,21,27,87,],[-1,0,-14,-1,-16,-15,-21,-22,-23,-41,]),'INT':([0,3,19,21,27,28,37,46,60,78,85,87,],[11,11,-21,-22,-23,11,11,11,11,11,11,-41,]),'SHORT':([0,3,19,21,27,28,37,46,60,78,85,87,],[12,12,-21,-22,-23,12,12,12,12,12,12,-41,]),'CHAR':([0,3,19,21,27,28,37,46,60,78,85,87,],[13,13,-21,-22,-23,13,13,13,13,13,13,-41,]),'LONG':([0,3,19,21,27,28,37,46,60,78,85,87,],[14,14,-21,-22,-23,14,14,14,14,14,14,-41,]),'FLOAT':([0,3,19,21,27,28,37,46,60,78,85,87,],[15,15,-21,-22,-23,15,15,15,15,15,15,-41,]),'DOUBLE':([0,3,19,21,27,28,37,46,60,78,85,87,],[16,16,-21,-22,-23,16,16,16,16,16,16,-41,]),'STRUCT':([0,3,19,21,27,28,37,46,78,85,87,],[17,17,-21,-22,-23,17,17,17,17,17,-41,]),';':([5,6,8,9,10,11,12,13,14,15,16,22,23,24,28,30,31,33,34,35,39,40,41,42,43,44,49,52,54,57,58,61,62,63,64,65,66,70,71,78,80,81,83,84,87,89,90,111,112,113,114,117,118,119,120,121,123,125,126,127,128,129,130,131,132,133,135,137,140,144,145,146,147,148,150,151,152,154,155,156,157,],[19,21,-20,-24,-25,-8,-9,-10,-11,-12,-13,-34,-18,-31,-1,-27,-30,-19,-31,-34,-35,58,78,-54,-55,-57,-37,-32,58,90,-51,-50,-52,-69,-70,-71,-72,-78,-79,-1,-56,-59,-33,-36,-41,125,-49,-64,-63,-61,-82,-62,-65,-66,-53,-58,-26,-44,-73,-74,-75,-76,-77,-80,-81,-83,-85,-68,-87,-60,-84,152,-67,-86,58,58,-45,-46,-48,58,-47,]),',':([5,8,22,23,24,33,34,35,39,43,44,49,50,52,63,64,65,66,70,71,80,81,83,84,86,111,112,113,114,117,118,119,121,126,127,128,129,130,131,132,133,135,137,140,141,144,145,147,148,],[20,-20,-34,-18,-31,-19,-31,-34,-35,79,-57,-37,85,-32,-69,-70,-71,-72,-78,-79,-56,-59,-33,-36,-40,-64,-63,-61,-82,-62,-65,-66,-58,-73,-74,-75,-76,-77,-80,-81,-83,-85,-68,-87,149,-60,-84,-67,-86,]),'ID':([6,9,10,11,12,13,14,15,16,17,20,25,26,28,30,31,40,42,45,51,54,56,58,60,61,62,67,68,69,72,75,76,77,78,79,87,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,115,116,120,122,123,125,138,149,150,151,152,154,155,156,157,],[24,-24,-25,-8,-9,-10,-11,-12,-13,31,34,34,34,-1,-27,-30,63,-54,34,34,63,63,-51,63,-50,-52,63,63,63,63,63,63,63,-1,34,-41,-49,63,63,63,63,63,63,63,63,63,135,-2,-3,-4,-5,-6,-7,63,63,63,63,-53,63,-26,-44,63,63,63,63,-45,-46,-48,63,-47,]),'(':([6,9,10,11,12,13,14,15,16,20,24,25,26,28,30,31,34,40,42,45,51,54,56,58,59,60,61,62,63,67,68,69,72,73,74,75,76,77,78,79,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,123,125,138,149,150,151,152,154,155,156,157,],[25,-24,-25,-8,-9,-10,-11,-12,-13,25,37,25,25,-1,-27,-30,37,60,-54,25,25,60,60,-51,107,60,-50,-52,110,60,60,60,60,115,116,60,60,60,-1,25,-41,-49,60,60,60,60,60,60,60,60,60,-2,-3,-4,-5,-6,-7,60,60,60,60,-53,60,-26,-44,60,60,60,60,-45,-46,-48,60,-47,]),'*':([6,9,10,11,12,13,14,15,16,20,25,26,28,30,31,40,42,45,51,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,79,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,145,147,148,149,150,151,152,154,155,156,157,],[26,-24,-25,-8,-9,-10,-11,-12,-13,26,26,26,-1,-27,-30,69,-54,26,26,69,69,94,-51,69,-50,-52,-69,-70,-71,-72,69,69,69,-78,-79,69,69,69,69,-1,26,-41,94,-49,69,69,69,69,69,69,69,69,69,-2,-3,-4,-5,-6,-7,69,94,69,-64,-63,-61,94,69,69,94,94,94,-53,69,-26,-44,94,94,94,-76,-77,94,94,94,94,-85,94,-68,69,-87,94,94,94,94,-84,94,-86,69,69,69,-45,-46,-48,69,-47,]),'{':([7,17,22,28,29,31,32,40,42,49,54,58,61,62,78,84,87,90,120,125,150,151,152,154,155,156,157,],[28,-1,-17,-1,46,-28,-29,28,-54,-37,28,-51,-50,-52,-1,-36,-41,-49,-53,-44,28,28,-45,-46,-48,28,-47,]),')':([11,12,13,14,15,16,34,35,37,38,39,48,49,50,52,63,64,65,66,70,71,83,84,86,108,109,110,111,112,113,114,117,118,119,124,126,127,128,129,130,131,132,133,135,136,137,139,140,141,142,143,145,147,148,153,],[-8,-9,-10,-11,-12,-13,-31,-34,49,52,-35,84,-37,-39,-32,-69,-70,-71,-72,-78,-79,-33,-36,-40,137,138,140,-64,-63,-61,-82,-62,-65,-66,-38,-73,-74,-75,-76,-77,-80,-81,-83,-85,146,-68,148,-87,-89,150,151,-84,-67,-86,-88,]),'[':([22,23,24,33,34,35,38,39,49,52,57,63,64,65,66,70,71,81,83,84,86,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[-34,36,-31,36,-31,-34,36,-35,-37,-32,99,-69,-70,-71,-72,-78,-79,36,-33,-36,36,99,99,-64,-63,-61,99,99,99,99,99,-74,-75,-76,-77,99,99,99,99,-85,99,-68,-87,99,99,99,99,-84,99,-86,]),'RETURN':([28,40,42,54,58,61,62,78,87,90,120,125,150,151,152,154,155,156,157,],[-1,56,-54,56,-51,-50,-52,-1,-41,-49,-53,-44,56,56,-45,-46,-48,56,-47,]),'PRINT':([28,40,42,54,58,61,62,78,87,90,120,125,150,151,152,154,155,156,157,],[-1,59,-54,59,-51,-50,-52,-1,-41,-49,-53,-44,59,59,-45,-46,-48,59,-47,]),'NUMBER':([28,36,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,47,64,-54,64,64,-51,64,-50,-52,64,64,64,64,64,64,64,-1,-41,-49,64,64,64,64,64,64,64,64,64,-2,-3,-4,-5,-6,-7,64,64,64,64,-53,64,-44,64,64,64,64,-45,-46,-48,64,-47,]),'DECIMAL':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,65,-54,65,65,-51,65,-50,-52,65,65,65,65,65,65,65,-1,-41,-49,65,65,65,65,65,65,65,65,65,-2,-3,-4,-5,-6,-7,65,65,65,65,-53,65,-44,65,65,65,65,-45,-46,-48,65,-47,]),'STRINGLITERAL':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,66,-54,66,66,-51,66,-50,-52,66,66,66,66,66,66,66,-1,-41,-49,66,66,66,66,66,66,66,66,66,-2,-3,-4,-5,-6,-7,66,66,66,66,-53,66,-44,66,66,66,66,-45,-46,-48,66,-47,]),'!':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,72,-54,72,72,-51,72,-50,-52,72,72,72,72,72,72,72,-1,-41,-49,72,72,72,72,72,72,72,72,72,-2,-3,-4,-5,-6,-7,72,72,72,72,-53,72,-44,72,72,72,72,-45,-46,-48,72,-47,]),'IF':([28,40,42,54,58,61,62,78,87,90,120,125,150,151,152,154,155,156,157,],[-1,73,-54,73,-51,-50,-52,-1,-41,-49,-53,-44,73,73,-45,-46,-48,73,-47,]),'WHILE':([28,40,42,54,58,61,62,78,87,90,120,125,150,151,152,154,155,156,157,],[-1,74,-54,74,-51,-50,-52,-1,-41,-49,-53,-44,74,74,-45,-46,-48,74,-47,]),'&':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,75,-54,75,75,-51,75,-50,-52,75,75,75,75,75,75,75,-1,-41,-49,75,75,75,75,75,75,75,75,75,-2,-3,-4,-5,-6,-7,75,75,75,75,-53,75,-44,75,75,75,75,-45,-46,-48,75,-47,]),'-':([28,40,42,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,122,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,145,147,148,149,150,151,152,154,155,156,157,],[-1,68,-54,68,68,93,-51,68,-50,-52,-69,-70,-71,-72,68,68,68,-78,-79,68,68,68,68,-1,-41,93,-49,68,68,68,68,68,68,68,68,68,-2,-3,-4,-5,-6,-7,68,93,68,-64,-63,-61,93,68,68,93,93,93,-53,68,-44,93,-74,-75,-76,-77,93,93,93,93,-85,93,-68,68,-87,93,93,93,93,-84,93,-86,68,68,68,-45,-46,-48,68,-47,]),'+':([28,40,42,54,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,87,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,122,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,145,147,148,149,150,151,152,154,155,156,157,],[-1,67,-54,67,67,92,-51,67,-50,-52,-69,-70,-71,-72,67,67,67,-78,-79,67,67,67,67,-1,-41,92,-49,67,67,67,67,67,67,67,67,67,-2,-3,-4,-5,-6,-7,67,92,67,-64,-63,-61,92,67,67,92,92,92,-53,67,-44,92,-74,-75,-76,-77,92,92,92,92,-85,92,-68,67,-87,92,92,92,92,-84,92,-86,67,67,67,-45,-46,-48,67,-47,]),'PLUSSLF':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,76,-54,76,76,-51,76,-50,-52,76,76,76,76,76,76,76,-1,-41,-49,76,76,76,76,76,76,76,76,76,-2,-3,-4,-5,-6,-7,76,76,76,76,-53,76,-44,76,76,76,76,-45,-46,-48,76,-47,]),'SUBSLF':([28,40,42,54,56,58,60,61,62,67,68,69,72,75,76,77,78,87,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,115,116,120,122,125,138,149,150,151,152,154,155,156,157,],[-1,77,-54,77,77,-51,77,-50,-52,77,77,77,77,77,77,77,-1,-41,-49,77,77,77,77,77,77,77,77,77,-2,-3,-4,-5,-6,-7,77,77,77,77,-53,77,-44,77,77,77,77,-45,-46,-48,77,-47,]),'}':([28,40,42,46,53,54,55,58,61,62,78,82,87,88,90,120,125,152,154,155,157,],[-1,-1,-54,-1,87,-1,-43,-51,-50,-52,-1,123,-41,-42,-49,-53,-44,-45,-46,-48,-47,]),'=':([34,35,39,49,52,57,63,64,65,66,70,71,81,83,84,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[-31,-34,-35,-37,-32,91,-69,-70,-71,-72,-78,-79,122,-33,-36,91,91,-64,-63,-61,91,91,91,91,91,-74,-75,-76,-77,91,91,91,91,-85,91,-68,-87,91,91,91,91,-84,91,-86,]),']':([47,63,64,65,66,70,71,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,137,140,145,147,148,],[83,-69,-70,-71,-72,-78,-79,-64,-63,-61,-82,-62,-65,-66,-73,-74,-75,-76,-77,-80,-81,-83,145,-85,-68,-87,-84,-67,-86,]),'/':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[95,-69,-70,-71,-72,-78,-79,95,95,-64,-63,-61,95,95,95,95,95,95,95,-76,-77,95,95,95,95,-85,95,-68,-87,95,95,95,95,-84,95,-86,]),'BOOLAND':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[96,-69,-70,-71,-72,-78,-79,96,96,-64,-63,-61,96,96,96,96,96,-74,-75,-76,-77,96,96,96,96,-85,96,-68,-87,96,96,96,96,-84,96,-86,]),'BOOLOR':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[97,-69,-70,-71,-72,-78,-79,97,97,-64,-63,-61,97,97,97,97,97,-74,-75,-76,-77,97,97,97,97,-85,97,-68,-87,97,97,97,97,-84,97,-86,]),'.':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[100,-69,-70,-71,-72,-78,-79,100,100,-64,-63,-61,100,100,100,100,100,-74,-75,-76,-77,100,100,100,100,-85,100,-68,-87,100,100,100,100,-84,100,-86,]),'>':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[101,-69,-70,-71,-72,-78,-79,101,101,-64,-63,-61,101,101,101,101,101,-74,-75,-76,-77,101,101,101,101,-85,101,-68,-87,101,101,101,101,-84,101,-86,]),'<':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[102,-69,-70,-71,-72,-78,-79,102,102,-64,-63,-61,102,102,102,102,102,-74,-75,-76,-77,102,102,102,102,-85,102,-68,-87,102,102,102,102,-84,102,-86,]),'GRTREQL':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[103,-69,-70,-71,-72,-78,-79,103,103,-64,-63,-61,103,103,103,103,103,-74,-75,-76,-77,103,103,103,103,-85,103,-68,-87,103,103,103,103,-84,103,-86,]),'LESSEQL':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[104,-69,-70,-71,-72,-78,-79,104,104,-64,-63,-61,104,104,104,104,104,-74,-75,-76,-77,104,104,104,104,-85,104,-68,-87,104,104,104,104,-84,104,-86,]),'EQUAL':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[105,-69,-70,-71,-72,-78,-79,105,105,-64,-63,-61,105,105,105,105,105,-74,-75,-76,-77,105,105,105,105,-85,105,-68,-87,105,105,105,105,-84,105,-86,]),'NEQUAL':([57,63,64,65,66,70,71,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,140,141,142,143,144,145,147,148,],[106,-69,-70,-71,-72,-78,-79,106,106,-64,-63,-61,106,106,106,106,106,-74,-75,-76,-77,106,106,106,106,-85,106,-68,-87,106,106,106,106,-84,106,-86,]),'ELSE':([58,61,62,87,90,125,152,154,155,157,],[-51,-50,-52,-41,-49,-44,-45,156,-48,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'ExtDefList':([0,3,],[2,18,]),'ExtDef':([0,3,],[3,3,]),'EMPTY':([0,3,17,28,40,46,54,78,],[4,4,32,42,55,42,55,42,]),'ExtDecList':([0,3,],[5,5,]),'Specifier':([0,3,28,37,46,78,85,],[6,6,45,51,45,45,51,]),'FunHead':([0,3,],[7,7,]),'ExtDecHead':([0,3,],[8,8,]),'TYPE':([0,3,28,37,46,60,78,85,],[9,9,9,9,9,109,9,9,]),'StructSpecifier':([0,3,28,37,46,78,85,],[10,10,10,10,10,10,10,]),'FunDec':([6,20,25,26,45,51,79,],[22,35,35,35,35,35,35,]),'VarDec':([6,20,25,26,45,51,79,],[23,33,38,39,81,86,81,]),'CompSt':([7,40,54,150,151,156,],[27,61,61,61,61,61,]),'OptTag':([17,],[29,]),'Tag':([17,],[30,]),'DefList':([28,46,78,],[40,82,120,]),'Def':([28,46,78,],[41,41,41,]),'DecList':([28,46,78,],[43,43,43,]),'DecHead':([28,46,78,],[44,44,44,]),'VarList':([37,85,],[48,124,]),'ParamDec':([37,85,],[50,50,]),'StmtList':([40,54,],[53,88,]),'Stmt':([40,54,150,151,156,],[54,54,154,155,157,]),'Exp':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,110,115,116,122,138,149,150,151,156,],[57,57,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,136,141,142,143,144,147,141,57,57,57,]),'FlowCtrl':([40,54,150,151,156,],[62,62,62,62,62,]),'FuncCall':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,110,115,116,122,138,149,150,151,156,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'PrefixedExp':([40,54,56,60,67,68,69,72,75,76,77,91,92,93,94,95,96,97,98,99,107,110,115,116,122,138,149,150,151,156,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'Dec':([45,79,],[80,121,]),'RELOP':([57,89,108,111,112,113,114,117,118,119,126,127,128,129,130,131,132,133,134,136,141,142,143,144,147,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'Args':([110,149,],[139,153,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','yacc.py',16),
  ('RELOP -> >','RELOP',1,'p_relop','yacc.py',20),
  ('RELOP -> <','RELOP',1,'p_relop','yacc.py',21),
  ('RELOP -> GRTREQL','RELOP',1,'p_relop','yacc.py',22),
  ('RELOP -> LESSEQL','RELOP',1,'p_relop','yacc.py',23),
  ('RELOP -> EQUAL','RELOP',1,'p_relop','yacc.py',24),
  ('RELOP -> NEQUAL','RELOP',1,'p_relop','yacc.py',25),
  ('TYPE -> INT','TYPE',1,'p_type','yacc.py',29),
  ('TYPE -> SHORT','TYPE',1,'p_type','yacc.py',30),
  ('TYPE -> CHAR','TYPE',1,'p_type','yacc.py',31),
  ('TYPE -> LONG','TYPE',1,'p_type','yacc.py',32),
  ('TYPE -> FLOAT','TYPE',1,'p_type','yacc.py',33),
  ('TYPE -> DOUBLE','TYPE',1,'p_type','yacc.py',34),
  ('Program -> ExtDefList','Program',1,'p_Program','yacc.py',38),
  ('ExtDefList -> ExtDef ExtDefList','ExtDefList',2,'p_ExtDefList','yacc.py',44),
  ('ExtDefList -> EMPTY','ExtDefList',1,'p_ExtDefList','yacc.py',45),
  ('FunHead -> Specifier FunDec','FunHead',2,'p_FunHead','yacc.py',53),
  ('ExtDecHead -> Specifier VarDec','ExtDecHead',2,'p_ExtDecHead','yacc.py',58),
  ('ExtDecList -> ExtDecList , VarDec','ExtDecList',3,'p_ExtDecList','yacc.py',68),
  ('ExtDecList -> ExtDecHead','ExtDecList',1,'p_ExtDecList','yacc.py',69),
  ('ExtDef -> ExtDecList ;','ExtDef',2,'p_ExtDef_ExtDecList','yacc.py',82),
  ('ExtDef -> Specifier ;','ExtDef',2,'p_ExtDef_Specifier','yacc.py',87),
  ('ExtDef -> FunHead CompSt','ExtDef',2,'p_ExtDef_FunDef','yacc.py',92),
  ('Specifier -> TYPE','Specifier',1,'p_Specifier','yacc.py',97),
  ('Specifier -> StructSpecifier','Specifier',1,'p_Specifier','yacc.py',98),
  ('StructSpecifier -> STRUCT OptTag { DefList }','StructSpecifier',5,'p_StructSpecifier','yacc.py',103),
  ('StructSpecifier -> STRUCT Tag','StructSpecifier',2,'p_StructSpecifier','yacc.py',104),
  ('OptTag -> ID','OptTag',1,'p_OptTag','yacc.py',112),
  ('OptTag -> EMPTY','OptTag',1,'p_OptTag','yacc.py',113),
  ('Tag -> ID','Tag',1,'p_Tag','yacc.py',118),
  ('VarDec -> ID','VarDec',1,'p_VarDec','yacc.py',123),
  ('VarDec -> ( VarDec )','VarDec',3,'p_VarDec','yacc.py',124),
  ('VarDec -> VarDec [ NUMBER ]','VarDec',4,'p_VarDec','yacc.py',125),
  ('VarDec -> FunDec','VarDec',1,'p_VarDec','yacc.py',126),
  ('VarDec -> * VarDec','VarDec',2,'p_VarDec_pointer','yacc.py',135),
  ('FunDec -> ID ( VarList )','FunDec',4,'p_FunDec','yacc.py',139),
  ('FunDec -> ID ( )','FunDec',3,'p_FunDec','yacc.py',140),
  ('VarList -> ParamDec , VarList','VarList',3,'p_VarList','yacc.py',148),
  ('VarList -> ParamDec','VarList',1,'p_VarList','yacc.py',149),
  ('ParamDec -> Specifier VarDec','ParamDec',2,'p_ParamDec','yacc.py',157),
  ('CompSt -> { DefList StmtList }','CompSt',4,'p_CompSt','yacc.py',162),
  ('StmtList -> Stmt StmtList','StmtList',2,'p_StmtList','yacc.py',167),
  ('StmtList -> EMPTY','StmtList',1,'p_StmtList','yacc.py',168),
  ('Stmt -> RETURN Exp ;','Stmt',3,'p_Stmt_return','yacc.py',176),
  ('Stmt -> PRINT ( Exp ) ;','Stmt',5,'p_Stmt_print','yacc.py',180),
  ('FlowCtrl -> IF ( Exp ) Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',184),
  ('FlowCtrl -> IF ( Exp ) Stmt ELSE Stmt','FlowCtrl',7,'p_FlowCtrl','yacc.py',185),
  ('FlowCtrl -> WHILE ( Exp ) Stmt','FlowCtrl',5,'p_FlowCtrl','yacc.py',186),
  ('Stmt -> Exp ;','Stmt',2,'p_Stmt','yacc.py',197),
  ('Stmt -> CompSt','Stmt',1,'p_Stmt','yacc.py',198),
  ('Stmt -> ;','Stmt',1,'p_Stmt','yacc.py',199),
  ('Stmt -> FlowCtrl','Stmt',1,'p_Stmt','yacc.py',200),
  ('DefList -> Def ; DefList','DefList',3,'p_DefList','yacc.py',204),
  ('DefList -> EMPTY','DefList',1,'p_DefList','yacc.py',205),
  ('Def -> DecList','Def',1,'p_Def','yacc.py',213),
  ('DecHead -> Specifier Dec','DecHead',2,'p_DecHead','yacc.py',218),
  ('DecList -> DecHead','DecList',1,'p_DecList','yacc.py',223),
  ('DecList -> DecList , Dec','DecList',3,'p_DecList','yacc.py',224),
  ('Dec -> VarDec','Dec',1,'p_Dec','yacc.py',232),
  ('Dec -> VarDec = Exp','Dec',3,'p_Dec','yacc.py',233),
  ('PrefixedExp -> * Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',241),
  ('PrefixedExp -> & Exp','PrefixedExp',2,'p_PrefixedExp_Mem','yacc.py',242),
  ('PrefixedExp -> - Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',246),
  ('PrefixedExp -> + Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',247),
  ('PrefixedExp -> PLUSSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',248),
  ('PrefixedExp -> SUBSLF Exp','PrefixedExp',2,'p_PrefixedExp','yacc.py',249),
  ('PrefixedExp -> ( TYPE ) Exp','PrefixedExp',4,'p_PrefixedExp','yacc.py',250),
  ('Exp -> ( Exp )','Exp',3,'p_Exp_par','yacc.py',258),
  ('Exp -> ID','Exp',1,'p_Exp_Id','yacc.py',263),
  ('Exp -> NUMBER','Exp',1,'p_Exp_Number','yacc.py',267),
  ('Exp -> DECIMAL','Exp',1,'p_Exp_Constant','yacc.py',272),
  ('Exp -> STRINGLITERAL','Exp',1,'p_Exp_Constant','yacc.py',273),
  ('Exp -> Exp = Exp','Exp',3,'p_Exp','yacc.py',279),
  ('Exp -> Exp + Exp','Exp',3,'p_Exp','yacc.py',280),
  ('Exp -> Exp - Exp','Exp',3,'p_Exp','yacc.py',281),
  ('Exp -> Exp * Exp','Exp',3,'p_Exp','yacc.py',282),
  ('Exp -> Exp / Exp','Exp',3,'p_Exp','yacc.py',283),
  ('Exp -> FuncCall','Exp',1,'p_Exp','yacc.py',284),
  ('Exp -> PrefixedExp','Exp',1,'p_Exp','yacc.py',285),
  ('Exp -> Exp BOOLAND Exp','Exp',3,'p_Exp_Logic','yacc.py',292),
  ('Exp -> Exp BOOLOR Exp','Exp',3,'p_Exp_Logic','yacc.py',293),
  ('Exp -> ! Exp','Exp',2,'p_Exp_Logic','yacc.py',294),
  ('Exp -> Exp RELOP Exp','Exp',3,'p_Exp_Relop','yacc.py',301),
  ('Exp -> Exp [ Exp ]','Exp',4,'p_Exp_Mem','yacc.py',306),
  ('Exp -> Exp . ID','Exp',3,'p_Exp_Mem','yacc.py',307),
  ('FuncCall -> ID ( Args )','FuncCall',4,'p_FuncCall','yacc.py',315),
  ('FuncCall -> ID ( )','FuncCall',3,'p_FuncCall','yacc.py',316),
  ('Args -> Exp , Args','Args',3,'p_Args','yacc.py',324),
  ('Args -> Exp','Args',1,'p_Args','yacc.py',325),
]
