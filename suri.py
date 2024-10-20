#find the first non-repeating character in a string
def count_of_letters(letter,word):
    count = 0
    for i in word :
        if i == letter :
            count += 1 
    return count
            
def find_first_Non_Repeating_Character(word):
    for letter  in word :
        letter_count = count_of_letters(letter,word)
        if letter_count == 1 :
            print(letter)
            break
        
word = input()
find_first_Non_Repeating_Character(word)
