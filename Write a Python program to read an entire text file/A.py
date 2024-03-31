try:
    F= open('NS.txt', 'r') 
    file_content = F.read()
    print("File content:")
    print(file_content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")