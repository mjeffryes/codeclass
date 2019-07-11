def checkWord(W):
    """Helper for listOfWords def - this checks if 
    character is in alphabet or a period"""
    if W in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.':
            return True
    else:
        return False

def listOfWords(S):
    """takes as input a string S and should 
    return a list of the "words" in S."""
    if S == '':
        return ['']
    else:
        L = listOfWords(S[1:])
        print('L ==', L)
        if checkWord(S[0]):
            List = [S[0] + L[0]]
            print('List ==', List)
            return List + L[1:]
        else: 
            return [''] + L


