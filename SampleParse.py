import LexicalDict
from _typeshed import Self

class RA:
    def __init__(self, tokens:list(str)) -> None:
        self.tokens = tokens
        self.current = 0
        self.currentToken = tokens[self.current]

    def getNextToken(self):
        if self.current < len[self.tokens]:
            self.current += 1

        self.currentToken = self.tokens[self.current]

    def error(self):
        print("There is a syntax error in the code. ")

    #<start> --> <poi>
    def start(self):
      self.poi()
    
    def poi(self):
      #<poi> -->  <when> | <during> | <as_> | <block> 
      if self.currentToken == LexicalDict.Lex.lexList[1]: #when/if 
        self.when()
      elif self.currentToken == LexicalDict.Lex.lexList[2]: #con/while
          self.con()
      elif self.currentToken == LexicalDict.Lex.lexList[4]:  #asig
          self.as_()
      elif self.currentToken == '{':   #block
          self.block()
      else:
        self.error()

    #when (if stmt)
    def when(self):

        #<when> --> 'when' '('  <bool>  ')' '[ <poi> ] 'else'  <poi> 

        if self.currentToken == LexicalDict.Lex.lexList[1]: # when
            self.getNextToken()
            if self.currentToken == LexicalDict.Lex.lexList[14]: # (
                self.getNextToken()
                self.bool()
                self.getNextToken()
                if self.currentToken == ')':
                    self.getNextToken()
                    if self.currentToken == '[':
                        self.getNextToken()
                        self.poi()
                        self.getNextToken()
                        if self.currentToken == ']':
                            self.getNextToken()
                            if self.currentToken == 'else':
                                self.getNextToken()
                                self.poi()
                                self.getNextToken()
                                if self.currentToken == ';':
                                    pass
                                else:
                                    self.error()
                            else:
                                self.error() 
                        else:
                            self.error() 
                    else:
                        self.error()    
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    #con_poi
    def con(self):
        
        #<con_circ> --> 'con' '('  <bool_poi>  ')' <poi> ';'

        if self.currentToken == 'con':
            self.getNextToken()
            if self.currentToken == '(':
                self.bool()
                self.getNextToken()
                if self.currentToken == ')':
                    self.getNextToken()
                    self.poi()
                    self.getNextToken()
                    if self.currentToken == ';':
                        pass
                    else:
                        self.error()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    def as_(self):
        #<as_poi> --> 'varNAme' '=' <expr> ';'
        if self.currentToken == 'varName':
            self.getNextToken()
            if self.currentToken == '=':
                self.getNextToken()
                self.expr()
            else:
                self.error()
        else:
            self.error()

    def bool(self):
        
        #<bool> --> '(' <poi> ')'
        if self.currentToken == '(':
            self.poi()
            self.getNextToken()
            if self.currentToken == ')':
                self.getNextToken()
            else:
                self.error()
        else:
            self.error()

            
            

    def expr(self):
        '''
        #<expr> --> <term>  ('+' | '-') <term> 
        '''
        self.term()
        while self.current == '+' or self.current == '-' :
            self.getNextToken()
            self.term()
            self.getNextToken()

    def term(self):
        '''
        <term> --> <factor> { ('*' | '\' | '%' ) <factor> }
        '''
        self.factor()
        while self.current == '*' or self.current == '\\' or self.current =='%':
            self.getNextToken()
            self.factor()
            self.getNextToken()

    def factor(self):
        '''
        <factor> --> 'id' | 'int_lit' | 'float_lit' | '(' ' <expr> ' ')'
        '''
        if self.currentToken in LexicalDict.varName.varPattern:
            self.getNextToken()
        elif self.currentToken == '(':
            self.getNextToken() 
            self.expr()
            if self.currentToken == ')':
                self.getNextToken()
                self.getNextToken() 
                if self.currentToken == ';':
                    self.getNextToken()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

