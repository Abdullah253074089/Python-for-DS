def remove_blank_lines(lines):
    return [line for line in lines if line.strip()]

def remove_comments(lines):
    cleaned_lines = []
    for line in lines:
        # Remove single-line comments
        if '//' in line:
            line = line[:line.index('//')]
        # Remove multi-line comments
        if '/*' in line:
            line = line[:line.index('/*')]
        cleaned_lines.append(line)
    return cleaned_lines

def remove_extra_whitespace(lines):
    return [' '.join(line.split()) for line in lines]

def remove_imports_and_annotations(lines):
    return [line for line in lines if not (line.strip().startswith('import') or line.strip().startswith('@'))]

def main():
    input_file = input("Enter the source code file name: ")
    
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Process the lines
        lines = remove_blank_lines(lines)
        lines = remove_comments(lines)
        lines = remove_extra_whitespace(lines)
        lines = remove_imports_and_annotations(lines)
        
        # Write the cleaned lines to out1.txt
        with open('out1.txt', 'w') as file:
            file.writelines(lines)
        
        # Display the contents of out1.txt
        print("\nContents of out1.txt:")
        print("----------------------")
        with open('out1.txt', 'r') as file:
            print(file.read())
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    main()