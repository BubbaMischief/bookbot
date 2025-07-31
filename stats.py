def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(words):
    count = 0
    separate = words.split()
    for sep in separate:
        count += 1
    return count

def characters(words):
    letters = {}
    for word in words:
        if word.lower() not in letters:
            letters[word.lower()] = 1
        else:
            letters[word.lower()] +=1

    return letters

def sorted_dictionary(dictionary):
    unsorted_list = []
    for letter in dictionary:
        char = letter
        num = dictionary[letter]
        if letter.isalpha() == True:
            unsorted_list.append({"char":char,"num":num})
        
       
    unsorted_list.sort(reverse=True,key=sort_on)
    return unsorted_list

def sort_on(each_dict):
    return each_dict["num"]