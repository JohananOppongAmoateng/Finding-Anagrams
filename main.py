# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(word,word2):
    # [assignment] Add your code here
    word
    word =sorted(word.replace(" ",""))
    word2 = sorted(word2.replace(" ",""))
    if word == word2:
        print(True)
        return True
    else:
        print(False)
        return False
    
# find_anagrams("race c ar","ca j r r ace")
