import re 
import sys



def main():
    try:
        to_compile = sys.argv[1]
    except IndexError:
        print("Error: No file is given to compile.\nExample: python3 lexer.py to_compile.c\nExiting...")
        exit()

    print("Compiling", sys.argv[1])

    lex(to_compile)

def lex(to_compile):
    with open(to_compile, 'r') as f:
        content = f.read()

    regex = "{|}|\(|\)|;|int|return|[a-zA-Z]\w*|[0-9]+"
    tags = re.findall(regex, content)
    
    print("Tokenized code:", tags)
    return tags

if __name__ == '__main__':
    main()
