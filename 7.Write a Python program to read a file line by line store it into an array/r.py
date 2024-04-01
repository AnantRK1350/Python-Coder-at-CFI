file_path = "NS.txt"  

try:
    lines_array = []
    r= open(file_path, 'r') 
    for line in r:
        lines_array.append(line.strip())  
    
    print("File content stored in an array:")
    for line in lines_array:
        print(line)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
