# Make Me A Video Game!

# I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

# What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.

print('Welcome to Mad Libs. Mad Libs are a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story before reading aloud.\n')
    #source: https://en.wikipedia.org/wiki/Mad_Libs


def read(txt):
    """function for opening/reading madlib.txt"""
    with open(txt, 'r') as f:
        contents = f.read()
        print(contents)
        return contents 


read('asset/madlib.txt')


def list_of_words():
    with open('asset/madlib.txt') as template:
        content = template.read()
        word_list = []
        last_word = 0
        find_bracket = content.count('{')
        for items in range(find_bracket):
            first_word = content.find('{', last_word) + 1
            last_word = content.find('}', first_word)
            text = content[first_word : last_word]
            word_list.append(text)
    print(word_list)
list_of_words()




