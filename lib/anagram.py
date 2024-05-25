# your code goes here!
my_list = ['enlists', 'google', 'inlets', 'banana']
class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        self._word = word


    def match(self, word):
        matching_words = []
        split_word = list(word)
        split_word.sort()
        print(split_word)

        for list_word in my_list:
            split_list_word = list(list_word)
            split_list_word.sort()
            print(split_list_word)
        
            if split_word == split_list_word:
                matching_words.append(list_word)

        return matching_words

listen = Anagram("listen")
print(listen.match("listen"))

silent = Anagram("silent")
print(silent.match("listen"))
  


