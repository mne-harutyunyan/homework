#task1
#ap= open("append_mode.txt", mode = "a")
#ap.write("Hello world")
#ap.close()

#task2
#fs = open("exclusive_mode.txt", mode = "x")
#fs.write("Hello")
#fs.close()

#task3
#mn = open("specific_position.txt", mode = "w")
#mn.write("Hello python")
#mn.close()
#fs2 = open("specific_position.txt", mode = "r+")
#fs2.read()
#fs2.seek(6)
#fs2.write("World ")
#fs2.close()


#task4
example = "example"
all = "all"
word = "word"
up = "up"
did = "did"
him = "him"

rb = open("peterrabbit.txt")
rb1 = rb.readlines()
count_example = 0
count_all = 0
count_word = 0
count_up = 0
count_did = 0
count_him = 0

for line in rb1:
    if example in line:
        count_example = count_example + 1
    if all in line:
        count_all = count_all + 1
    if word in line:
        count_word = count_word + 1
    if up in line:
        count_up = count_up + 1
    if did in line:
        count_did = count_did + 1
    if him in line:
        count_him = count_him + 1

print(f' example - {count_example}')
print(f' all - {count_all}')
print(f' word - {count_word}')
print(f' up - {count_up}')
print(f' did - {count_did}')
print(f' him - {count_him}')

