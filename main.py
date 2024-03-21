def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
    
    dict = count_letters(file_contents)
    alpha_count = sorted_letters(dict)

    print(f'--- Begin report of {book} ---')
    print(f'There are {count_words(file_contents)} words in this book.')
    for char in alpha_count:
        print(f"The '{char['letter']}' was found {char['count']} times.")
    print('--- End report ---')

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letters = {}
    for char in text:
        letters[char] = letters.get(char,0) + 1

    return letters

def sort_on(dict):
    return dict['count']

def sorted_letters(dict):
    letters_list = []
    for d in dict:
        if d.isalpha():
            letters_list.append({'letter':d, 'count':dict[d]})

    letters_list.sort(reverse=True,key=sort_on)
    return letters_list

main()