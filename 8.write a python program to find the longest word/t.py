file_path = "NS.txt" 

try:
    t= open(file_path, 'r') 
    longest_word = ""
    for line in t:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
    
    if longest_word:
        print(f"The longest word in the file is: {longest_word}")
    else:
        print("The file is empty.")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
