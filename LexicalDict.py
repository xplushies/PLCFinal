import re
#from _typeshed import Self
class Lex:
    lexList = []

    lexList.insert(0, "start")
    lexList.insert(1, "when")  #if statment
    lexList.insert(2, "con")  #while statement
    lexList.insert(3, "block")  #block statment
    lexList.insert(4, "as_")  #assignemt statement

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

#class error():
#    error = ("There is a Lexical error here.")

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

class LexAnalyzer:

    def toList(file):
        fl= open(file).read().split()
        return fl

    numErrors = 0
    lexCount = 0 #total lexemes, excluding comments
    def analyzer(file):
        fl = LexAnalyzer.toList(file)
        current = 0 #current int index of token list
        length = len(fl)
        lexCount = 0 #total lexemes, excluding comments
        #accounts for single line comments
        while (current < length):
            if fl[current] != "<:" and fl[current] != "<<:":
                LexAnalyzer.checkLex(fl[current])
                current +=1
            elif fl[current] == "<:":
                current += 1 #skip
                while (fl[current] != ":>"):
                    current += 1 #skip
                if (fl[current] == ":>"):
                    current += 1 #skip
                    #if a single line comment doesn't end with :>>, lex error and break loop
                else:
                    #error()
                    print("1")
                    break
            elif fl[current] == "<<:":
                current += 1 #skip
                while (fl[current] != ":>>"):
                    current += 1 #skip
                if (fl[current] == ":>>"):
                    current += 1 #skip
                    #if a mult line comment doesn't end with :>>, lex error and break loop
                else:
                    #error()
                    print("2")
                    break


        #returns num of errors in the file and is grammatically correct        
        if LexAnalyzer.numErrors == 1:
            print("There was " + str(LexAnalyzer.numErrors) + " lexical error in the code.")
        else:
            print("There were " + str(LexAnalyzer.numErrors) + " lexical errors in the code.")
        

    #helper method for analyzer
    def checkLex(token):
        if token in Lex.lexList:
            print(token + " is a lexeme.")
            LexAnalyzer.lexCount += 1
        elif natNum.numPattern.fullmatch(token):
            print(token + " is a natNum lexeme.")
            LexAnalyzer.lexCount += 1
        elif realNum.numPattern.fullmatch(token):
            print(token + " is a realNum lexeme.")
            LexAnalyzer.lexCount += 1
        elif varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
            LexAnalyzer.lexCount += 1
        elif token in bool.boolTypes:
            print(token + " is a bool lexeme.")
            LexAnalyzer.lexCount += 1
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            LexAnalyzer.numErrors += 1
        

    
    