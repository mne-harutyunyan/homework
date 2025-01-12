# Write a function that reads a text file and counts the number of lines, words, 
# and characters in the file. Then, write these statistics to a new file.
def text_calculator(file):
    text = open(file)
    words = 0
    characters = 0
    lines = 0
    for line in text:
        lines+=1
        words = words+len(line.split())
        for character in line.split():
            characters += len(character)
    text.close()
    new_file = open("new_output.txt","w")
    new_file.write(f"lines are {lines},\nwords are {words},\ncharacters are {characters}.")
    new_file.close()
text_calculator("peterrabbitcopy.txt")

