import os
from pdb import line_prefix

def clean_data(line):
    
    #convert to lower case
    line = line.lower()
    
    #remove UFT-8 tab
    line = line.replace("\ufeff"," ")

    #remove punctuations
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~“”–'''
    
    for char in line:
        if char in punc:
            line = line.replace(char," ")
            line = line.rstrip()
            line = line.lstrip()
            
    return line


#remove empty tokens, '\n' , numeric values.
def filter_words(line):

    line = list(filter(lambda x: x != '', line))
    line = list(filter(lambda x: x != '\n', line))
    line = list(filter(lambda x: x.isnumeric() != True , line))
    
    return line


def dictionary_creation():

    dirname = os.getcwd()

    f_name = "document.txt"

    all_tokens = []

    lines = []

    filename = os.path.join(dirname, f_name)

    print("---------------------------------------------------------")

    print()

    print(" ★ Processing the document corpus .........")



    f = open(filename,encoding="utf-8",mode= "r")

    for line in f:

        x = clean_data(line)
        lines.append(x)


    for line in lines:

        line = line.split(" ")
        reformed_line = filter_words(line)

        for word in reformed_line:

            if word.find("――") == -1:

                all_tokens.append(word)


    unique_tokens = list(set(all_tokens))

    # Writing to file
    with open("dictionary.txt", "w") as file:
        # Writing data to a file
        for word in unique_tokens:
            file.write(word+"\n")

            
    print(f"\n ★ Created dictionary from corpus containing - {len(unique_tokens)} unique words")

    print()


