import re

# Define the categories of lexemes
keywords = {'if', 'else', 'while', 'for', 'do', 'int', 'float', 'double', 
            'char', 'void', 'boolean', 'true', 'false', 'return', 'class', 
            'public', 'private', 'protected', 'static', 'final', 'try', 
            'catch', 'throw', 'interface'}

operators = {'+', '-', '*', '/', '%', '=', '+=', '-=', '*=', '/=', '==', 
             '!=', '<', '>', '<=', '>=', '++', '--', '&&'}

punctuators = {'{', '}', '[', ']', '(', ')', ',', ';', ':', '.'}

def is_identifier(token):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) is not None

def is_literal(token):
    return re.match(r'^\d+$', token) or re.match(r'^\d+\.\d+$', token) or re.match(r'^".*"$', token)

def lexical_analysis(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Remove the sentinel value
        content = content.replace('$', '')

        # Tokenize the content using regex
        tokens = re.findall(r'\w+|[^\w\s]', content, re.UNICODE)

        for token in tokens:
            if token in keywords:
                print(f"Lexeme (Keyword): {token}")
            elif is_identifier(token):
                print(f"Lexeme (Identifier): {token}")
            elif token in operators:
                print(f"Lexeme (Operator): {token}")
            elif token in punctuators:
                print(f"Lexeme (Punctuator): {token}")
            elif is_literal(token):
                print(f"Lexeme (Literal): {token}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def main():
    input_file = input("Enter the output file name from Task 2 (e.g., out2.txt): ")
    lexical_analysis(input_file)

if __name__ == "__main__":
    main()