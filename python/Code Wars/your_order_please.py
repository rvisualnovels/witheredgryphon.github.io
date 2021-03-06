'''
Your task is to sort a given string. 
Each word in the String will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. 
The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"
'''

def order(sentence):
    iter = 1
    sortedSentence = []
    sentence = sentence.split()
    while sentence:
        word = filter(lambda x: str(iter) in x, sentence)
        sentence.remove(word[0])
        sortedSentence.append(word[0])
        iter += 1
    sortedSentence = ' '.join(sortedSentence)
    return sortedSentence