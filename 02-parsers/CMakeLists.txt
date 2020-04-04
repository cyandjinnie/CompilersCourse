project(ParserExample)
set(
    HEADERS
    ${ParserExample_SOURCE_DIR}/driver.hh
    ${ParserExample_SOURCE_DIR}/parser.hh
    )

BISON_TARGET(
    MyParser
    parser.y
    ${ParserExample_SOURCE_DIR}/parser.cpp
    DEFINES_FILE ${ParserExample_SOURCE_DIR}/parser.hh
)

FLEX_TARGET(
    MyScanner
    scanner.l
    ${ParserExample_SOURCE_DIR}/scanner.cpp
)

ADD_FLEX_BISON_DEPENDENCY(MyScanner MyParser)

add_executable(
    ParserExample
    main.cpp
    driver.cpp
    ${BISON_MyParser_OUTPUTS}
    ${FLEX_MyScanner_OUTPUTS}
        Program.h Expr/Expr.h BaseNode.h Expr/BinaryOp.cpp Expr/BinaryOp.h Visitor/Visitor.h Entity/Const.hpp Type/Type.h Entity/Entity.h Entity/Id.h Entity/Id.cpp Stmt/Stmt.h Stmt/Assign.cpp Stmt/Assign.h Stmt/Print.cpp Stmt/Print.h Stmt/VarDecl.cpp Stmt/VarDecl.h Expr/UnaryOp.h Stmt/Ret.cpp Stmt/Ret.h Stmt/List.cpp Stmt/List.h Expr/UnaryOp.cpp ast.h Expr/rvalue.cpp Expr/rvalue.h Expr/lvalue.cpp Expr/lvalue.h Stmt/Cond.cpp Stmt/Cond.h ast_decl.h Visitor/PrintAST.cpp Visitor/PrintAST.h)
target_include_directories(ParserExample PRIVATE ${ParserExample_SOURCE_DIR})



