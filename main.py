def counter(text):
    print(len(text.split()))

def word_count(text):
    new_dict = {}
    for t in text.lower():
        if t in new_dict.keys():
            new_dict[t] += 1
        else:
            new_dict[t] = 1
    return new_dict
    
    
def sort_on(dict):
    return dict["num"]
    
    
    
def report_generate(word_dict):
    for k, v in word_dict.items():
        print(f"The {k} character was found {v} times")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        counter(file_contents)
        print(word_count(file_contents))
        report_generate(word_count(file_contents))
        



main()
