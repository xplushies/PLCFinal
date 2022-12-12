import re
from typing import Self

class Token:
    def __init__(self, code:int, lex:str):
        self.code = code
        self.lex = lex


class Lexer:
    lexList = []

    lexList.insert(0, "start")
    lexList.insert(1, "if")  #if statment
    lexList.insert(2, "while")  #while statement
    lexList.insert(3, "block")  #block statment
    lexList.insert(4, "asig")  #assignemt statement

    lexList.insert(5, "expr")  #expression
    lexList.insert(6, "term")  #term
    lexList.insert(7, "factor")  #factor

    lexList.insert(8, "bool_expr")  #boolean expression
    lexList.insert(9, "boolAnd")  #boolean and
    lexList.insert(10, "boolEqu")  #boolean equal to
    lexList.insert(11, "boolRel")  #boolean relation operation

    lexList.insert(12, "{")  #start
    lexList.insert(13, "}")  #end

    lexList.insert(14, "(")  #parenR bracket
    lexList.insert(15, ")")  #parenL bracket
    lexList.insert(16, "[")  #squareR bracket
    lexList.insert(17, "]")  #squareL bracket

    lexList.insert(18, "/")  #division
    lexList.insert(19, "%")  #modulous
    lexList.insert(20, "*")  #multiple
    lexList.insert(21, "+")  #addition
    lexList.insert(22, "-")  #subtraction

    lexList.insert(23, "=")  #assignment
    lexList.insert(24, "<")  #lessThan sign
    lexList.insert(25, ">")  #greaterThan sign
    lexList.insert(26, "<=") #greaterThanEqualTo
    lexList.insert(27, ">=") #greaterThanEqualTo
    lexList.insert(28, "==") #equalTo
    lexList.insert(29, "!=") #doesNotEqual

    lexList.insert(30, ":")   #colen
    lexList.insert(31, ";")   #end of stmt
    lexList.insert(32, "@")   #1 byte memory suffix
    lexList.insert(33, "#")   #2 byte memory suffix
    lexList.insert(34, "$")   #3 byte memory suffix
    lexList.insert(35, "^")   #4 byte memory suffix
    lexList.insert(36, "&")   #and
    lexList.insert(37, "|")   #or
    lexList.insert(38, "\\")  #escape character
    lexList.insert(39, ",")   #comma
    lexList.insert(40, "else")#else
    #lexList.insert(41, "<:")  #single line comment beginning
    #lexList.insert(42, ":>")  #single line comment end
    #lexList.insert(43, "<<:") #multi-line comment beginning
    #lexList.insert(44, ":>>") #multi-line comment end


    lexList.insert(50, " ")  #space

    class error():
        error = ("There is a Lexical error here.")

    class varName:
        varPattern = re.compile(r"\b\w{6,8}\b")

    #natiral_literal: whole numbers w/out decimals
    class natNum:
        numPattern = re.compile(r"(\d)+[@#$^]*")

    #decimals/fractions
    class realNum:
        numPattern = re.compile(r"((\d)*[\.])?(\d)+[@#$^]*")

    class bool:
        true = "true"
        false = "false"
        boolTypes = [true, false]

    class char:
        charPattern = re.compile(r"\'[a-zA-Z0-9]\'")

    class string:
        stringPattern = re.compile(r"\"[a-zA-Z0-9]+\"")



    def __init__(self, input:list(str)):
        self.input = input
        self.dict = Lexer.lexList


        self.tokens = []
        self.typeList = []
        self.lexCount = 0 #total lexemes, excluding comments

    def analyzer(self):
        current = 0 #current int index of token list
        length = len(self.input) #length of token list
        #accounts for single line comments
        while (current < length):
            if self.input[current] != "<:" and self.input[current] != "<<:":
                self.checkLex(self.input[current])
                self.tokens.append(self.input[current])
                current +=1
            elif self.input[current] == "<:":
                current += 1 #skip
                while (self.input[current] != ":>"):
                    current += 1 #skip
                if (self.input[current] == ":>"):
                    current += 1 #skip
                    #if a single line comment doesn't end with :>>, lex error and break loop
                else:
                    Lexer.error()
                    break
            elif self.input[current] == "<<:":
                current += 1 #skip
                while (self.input[current] != ":>>"):
                    current += 1 #skip
                if (self.input[current] == ":>>"):
                    current += 1 #skip
                    #if a mult line comment doesn't end with :>>, lex error and break loop
                else:
                    Lexer.error()
                    break
        return print(self.tokens)
        
    #helper method for analyzer
    def checkLex(self, token):
        if token in self.dict:
            print(token + " is a lexeme.")
            if token == "=":
                self.typeList.append("asig")
                self.lexCount += 1
            elif token == ("<" or "<=" or ">" or ">=" or "==" or "!="):
                self.typeList.append("boolOp")
                self.lexCount += 1
            elif token == ("+" or "-" or "*" or "/" or "%"):
                self.typeList.append("mathOp")
                self.lexCount += 1
            elif token == ("&" or "|"):
                self.typeList.append("logicOp")
                self.lexCount += 1
            elif token == ("@" or "#" or "$" or "^"):
                self.typeList.append("memorySuffix")
                self.lexCount += 1
            elif token == ("(" or ")" or "{" or "}" or "[" or "]"):
                self.typeList.append("parenthesis")
                self.lexCount += 1
            elif token == (";" or "," or ":" or "."):
                self.typeList.append("punctuation")
                self.lexCount += 1
            elif token == ("else"):
                self.typeList.append("else")
                self.lexCount += 1
            elif token == (" "):
                self.typeList.append("space")
                self.lexCount += 1
            elif token == ("\\"):
                self.typeList.append("escape")
                self.lexCount += 1
            elif token == ("\""):
                self.typeList.append("string")
                self.lexCount += 1
            elif token == ("\'"):
                self.typeList.append("char")
                self.lexCount += 1
            elif token == ("true" or "false"):
                self.typeList.append("bool")
                self.lexCount += 1
            elif token == ("if" or "when" or "con" or "block" or "as_"):
                self.typeList.append("keyword")
                self.lexCount += 1
            else:
                self.typeList.append("undefined type")
                self.lexCount += 1
            #self.typeList.append("undefined type")
            #self.lexCount += 1
        elif Lexer.natNum.numPattern.fullmatch(token):
            print(token + " is a natNum lexeme.")
            self.typeList.append("natNum")
            self.lexCount += 1
        elif Lexer.realNum.numPattern.fullmatch(token):
            print(token + " is a realNum lexeme.")
            self.typeList.append("realNum")
            self.lexCount += 1
        elif Lexer.varName.varPattern.fullmatch(token):
            print(token + " is a varName lexeme.")
            self.typeList.append("varName")
            self.lexCount += 1
        elif Lexer.string.stringPattern.fullmatch(token):
            print(token + " is a string lexeme.")
            self.typeList.append("string")
            self.lexCount += 1
        elif Lexer.char.charPattern.fullmatch(token):
            print(token + " is a char lexeme.")
            self.typeList.append("char")
            self.lexCount += 1
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            self.numErrors += 1
            self.typeList.append("undefined")


        

