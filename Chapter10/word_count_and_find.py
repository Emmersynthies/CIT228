def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def count_common_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as n:
            contents = n.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        
        msg = f"'{word}' is in {filename} about {word_count} times."
        print(msg)
def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass  
    else:    
        searchWord = contents.count(searchWord)
        print("What is your word?\n")

filenames = ['Chapter10/harryPotter.txt', 'Chapter10/percyJackson.txt', 'Chapter10/catAndTheHat.txt']
searchWord=input("What common word would you like to search for within the files? ")  
for filename in filenames:
    count_words(filename)
    find_words(filename,searchWord)
    