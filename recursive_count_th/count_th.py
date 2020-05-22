'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # I need to be able to take a string as an argument in the given function 
    # I need to be able to retrun how many occurences of "th" occure in the word, case matters
    # I need to be able to use recursursion so there will be a base case 
    # I can't use any loops 
    # variable for length of word
    # variable for length of th

    n1 = len(word)
    n2 = len("th")
    if (n1 == 0 or n1 < n2):
        return 0
    if (word[0: n2] == "th"):
        return count_th(word[n2:]) + 1 
    return count_th(word[n2-1:])

    