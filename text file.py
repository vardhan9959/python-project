def count_words(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.read().split())
    except FileNotFoundError:
        return -1
filename = 'sample.txt'
word_count = count_words(filename)
if word_count != -1:
    print(f"Number of words in '{filename}': {word_count}")
else:
    print("File Not found!")
