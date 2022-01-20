import sys
import time

from create_dictionary import dictionary_creation




NodeCount = 0               #to keep count of nodes created in trie

WordCount = 0               #to keep count of words inserted in trie

MAX_COST = 2



# The Trie data structure keeps a set of words, organized with one node for
# each letter. Each node has a branch for each letter that may follow it in the
# set of words.

class TrieNode:
    
    def __init__(self):
        self.word = None
        self.children = {}

        global NodeCount
        NodeCount += 1

    def insert_word( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word


#read dictionary file into a trie
def create_trie(dict):

    trie = TrieNode()
    global WordCount

    for word in dict:

        WordCount += 1
        trie.insert_word(word)
    
    return trie



# The search function returns a list of all words that are less than the given
# maximum distance from the target word
def search(trie, string, max_cost):

    current_row = range(len(string) + 1)
    results = set()

    for char in trie.children:
        search_recursive(trie.children[char],char, char, None, string, current_row, None, results, max_cost)
    
    return results

# This recursive helper is used by the search function above. It assumes that
# the previousRow has been filled in already.
def search_recursive(node, prefix, char, prev_char, string, previous_row, pre_previous_row, results, max_cost):

    columns = len(string) + 1
    current_row = [previous_row[0] + 1]

    for column in range(1, columns):

        insert_cost = previous_row[column] + 1
        delete_cost = current_row[column - 1] + 1

        if string[column - 1] != char:
          replace_cost = previous_row[column - 1] + 1
        else:                
          replace_cost = previous_row[column - 1]

        current_row.append(min(insert_cost, delete_cost, replace_cost))
        if prev_char and column - 1 > 0 and char == string[column-2] and prev_char == string[column-1] and string[column-1] != char:
            current_row[column] = min(current_row[column], pre_previous_row[column-2] + 1)

    if current_row[-1] <= max_cost and node.word != None:
        results.add((prefix, current_row[-1]))

    if min(current_row) <= max_cost:
        prev_char = char
        # max_calc = max_cost if self.max_calc_flag else None
        for char in node.children: #self.edges(self.dictionary, prefix, self.chars, max_calc):
            search_recursive( node.children[char], prefix + char, char, prev_char, string, current_row, previous_row, results, max_cost)




def spell_checker():

    #create dictionary from corpus document
    dictionary_creation()

    print(" ★ Reading dictionary .......")

    print()

    #read dictionary from file
    with open("dictionary.txt","r") as file:
        words = file.readlines()
    
    #list representation of dictionary
    dict = []

    for word in words:
        dict.append(word.rstrip())


    trie = create_trie(dict)

    print(" ★ Enter the input word :: ",end='')
    input_wrd = input()

    print()
    
    results = search(trie, input_wrd, MAX_COST )

    results = list(results)

    results.sort(key = lambda x: x[1])

    d = int(results[0][1])

    if d == 0:

        print(" ★ Word is found in the dictionary ") 
    
    else :

        print(" ★ Sorry we didn't found the word in the dictionary, Did you mean :: ")
        
        print()

        for suggs in results[:5]:

                print(f" ➼ {suggs[0]}")
                print()

    print("---------------------------------------------------------")


spell_checker()

    

