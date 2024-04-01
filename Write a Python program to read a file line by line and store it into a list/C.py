file_path = "NS.txt"  
try:
    lines = []
    C= open(file_path, 'r') 
    for line in C:
        lines.append(line.strip()) 
    
    print("Lines stored in the list:")
    for line in lines:
        print(line)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
