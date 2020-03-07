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
    token_strings = re.findall(merge_regexps(token_types), content)

    tokens = []

    # for each token string, find it's corresponding token type, 
    # create Token object from it and put that object in tokens list
    for string in token_strings:
        for t in token_types:
            if re.fullmatch(t.pattern, string) != None:
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


def get_ast(token_iterator):
    return None


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
    token_types.append(TokenType("INT", "int"))

    # return keyword
    token_types.append(TokenType("RETURN", "return"))

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

