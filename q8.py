def check_palindrome(inputString):
    #i'm sorry my code is ugly
    inverse = ""
    for i in range(len(inputString)-1,-1,-1):
        inverse+= inputString[i]
    if(inputString == inverse):
        return True
    return False
print(check_palindrome("hel leh"))