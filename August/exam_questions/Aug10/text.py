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
    return f"words count is: {words},\ncharacters count is: {characters},\nlines count is: {lines}."
print(text_calculator("peterrabbitcopy.txt"))