#class Parser:
#
#    #constructor for token
#    def __init__(self, tokens:list(str)):
#        self.tokens = tokens
#        self.current = 0
#        self.currentToken = self.tokens[self.current]
#
#    def getNextToken(self):
#        if self.current < len[self.tokens]:
#            self.current += 1
#
#        self.currentToken = self.tokens[self.current]
#
#    
#    def error(self):
#        print("There is a syntax error in the code. ")
#
#    #<start> --> <poi>
#    def start(self):
#        self.poi()
#
#    #def sortLexTypes(file):
#    #    self.input = Token.toList(file)
#    #    for i in self.input:
#    #        if i in LexicalDict.Lex.lexList:
#    #            Token.typeList.append(LexicalDict.Lex.lexList.index(i))
#    #        else:
#    #            Token.typeList.append(0)
#
#
#    
#    def poi(self):
#        #<poi> -->  <when> | <during> | <as_> | <block> 
#        if self.currentToken == "when": #when/if 
#            self.when()
#        elif self.currentToken == "con": #con/while
#            self.con()
#        elif self.currentToken == "asig":  #asig
#            self.as_()
#        elif self.currentToken == "(":   #block
#            self.block()
#        else:
#            self.error()
#
#    def asig(self):
#        #<asig> --> 'asig' <id> <op> <expr> ';'
#        if self.currentToken == "asig":
#            pass
#
#class Compiler:
#    def __init__(self, file:str):
#        self.file = file
#        text_file = open(file, "r")
#
#        input = text_file.read()
#        lex = Lexer(input)
#        tokens = lex.find_tokens()
#        print(tokens)
#        parser = Parser(tokens)
#        parser.program()
#        #semantics = Semantics(tokens)
#        text_file.close