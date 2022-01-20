from create_dictionary import dictionary_creation

def editDistance(str1, str2):

    m = len(str1)
    n =len(str2)

    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):

        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j    

            elif j == 0:
                dp[i][j] = i    
            
            #same char no action needed
            elif str1[i-1] == str2[j-1]:
                
                dp[i][j] = dp[i-1][j-1]

            else:
                
                #insert delete and replace

                insert_cost = dp[i][j-1]        #cost for insertion

                delete_cost = dp[i-1][j]        #cost for deletion

                replace_cost = dp[i-1][j-1]     #cost for replacement

                dp[i][j] = 1 + min(insert_cost, delete_cost, replace_cost)      
                                      

                #transposition
                if (i > 1 and j > 1 and (str1[i - 1] == str2[j - 2]) and (str1[i - 2] == str2[j - 1])):
                
                    transposition_cost = dp[i-2][j-2] + 1   #cost for transposition

                    dp[i][j] = min(dp[i][j], transposition_cost)
                
                
    return dp[m][n]


dictionary_creation()

print(" ★ Reading dictionary .......")

print()

#read dictionary from file
with open("dictionary.txt","r") as file:
    words = file.readlines()
 
#list representation of dictionary
DICT = []

for word in words:
    DICT.append(word.rstrip())


#function to spell check the word and give related suggestions from dictionary 
def spell_checker(input_word):

    if input_word in DICT:

        print(" ★ Word is found in the dictionary ") 
    
    else:

        print(" ★ Sorry we didn't found the word in the dictionary, Did you mean :: ")
        print()

        suggestions = []
        suggested_words = []

        for word in DICT:        
            dis = editDistance(input_word,word)
            suggestions.append((dis,word))

        suggestions.sort()

        top_suggestions = suggestions[:5]

        for s in top_suggestions:
            suggested_words.append(s[1])
        
        for suggs in suggested_words:

            print(f" ➼ {suggs}")
            print()

    print("---------------------------------------------------------")



print(" ★ Enter the input word :: ",end='')
input_wrd = input()

print()
spell_checker(input_wrd)





