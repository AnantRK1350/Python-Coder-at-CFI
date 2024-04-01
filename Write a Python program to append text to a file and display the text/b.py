file_path = "NS.txt"  


text_to_append = " WELCOME TO THE WORLD OF FILE HANDLING.\n "

try:
    A= open(file_path, 'a') 
    A.write(text_to_append)
    
    
    A= open(file_path, 'r') 
    appended_text = A.read()
    print("Appended text:")
    print(appended_text)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
