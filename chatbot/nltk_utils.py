import nltk
import numpy as np
nltk.download("punkt")
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer

stemmer = PorterStemmer() 
#what's difference with LancasterStemmer, -> LancasterStemmer가 더 성능 좋음

def tokenize(sentence: str) -> list:
    """
    this function return token
    
    ex.
    hello, world?
    -> ['hello', ',', 'world', '?']
    """

    return nltk.word_tokenize(sentence)


def stem(word: str) -> str:
    """
    make str original

    ex.
    playing -> play
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_word):
    """
    sentence = [ "hello", "who", "are", "you" ]
    words    = [ "hi", "hello", "I", "you", "bye" ]
    bag      = [    0,       1,   0,     1,     0 ]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_word), dtype = np.float32)
    for idx, w in enumerate(all_word):
        #enumerate : ( repeat times, data )
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag

def main() -> None:
    """
    this function tell what this module do
    """
    test_str = "this string is test string"
    print(test_str)
    test_token = tokenize(test_str)
    print("this is tokenized string", test_token)
    stemed_data = list(map(stem, test_token))
    print("this is stem ", stemed_data)
    
    all_word = sorted([ "hi", "hello", "I", "you", "bye", "is" ])
    vector = bag_of_words(stemed_data, all_word)
    print(vector)
    return None


if __name__ == '__main__':
    main()


"""
Bag of Words:단어들의 순서는 전혀 고려하지 않고, 
단어들의 출현 빈도(frequency)에만 집중하는 텍스트 데이터의 수치화 표현 방법

"""
