import re 
import sys



def main():
    try:
        to_compile = sys.argv[1]
    except IndexError:
        print("Error: No file is given to compile.\nExample: python3 compiler.py to_compile.c\nExiting...")
        exit()

    print("Compiling", to_compile)

    lex(to_compile)


def lex(to_compile):
    with open(to_compile, 'r') as f:
        content = f.read()

    tts = create_token_types()
    regex = merge_regexps(tts)

    tags = re.findall(regex, content)
    print("Tokenized code:", tags)

    return tags


class TokenType:
    def __init__(self, name, regexp):
        self.name = name
        self.regexp = regexp


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

