file_path = "NS.txt"  
n = 5  

try:
    d= open(file_path, 'r') 
    all_lines = d.readlines()
        
    last_n_lines = all_lines[-n:]
    
    print(f"Last {n} lines of the file:")
    for line in last_n_lines:
        print(line, end='')

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
