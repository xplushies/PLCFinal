

class Token():

    #constructor for token
    def __init__(self, tokens:list(str)):
        self.tokens = tokens 
        self.lexeme = lex
        self.code = 0 # int for token code
        self.currentToken = tokens[self.current]

    def getNextToken(self):
        if self.current < len[self.tokens]:
            self.current += 1

        self.currentToken = self.tokens[self.current]

    def error(self):
        print("There is a syntax error in the code. ")

    class String():
        pass
