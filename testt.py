 
def word_count2(text):
    new_dict = {}
    for t in text.lower():
        if t in new_dict.keys():
            new_dict[t] += 1
        else:
            new_dict[t] = 1
    return new_dict
    
def main():
    with open('github.com/erickale/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
        print(word_count2(file_contents))
        



main()