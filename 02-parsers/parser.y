%skeleton "lalr1.cc"
%require "3.5"

%defines
%define api.token.constructor
%define api.value.type variant
%define parse.assert

%code requires {
    #include <string>
    class Scanner;
    class Driver;
}

// %param { Driver &drv }

%define parse.trace
%define parse.error verbose

%code {
    #include "driver.hh"
    #include "location.hh"

    static yy::parser::symbol_type yylex(Scanner &scanner, Driver& driver) {
        return scanner.ScanToken();
    }
}

%lex-param { Scanner &scanner }
%lex-param { Driver &driver }
%parse-param { Scanner &scanner }
%parse-param { Driver &driver }

%locations

%define api.token.prefix {TOK_}

%token
// Unable to classify :)
    END 0 "end of file"
    SEMICOLON ";"

// Brackets
    LPAREN "("
    RPAREN ")"
    LBRACE "{"
    RBRACE "}"
    LBRACKET "["
    RBRACKET "]"

// Operators
    op_member 	"."
    op_assign 	"="
    op_sub	"-"
    op_add 	"+"
    op_mul	"*"
    op_div 	"/"
    op_inv	"!"

// Keywords
    kw_class 	"class"
    kw_public 	"public"
    kw_static 	"static"
    kw_void 	"void"
    kw_main 	"main"
    kw_System 	"System"
    kw_out 	"out"
    kw_println	"println"
    kw_new	"new"
    kw_length   "length"
    kw_true	"true"
    kw_false	"false"
    kw_return	"return"
    kw_if	"if"
    kw_else	"else"
    kw_while	"while"

// Types
    t_int	"int"
    t_boolean	"boolean"
;

%token <std::string> IDENTIFIER "identifier"
%token <int> NUMBER "number"
%nterm <int> expression
%nterm <int*> lvalue;

%printer { yyo << $$; } <*>;

%%
%start program;
program: main_class

main_class:
    "class" "identifier" "{" "public" "static" "void" "main" "(" ")" "{" statements "}" "}"

statements:
    %empty {}
    | statements statement {};

statement:
    open_statement
    | closed_statement

open_statement:
    "if" "(" expression ")" statement
    | "if" "(" expression ")" closed_statement "else" open_statement
    | loop_header open_statement

closed_statement:
    simple_statement
    | "if" "(" expression ")" closed_statement "else" closed_statement
    | loop_header closed_statement

loop_header:
    "while" "(" expression ")"

simple_statement:
    "System" "." "out" "." "println" "(" expression ")" ";" { std::cout << $7 << std::endl; }
    | local_var_decl
    | lvalue "=" expression ";" { *($1) = $3; };
    | "return" expression ";" { driver.result = $2; }
    | "{" statements "}" {};

// Set the precedence for binary ops
%left "+" "-";
%left "*" "/";
%left "!";

expression:
    "number"
    | "identifier" { $$ = driver.variables[$1]; }
    | expression "+" expression { $$ = $1 + $3; }
    | expression "-" expression { $$ = $1 - $3; }
    | expression "*" expression { $$ = $1 * $3; }
    | expression "/" expression { $$ = $1 / $3; }

    | "!" expression { $$ = !($2); }

    | "true"  { $$ = 1; }
    | "false" { $$ = 0; }

    | "(" expression ")" { $$ = $2; };

type:
    simple_type

simple_type:
    "int"
    | "boolean";

var_decl:
    type "identifier" ";" { driver.variables[$2] = 0; };

local_var_decl:
    var_decl;

lvalue:
    "identifier" { $$ = &driver.variables[$1]; };
%%

void
yy::parser::error(const location_type& l, const std::string& m)
{
  std::cerr << l << ": " << m << '\n';
}
