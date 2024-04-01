file_path = "NS.txt"  # Replace 'example.txt' with your file path
n = 1  # Number of lines to read

try:
    A = open(file_path, 'r') 
    lines = []
    for i in range(n):
        line = A.readline()
        if line:
            lines.append(line)
        else:
            break
    
    print(f"First {len(lines)} lines of the file:")
    for line in lines:
        print(line, end='')
        
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
