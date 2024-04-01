file_path = "NS.txt"

try:
    file_content = ""
    d= open(file_path, 'r')
    for line in d:
        file_content += line
    
    print("File content stored in a variable:")
    print(file_content)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
