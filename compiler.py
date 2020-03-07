import re 
import sys



def main():
    try:
        to_compile = sys.argv[1]
    except IndexError:
        print("Error: No file is given to compile.\nExample: python3 compiler.py to_compile.c\nExiting...")
        exit()

    print("Compiling", to_compile)

    get_ast(lex(to_compile))


def lex(to_compile):
    with open(to_compile, 'r') as f:
        content = f.read()
        # print("Actual code:")
        # print(content)

    token_types = create_token_types()
    keywords = ("INT", "RETURN");
    token_strings = re.findall(merge_regexps(token_types), content)

    tokens = []

    # for each token string, find it's corresponding token type, 
    # create Token object from it and put that object in tokens list
    for string in token_strings:
        for t in token_types:
            if re.fullmatch(t.pattern, string) != None:
                # if token is keyword (int, return, etc.) remove space from the end
                if t.name in keywords:
                    string = string[:-1]
                token = Token(string, t)
                tokens.append(token)
                break
            
    # print found tokens
    print("Tokenized code:")
    for t in tokens:
        print(t)

    # create iterator from tokens for easier parsing
    iterator = iter(tokens)

    return iterator


# returns abstract syntax tree (AST) after successfully processing tokens
def get_ast(tokens):
    tree = parse_program(tokens)
    print("Abstract Syntax Tree:")
    print(tree)
    return tree


# for now, program is just a function declaration
def parse_program(tokens):
    func = parse_function(tokens)
    node = Program(func)
    return node


def parse_function(tokens):
    ret_type = next(tokens)
    if ret_type.type.name not in ("INT"):
        print("Expected function return type")
        exit()

    name = next(tokens)
    if name.type.name != "IDENTIFIER":
        print("Expected function identifier")
        exit()
    
    t = next(tokens)
    if t.type.name != "OPEN_PARENTHESIS":
        print("Missing open parenthesis")
        exit()

    t = next(tokens)
    if t.type.name != "CLOSE_PARENTHESIS":
        print("Missing close parenthesis")
        exit()

    t = next(tokens)
    if t.type.name != "OPEN_BRACE":
        print("Missing open brace")
        exit()

    # for now, function body is just one statement
    statement = parse_statement(tokens)

    # create function node
    node = Function(ret_type.string, name.string, statement) 

    t = next(tokens)
    if t.type.name != "CLOSE_BRACE":
        print("Missing close brace")
        exit()

    return node


# for now, only statement available is return statement
def parse_statement(tokens):
    t = next(tokens)
    if t.type.name != "RETURN":
        print("Invalid return statement")
        exit()

    # for now, expression can only be integer literal
    expression = parse_expression(tokens)
    
    node = Return(expression)

    t = next(tokens)
    if t.type.name != "SEMICOLON":
        print("Missing semicolon")
        exit()

    return node


def parse_expression(tokens):
    integer = next(tokens)
    if integer.type.name != "INTEGER_LITERAL":
        print("Missing return value")
        exit()
    if int(integer.string) > 2147483647:
        print("Integer limit exceeded")
        exit()

    # for now, expression can only be integer literal
    node = Const(int(integer.string))

    return node


class Program:
    def __init__(self, function):
        self.function = function

    def __str__(self, depth=0):
        return "PROGRAM:\n" + self.function.__str__(depth + 1)


class Function:
    def __init__(self, ret_val, name, body):
        self.ret_val = ret_val
        self.name = name
        self.body = body 
    
    def __str__(self, depth=0):
        return ("\t" * depth) + "FUNCTION " + self.ret_val + " " + self.name + ":\n" + self.body.__str__(depth + 1)


class Return:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self, depth=0):
        return ("\t" * depth) + "RETURN " + self.expression.__str__(depth + 1)


class Const:
    def __init__(self, value):
        self.value = value

    def __str__(self, depth=0):
        return "CONST " + str(self.value)


class Token:
    def __init__(self, string, token_type):
        self.string = string
        self.type = token_type

    def __repr__(self):
        return "<" + '"' + self.string + '" | ' + 'TYPE: ' + self.type.name + ">"


class TokenType:
    def __init__(self, name, regexp):
        self.name = name
        self.regexp = regexp
        self.pattern = re.compile(regexp)


# WARNING: the most general regular expressions should be added last in token_types.
#          that's because keywords satisify identifier regexp too.
def create_token_types():
    token_types = []

    # open brace
    token_types.append(TokenType("OPEN_BRACE", "{"))

    # close brace
    token_types.append(TokenType("CLOSE_BRACE", "}"))

    # open parenthesis
    token_types.append(TokenType("OPEN_PARENTHESIS", "\("))

    # close parenthesis
    token_types.append(TokenType("CLOSE_PARENTHESIS", "\)"))

    # semicolon
    token_types.append(TokenType("SEMICOLON", ";"))

    # int keyword
    token_types.append(TokenType("INT", "int "))

    # return keyword
    token_types.append(TokenType("RETURN", "return "))

    # identifier
    token_types.append(TokenType("IDENTIFIER", "[a-zA-Z]\w*"))

    # integer literal
    token_types.append(TokenType("INTEGER_LITERAL", "[0-9]+"))
    
    return token_types


# creates regular expression from all individiual tokens' regular expressions
def merge_regexps(token_types):
    result = ""
    
    for t in token_types:
        result += t.regexp + '|'

    return result[:-1]


if __name__ == '__main__':
    main()

