# Write a generator function read_file_lines(file_path) that reads a file line by line and yields each line.
# Use this generator to print each line of a file without loading the entire file into memory.
def read_files_lines(file_path):
    fs=open(file_path,mode="r")
    for i in fs:
        yield i
    fs.close()

read=read_files_lines("peterrabbitcopy.txt")
for i in range(13):
    print(next(read))