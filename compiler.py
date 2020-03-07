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

    tokens = create_tokens()
    regex = merge_tokens(tokens)

    tags = re.findall(regex, content)
    print("Tokenized code:", tags)

    return tags


class Token:
    def __init__(self, name, regexp):
        self.name = name
        self.regexp = regexp

def create_tokens():
    tokens = []

    # open brace
    tokens.append(Token("OPEN_BRACE", "{"))

    # close brace
    tokens.append(Token("CLOSE_BRACE", "}"))

    # open parenthesis
    tokens.append(Token("OPEN_PARENTHESIS", "\("))

    # close parenthesis
    tokens.append(Token("CLOSE_PARENTHESIS", "\)"))

    # semicolon
    tokens.append(Token("SEMICOLON", ";"))

    # int keyword
    tokens.append(Token("INT", "int"))

    # return keyword
    tokens.append(Token("RETURN", "return"))

    # identifier
    tokens.append(Token("IDENTIFIER", "[a-zA-Z]\w*"))

    # integer literal
    tokens.append(Token("INTEGER_LITERAL", "[0-9]+"))
    
    return tokens


# creates regular expression from all individiual tokens' regular expressions
def merge_tokens(tokens):
    result = ""
    
    for t in tokens:
        result += t.regexp + '|'

    return result[:-1]

if __name__ == '__main__':
    main()

