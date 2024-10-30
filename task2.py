def process_file(input_file):
    buffer = []
    
    try:
        with open(input_file, 'r') as file:
            while True:
                char = file.read(1)  # Read one character at a time
                if not char:  # If we reach the end of the file
                    break
                if char != '\n':  # Ignore newline characters
                    buffer.append(char)  # Add character to buffer

        # Add sentinel value at the end
        buffer.append('$')

        # Write the buffer to out2.txt
        with open('out2.txt', 'w') as file:
            file.write(''.join(buffer))

        # Display the contents of out2.txt
        print("\nContents of out2.txt:")
        print("----------------------")
        with open('out2.txt', 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def main():
    input_file = input("Enter the output file name from Task 1 (e.g., out1.txt): ")
    process_file(input_file)

if __name__ == "__main__":
    main()