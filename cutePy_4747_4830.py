# Archontis Nestoras 4747 cse94747
# Spyridon Chalidias 4830 cse94830

import sys

################ Lex ################

class Token:

    def __init__(self, recognized_string, family, line_number):
        self.recognized_string = recognized_string
        self.family = family
        self.line_number = line_number

    def getFamily(self):
        return  self.family
    def getLineNumber(self):
        return  self.line_number
    def getRecognizedString(self):
        return  self.recognized_string
    
    def setFamily(self,family): 
        self.family=family

class Lex:
    def __init__(self, file_name):#th monada poy dhmioyrgei kai ua epistrecei
        #real
        self.current_line_int = 0
        self.file_name = file_name
        self.token = Token
        self.lenOfWord=0
        
        #open
        file=open(file_name,"r",encoding="utf-8")
        self.lines=file.readlines()
        if(self.current_line_int<=len(self.lines)):
            self.lines[-1]=self.lines[-1].rstrip()
            self.lines[-1]+="\n"
            self.line_str=self.lines[self.current_line_int]#exei th seira poy doyleyoymai
            self.line_str.rstrip()#bgazei ta spaces apo to telos toy string den xerwan xreiazetai
            print('...TOKENS...')
        else:
            print ("end of program")
        #counters
        #self.lineCounter=0 se poia seira eimai de xreiazetai giati exw to currentline
        self.letterCounter=0 #se poio gramma ths lexhw eimai

    def getFileLines(self):
        return len(self.lines)

    def next_Token(self):
        state='state0'
        while state!='OK' and state!='error':
            input=self.line_str[self.letterCounter]

            #skip ta kena kai ta tabs
            if state == 'state0' and input == ' ' or input=='\t':
                state = 'state0'
                self.letterCounter = self.letterCounter + 1
            
            elif state == 'state0' and (input.isalpha() or input=='_'):
                state = 'state1'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter+1
            elif state == 'state1' and (input.isalpha() or input=='_' or input.isdigit()):
                state = 'state1'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter+1
            elif state == 'state1' and input.isalpha()==False:
                state = 'OK'
                x = self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]
                if x == "def" or x == "if" or x == "else" or x == "while" or x == "return" or x == "print" or x == "input" or x == "not" or x == "and" or x == "or" or x == "int":
                    token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Keyword",self.current_line_int+1)
                    self.lenOfWord=0
                    print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                    return token1
                if len(self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter])>30:
                    state='error'
                    print("LEX ERROR at Line("+str(self.current_line_int+1)+"): The ID has more than 30 characters")
                    sys.exit()
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Id",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            
            elif state=='state0' and input.isdigit():
                state='state2'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state2' and input.isdigit():
                state='state2'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1 
            elif state=='state2' and input.isdigit()==False:
                state='OK'
                if int(self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter])>(pow(2,32)-1):
                    state='error'
                    print("LEX ERROR at Line ("+str(self.current_line_int+1)+") The number is out of range")
                    sys.exit()
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Number",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            
            elif state=='state0' and (input=="(" or input==")" or input=="[" or input=="]" ):
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"GroupSymbol",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            
            elif state=='state0' and (input==";" or input=="," or input==":"):
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Delimiter",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            
            elif state=='state0' and (input=="+" or input=="-"):
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"ADD_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            
            elif state=='state0' and input=="/":
                state='state11'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1 
            elif state=='state11' and input=="/":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"MUL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            elif state=='state11':
                state='error'
                print_str = "\nLEX ERROR at Line("+str(self.current_line_int+1)+"): The division is done with this notation '//'\n"
                sys.exit(print_str)
            elif state=='state0' and input=="*":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"MUL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            
            elif state=='state0' and input=="#":
                state='state3'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state3' and (input=="{" or input=="}"):
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"GroupSymbol",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber()) 
                return token1
            #comments
            elif state=='state3' and input=="$":
                print("START OF COMMMENTS")
                state='state9'
                self.letterCounter=self.letterCounter + 1
            elif state=='state9' and input=="#":
                state='state10'
                self.letterCounter=self.letterCounter + 1
            elif state=='state9':
                state='state9'
                self.letterCounter=self.letterCounter + 1
            elif state=='state10' and input=="$":
                print("END OF COMMMENTS")
                state='state0'
                self.lenOfWord=0
                self.letterCounter=self.letterCounter + 1
                # DO NOT return token HERE
            elif state=='state10' and input!="$":
                state='state9'
                self.letterCounter=self.letterCounter + 1

            elif state=='state3' and input.isalpha():
                state='state4'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state3' and input.isalpha()==False:
                state='error'
                print_str = "LEX ERROR at Line("+str(self.current_line_int+1)+")"
                sys.exit(print_str)
            elif state=='state4' and input.isalpha():
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state4' and input==" ":
                state='OK'
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Declare",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state4' and input.isalpha()==False:
                state='error'
                print_str = "LEX ERROR at Line("+str(self.current_line_int+1)+"): Expected '#declare'"
                sys.exit(print_str)
            
            elif state=='state0' and (input=="<" or input==">"):
                state='state5'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state5' and input=="=":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"REL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state5' and input!="=":
                state='OK'
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"REL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state0' and input=="=":
                state='state6'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state6' and input=="=":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"REL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state6' and input!="=":
                state='OK'
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"Assignment",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state0' and input=="!":
                state='state7'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state7' and input=="=":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"REL_OP",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state7' and input!="=":
                state='error'
                #ayto termatizei olo to script
                print_str = "LEX ERROR at Line("+str(self.current_line_int+1)+"): Maybe you want to write '!='"
                sys.exit(print_str)

            elif state=='state0' and input=="\"":
                state='state8'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state8' and (input=="_" or input.isalpha()):
                state='state8'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
            elif state=='state8' and input=="\"":
                state='OK'
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"QuotationMarksMain",self.current_line_int+1)
                self.lenOfWord=0
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1
            elif state=='state8' and (input!="_" or input.isalpha()==False):
                state='error'
                print_str = "\nLEX ERROR at Line("+str(self.current_line_int+1)+"): Cannot write Strings. Maybe you want to write '\"__main__\"'\n"
                sys.exit(print_str)

            #check an ftasame sto telos tou arxeiou
            elif state=='state0' and self.current_line_int+1==len(self.lines):
                state='OK'
                token1=Token("eof","EndOfFile",self.current_line_int+1)
                print(token1.getRecognizedString(),", Family: ",token1.getFamily(),", Line: ",token1.getLineNumber())
                return token1

            elif input=='\n':
                self.current_line_int+=1
                self.letterCounter=0
                self.line_str=self.lines[self.current_line_int]
                state='state0'
            
            else:
                self.lenOfWord+=1
                self.letterCounter=self.letterCounter + 1
                token1=Token((self.line_str[(self.letterCounter-self.lenOfWord):self.letterCounter]),"WrongSymbol",self.current_line_int+1)
                self.lenOfWord=0
                print_str = "LEX ERROR at Line("+str(self.current_line_int+1)+"): This symbol \'"+str(token1.getRecognizedString())+"\' is unexpected"
                sys.exit(print_str)

################ Syntax ################
global count
count=0
global flagPar
flagPar = True

class Parser:
    def __init__(self):
        param1=sys.argv[1]
        self.lex1=Lex(param1)
    
    def get_token(self):
        self.token=self.lex1.next_Token()
        return self.token
    
    def error(self, type_error):
        if type_error == "def_main_func_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct definition for main_functions"
            sys.exit(print_str)
        if type_error == "def_main_func_:_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct definition for main_functions"
            sys.exit(print_str)
        if type_error == "def_func_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct definition for functions"
            sys.exit(print_str)
        if type_error == "def_func_:_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct definition for functions"
            sys.exit(print_str)
        elif type_error == "#{_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to open the function with '#{'"
            sys.exit(print_str)
        elif type_error == "#}_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to close the function with '#}'"
            sys.exit(print_str)
        elif type_error == "var_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): name variable expected"
            sys.exit(print_str)
        elif type_error == "def_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to start with def"
            sys.exit(print_str)
        elif type_error == "if_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to start with if or maybe def"
            sys.exit(print_str)
        elif type_error == "st_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected some statements here"
            sys.exit(print_str)
        elif type_error == "var_name_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): illegal variable name"
            sys.exit(print_str)
        elif type_error == "call_main_part_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct call for main part"
            sys.exit(print_str)
        elif type_error == "call_main_part_:_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct call for main part"
            sys.exit(print_str)
        elif type_error == "call_main_func_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct call for main functions"
            sys.exit(print_str)
        elif type_error == "call_main_func_;_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct call for main functions"
            sys.exit(print_str)
        elif type_error == "assignment_stat_;_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): expected to end with ;"
            sys.exit(print_str)
        elif type_error == "assignment_stat_)_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected )"
            sys.exit(print_str)
        elif type_error == "assignment_stat_(_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected ("
            sys.exit(print_str)
        elif type_error == ":_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): expected :"
            sys.exit(print_str)
        elif type_error=="assignment_stat_input_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected the word input"    
            sys.exit(print_str)
        elif type_error=="assignment_stat_start_=_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct way to start after ="    
            sys.exit(print_str)
        elif type_error=="assignment_stat_=_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected ="    
            sys.exit(print_str)
        elif type_error == "call_print_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct call for print"
            sys.exit(print_str)
        elif type_error == "call_print_;_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct call for print"
            sys.exit(print_str)
        elif type_error == "call_return_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct call for return"
            sys.exit(print_str)
        elif type_error == "call_return_;_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): that is not a correct call for return"
            sys.exit(print_str)
        elif type_error == "(_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to open the parentheses with '('"
            sys.exit(print_str)
        elif type_error == ")_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to close the parentheses with ')'"
            sys.exit(print_str)
        elif type_error == "expr_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected some expression here"
            sys.exit(print_str)
        elif type_error == "define_err":
            print_str="SYNTAX ERROR at Line("+str(token.getLineNumber())+"): '"+str(token.getRecognizedString())+"' is not defined"
            sys.exit(print_str)
        elif type_error == "[_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to open the brackets with '['"
            sys.exit(print_str)
        elif type_error == "]_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected to close the brackets with ']'"
            sys.exit(print_str)
        elif type_error == "relOp_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected some RelOperations here"
            sys.exit(print_str)
        elif type_error == "cond_exp_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): expected some condition here"
            sys.exit(print_str)
        elif type_error == "if_body_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct start for if statement"
            sys.exit(print_str)
        elif type_error == "while_body_err":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber())+"): that is not a correct start for while statement"
            sys.exit(print_str)
        elif type_error == "no_return_main":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): no return statement in main functions"
            sys.exit(print_str)
        elif type_error == "must_return_func":
            print_str="SYNTAX ERROR at Line("+str(self.token.getLineNumber()-1)+"): functions must have a return statement"
            sys.exit(print_str)
    
    def syntax_analyzer(self):
        global token
        global table
        table = Table()
        token = self.get_token()
        self.startRule()
        print('Compilation successfully completed')
        print()

    def startRule(self):
        global token
        global listOfFuncNames
        listOfFuncNames = []
        self.def_main_part()
        self.call_main_part()
        
    def def_main_part(self):
        global token
        self.def_main_function()
        while token.getRecognizedString()=="def":
            self.def_main_function()
    
    def def_main_function(self):
        global token
        global flag_for_main_function
        global counter
        global table
        global label_count
        global count
        global flagPar
        local_id = ''
        if token.getRecognizedString()=="def":
            token=self.get_token()
            if token.getFamily()=="Id" and token.getRecognizedString()[:5]=="main_":
                local_id = token.getRecognizedString()
                token=self.get_token()
                if token.getRecognizedString()=="(":
                    token=self.get_token()
                    if token.getRecognizedString()==")":
                        token=self.get_token()
                        if token.getRecognizedString()==":":
                            token=self.get_token()
                            if token.getRecognizedString()=="#{":
                                token=self.get_token()
                                
                                if len(table.listOfScopes) == 0:
                                    table.addScope() #-1
                                fun = Function(local_id, 0, 'int')
                                table.addEntity(fun)
                                table.addScope()

                                self.declarations()

                                while token.getRecognizedString()=="def":
                                    self.def_function()

                                genQuad('begin_block', local_id, '_', '_')

                                labelStartingQuad = label_count #+1
                                table.updateFields(fun, labelStartingQuad)

                                self.statements()

                                if token.getRecognizedString()=="#}":
                                    genQuad('end_block', local_id, '_', '_')

                                    table.updateFields(fun, labelStartingQuad)
                                    
                                    for quad in listOfQuads[count:len(listOfQuads)]:
                                        if quad.op == "begin_block" and quad.x == local_id:
                                            produceLabels(quad.label)
                                            produce("sw ra","(sp)")
                                        elif quad.op == ":=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "+":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("add t1","t2","t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "-":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("sub t1","t1","t2")
                                            storerv("t1", quad.z)
                                        elif quad.op == "*":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("mul t1","t2","t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "//":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("div t1","t1","t2")
                                            storerv("t1", quad.z)
                                        elif quad.op == "jump":
                                            produceLabels(quad.label)
                                            produce("j L"+str(quad.z))
                                        elif quad.op == "<":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("blt t1","t2","L"+str(quad.z))
                                        elif quad.op == ">":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bgt t1","t2","L"+str(quad.z))
                                        elif quad.op == "!=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bne t1","t2","L"+str(quad.z))
                                        elif quad.op == "<=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("ble t1","t2","L"+str(quad.z))
                                        elif quad.op == ">=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bge t1","t2","L"+str(quad.z))
                                        elif quad.op == "==":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("beq t1","t2","L"+str(quad.z))
                                        elif quad.op == "par":
                                            produceLabels(quad.label)
                                            if flagPar == False:
                                                i=i+1
                                                d=12+(i-1)*4
                                            if flagPar == True:
                                                i=1
                                                d=12+(i-1)*4
                                                flagPar = False
                                                func_call = table.searchEntity(quad.z)
                                                produce("addi fp","sp",str(func_call.frameLength))
                                            if quad.y == "cv":
                                                loadvr(quad.x, "t0")
                                                produce("sw t0", "-"+str(d)+"(fp)")
                                            elif quad.y == "ret":
                                                temp_var = table.searchEntity(quad.x)
                                                produce("addi t0", "sp", "-"+str(temp_var.offset))
                                                produce("sw t0", "-8(fp)")
                                        elif quad.op == "call":
                                            flagPar = True
                                            produceLabels(quad.label)
                                            produce("sw sp", "-4(fp)")
                                            func_call = table.searchEntity(quad.x)
                                            produce("addi sp", "sp", str(func_call.frameLength))
                                            produce("jal L"+str(func_call.startingQuad))
                                            produce("addi sp", "sp", "-"+str(func_call.frameLength))
                                        elif quad.op == "ret":
                                            self.error("no_return_main")
                                        elif quad.op == "in":
                                            produceLabels(quad.label)
                                            produce("li a7", "5")
                                            produce("ecall")
                                            storerv("a0", quad.x)
                                        elif quad.op == "out":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "a0")
                                            produce("li a7", "1")
                                            produce("ecall")
                                            produce("la a0", "str_nl")
                                            produce("li a7", "4")
                                            produce("ecall")
                                        elif quad.op == "end_block":
                                            produceLabels(quad.label)
                                            produce("lw ra", "(sp)")
                                            produce("jr ra")
                                    
                                    count = len(listOfQuads)
                                    #table.printTable()#
                                    

                                    table.deleteScope()

                                    token=self.get_token()
                                else:
                                    self.error("#}_err")
                            else:
                                self.error("#{_err")
                        else:
                            self.error("def_main_func_:_err")
                    else:
                        self.error("def_main_func_err")
                else:
                    self.error("def_main_func_err")
            else:
                self.error("def_main_func_err")
        else:
            self.error("def_exp_err")

    def def_function(self):
        global token
        global table
        global label_count
        local_id = ''
        global flagVar_Par
        global count
        global flagPar
        flagVar_Par = "Par"
        flagRetDefFunc = False
        func_calle = ''
        if token.getRecognizedString()=="def":
            token=self.get_token()
            if token.getFamily()=="Id" and token.getRecognizedString()[:5]!="main_":
                local_id = token.getRecognizedString()
                
                fun = Function(local_id, 0, 'int')
                table.addEntity(fun)
                table.addScope()
                
                token=self.get_token()
                if token.getRecognizedString()=="(":
                    token=self.get_token()
                    self.id_list()

                    for i in range(len(fun.listOfFormalParameters)):
                        param = Parameter(fun.listOfFormalParameters[i].name, "int", "cv")
                        table.addEntity(param)
                
                    if token.getRecognizedString()==")":
                        token=self.get_token()
                        if token.getRecognizedString()==":":
                            token=self.get_token()
                            if token.getRecognizedString()=="#{":
                                token=self.get_token()

                                self.declarations()

                                while token.getRecognizedString()=="def":
                                    self.def_function()

                                genQuad('begin_block', local_id, '_', '_')

                                labelStartingQuad = label_count #+1
                                table.updateFields(fun, labelStartingQuad)

                                self.statements()

                                if token.getRecognizedString()=="#}":
                                    genQuad('end_block', local_id, '_', '_')

                                    table.updateFields(fun, labelStartingQuad)

                                    for quad in listOfQuads[count:len(listOfQuads)]:
                                        if quad.op == "begin_block" and quad.x == local_id:
                                            func_calle = table.searchEntity(quad.x)
                                            produceLabels(quad.label)
                                            produce("sw ra","(sp)")
                                        elif quad.op == ":=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "+":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("add t1","t2","t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "-":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("sub t1","t1","t2")
                                            storerv("t1", quad.z)
                                        elif quad.op == "*":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("mul t1","t2","t1")
                                            storerv("t1", quad.z)
                                        elif quad.op == "//":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("div t1","t1","t2")
                                            storerv("t1", quad.z)
                                        elif quad.op == "jump":
                                            produceLabels(quad.label)
                                            produce("j L"+str(quad.z))
                                        elif quad.op == "<":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("blt t1","t2","L"+str(quad.z))
                                        elif quad.op == ">":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bgt t1","t2","L"+str(quad.z))
                                        elif quad.op == "!=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bne t1","t2","L"+str(quad.z))
                                        elif quad.op == "<=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("ble t1","t2","L"+str(quad.z))
                                        elif quad.op == ">=":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("bge t1","t2","L"+str(quad.z))
                                        elif quad.op == "==":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "t1")
                                            loadvr(quad.y, "t2")
                                            produce("beq t1","t2","L"+str(quad.z))
                                        elif quad.op == "par":
                                            produceLabels(quad.label)
                                            if flagPar == False:
                                                i=i+1
                                                d=12+(i-1)*4
                                            if flagPar == True:
                                                i=1
                                                d=12+(i-1)*4
                                                flagPar = False
                                                func_call = table.searchEntity(quad.z)
                                                produce("addi fp","sp",str(func_call.frameLength))
                                            if quad.y == "cv":
                                                loadvr(quad.x, "t0")
                                                produce("sw t0", "-"+str(d)+"(fp)")
                                            elif quad.y == "ret":
                                                temp_var = table.searchEntity(quad.x)
                                                produce("addi t0", "sp", "-"+str(temp_var.offset))
                                                produce("sw t0", "-8(fp)")
                                        elif quad.op == "call":
                                            flagPar = True
                                            produceLabels(quad.label)
                                            func_call = table.searchEntity(quad.x)

                                            #sto func prepei na ftiajoume kai tin periptosi tis klisis aderfou
                                            for scope in reversed(table.listOfScopes):
                                                if func_call in scope.listOfEntities:
                                                    func_call_level = scope.level
                                                if func_calle in scope.listOfEntities:
                                                    func_calle_level = scope.level
                                            if func_call_level == func_calle_level:
                                                produce("lw t0","-4(sp)")
                                                produce("sw t0","-4(fp)")
                                            else:
                                                produce("sw sp", "-4(fp)")
      
                                            produce("addi sp", "sp", str(func_call.frameLength))
                                            produce("jal L"+str(func_call.startingQuad))
                                            produce("addi sp", "sp", "-"+str(func_call.frameLength))
                                        elif quad.op == "ret":
                                            flagRetDefFunc = True #for SYNDAX
                                            produceLabels(quad.label)
                                            produce("lw t2", "-8(sp)")
                                            loadvr(quad.x, "t1")
                                            produce("sw t1", "(t2)")
                                            produce("j L"+str(len(listOfQuads)))
                                        elif quad.op == "in":
                                            produceLabels(quad.label)
                                            produce("li a7", "5")
                                            produce("ecall")
                                            storerv("a0", quad.x)
                                        elif quad.op == "out":
                                            produceLabels(quad.label)
                                            loadvr(quad.x, "a0")
                                            produce("li a7", "1")
                                            produce("ecall")
                                            produce("la a0", "str_nl")
                                            produce("li a7", "4")
                                            produce("ecall")
                                        elif quad.op == "end_block":
                                            if flagRetDefFunc == False:
                                                self.error("must_return_func")
                                            produceLabels(quad.label)
                                            produce("lw ra", "(sp)")
                                            produce("jr ra")
                                    
                                    count = len(listOfQuads)
                                    #table.printTable()#
                                    
                                    table.deleteScope()

                                    token=self.get_token()
                                else:
                                    self.error("#}_err")
                            else:
                                self.error("#{_err")
                        else:
                            self.error("def_func_:_err")
                    else:
                        self.error("def_func_err")
                else:
                    self.error("def_func_err")
            else:
                self.error("def_func_err")
        else:
            # NO error HERE
            pass
    
    def declarations(self):
        global token
        global flagVar_Par
        flagVar_Par = "Var"
        while token.getRecognizedString()=="#declare":
            token=self.get_token()
            self.declaration_line()
    
    def declaration_line(self):
        global token
        self.id_list()
            
    def id_list(self):
        global token
        global flagVar_Par
        if token.getFamily()=="Id":
            if flagVar_Par == "Var":
                var = Variable(token.getRecognizedString(), "int")
                table.addEntity(var)
            elif flagVar_Par == "Par":
                table.addFormalParameter(token.getRecognizedString(), "int", "cv")
            token=self.get_token()
            while token.getRecognizedString()==",":
                token=self.get_token()
                if token.getFamily()=="Id":
                    if flagVar_Par == "Var":
                        var = Variable(token.getRecognizedString(), "int")
                        table.addEntity(var)
                    elif flagVar_Par == "Par":
                        table.addFormalParameter(token.getRecognizedString(), "int", "cv")
                    token=self.get_token()
                else:
                    self.error("var_exp_err")
        elif token.getRecognizedString()==")":
            pass
        else:
            self.error("var_name_err")
    
    def call_main_part(self):
        global token
        if token.getRecognizedString()=="if":
            produceLabels("main")
            genQuad('begin_block', 'main', '_', '_')
            token=self.get_token()
            if token.getRecognizedString()=="__name__":
                token=self.get_token()
                if token.getRecognizedString()=="==":
                    token=self.get_token()
                    if token.getRecognizedString()=="\"__main__\"":
                        token=self.get_token()
                        if token.getRecognizedString()==":":
                            token=self.get_token()
                            self.main_function_call()
                            while token.getFamily()=="Id" and token.getRecognizedString()[:5]=="main_":
                                self.main_function_call()
                            if token.getRecognizedString()=="eof":
                                pass
                            else:
                                self.error("call_main_part_err")
                        else:
                            self.error("call_main_part_:_err")
                    else:
                        self.error("call_main_part_err")
                else:
                    self.error("call_main_part_err")
            else:
                self.error("call_main_part_err")
            genQuad('halt', '_', '_', '_')
            produceLabels(label_count)
            produce("li a0","0")
            produce("li a7","93")
            produce("ecall")

            genQuad('end_block', 'main', '_', '_')
        else:
            self.error("if_exp_err")

    def main_function_call(self):
        global token
        #global table
        if token.getFamily()=="Id":
            func_main_name = token.getRecognizedString()
            funcEntity = table.searchEntity(func_main_name)
            token=self.get_token()
            if token.getRecognizedString()=="(":
                token=self.get_token()
                if token.getRecognizedString()==")":
                    token=self.get_token()
                    if token.getRecognizedString()==";":
                        #func_res = newTemp()
                        #genQuad('par', func_res, 'ret', '_')

                        genQuad('call', func_main_name, '_', '_')

                        #table.printTable()#########################
                        produceLabels(label_count)
                        for quad in listOfQuads:
                            if quad.op == "begin_block" and quad.x == func_main_name:
                                produce("addi sp","sp",str(funcEntity.frameLength))
                                produce("jal L"+str(quad.label))
                                produce("addi sp","sp","-"+str(funcEntity.frameLength))
                            

                        token=self.get_token()
                    else:
                        self.error("call_main_func_;_err")
                else:
                    self.error("call_main_func_err")
            else:
                self.error("call_main_func_err")
        else:
            self.error("call_main_func_err")
    
    def statements(self):
        global token
        self.statement()
        while token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return" or token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
            self.statement()
    
    def statement(self):
        global token
        if token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return":
            self.simple_statement()
        elif token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
            self.structured_statement()
        else:
            self.error("st_exp_err")
    
    def simple_statement(self):
        global token
        if token.getFamily()=="Id":
            self.assignment_stat()
        elif token.getRecognizedString()=="print":
            self.print_stat()
        elif token.getRecognizedString()=="return":
            self.return_stat()
        else:
            pass
        
    def assignment_stat(self):
        global token
        global func_name
        global table
        global label_count
        if token.getFamily()=="Id":
            b = token.getRecognizedString()
            table.searchEntity(b)
            token=self.get_token()
            if token.getRecognizedString()=="=":
                token=self.get_token()
                if token.getFamily()=="ADD_OP" or token.getFamily()=="Number" or token.getRecognizedString()=="(" or token.getFamily()=="Id":
                    func_name = token.getRecognizedString()
                    a = self.expression()
                    if token.getRecognizedString()==";":
                        genQuad(':=', a, '_', b)
                        token=self.get_token()
                    else:
                        self.error("assignment_stat_;_err")
                elif token.getRecognizedString()=="int":
                    token=self.get_token()
                    if token.getRecognizedString()=="(":
                        token=self.get_token()
                        if token.getRecognizedString()=="input":
                            token=self.get_token()
                            if token.getRecognizedString()=="(":
                                token=self.get_token()
                                if token.getRecognizedString()==")":
                                    token=self.get_token()
                                    if token.getRecognizedString()==")":
                                        token=self.get_token()
                                        if token.getRecognizedString()==";":
                                            genQuad('in', 'x', '_', '_')
                                            token=self.get_token()
                                        else:
                                            self.error("assignment_stat_;_err")
                                    else:
                                        self.error("assignment_stat_)_err")
                                else:
                                    self.error("assignment_stat_)_err")
                            else:
                                self.error("assignment_stat_(_err")
                        else:
                            self.error("assignment_stat_input_err")
                    else:
                        self.error("assignment_stat_(_err")
                else:
                    self.error("assignment_stat_start_=_err")
            else:
                self.error("assignment_stat_=_err")
        else:
            pass
    
    def print_stat(self):
        global token
        if token.getRecognizedString()=="print":
            token=self.get_token()
            if token.getRecognizedString()=="(":
                token=self.get_token()
                x = self.expression()
                if token.getRecognizedString()==")":
                    token=self.get_token()
                    if token.getRecognizedString()==";":
                        genQuad('out', x, '_', '_')
                        token=self.get_token()
                    else:
                        self.error("call_print_;_err")
                else:
                    self.error("call_print_err")
            else:
                self.error("call_print_err")
        else:
            # NO error HERE
            pass
        
    def return_stat(self):
        global token 
        if token.getRecognizedString()=="return":
            token=self.get_token()
            if token.getRecognizedString()=="(":
                token=self.get_token()
                x = self.expression()
                if token.getRecognizedString()==")":
                    token=self.get_token()
                    if token.getRecognizedString()==";":
                        genQuad('ret', x, '_', '_')
                        token=self.get_token()
                    else:
                        self.error("call_return_;_err")
                else:
                    self.error("call_return_err")
            else:
                self.error("call_return_err")
        else:
            # NO error HERE
            pass

    def expression(self):
        global token
        global table
        self.optional_sign()
        T1_place = self.term() #T1
        while token.getFamily()=="ADD_OP":
            add_op = token.getRecognizedString()
            token=self.get_token()
            T2_place = self.term() #T2
            w = newTemp()
            genQuad(add_op, T1_place, T2_place, w)
            T1_place = w

            temp = TemporaryVariable(w, "int")
            table.addEntity(temp)

        E_place = T1_place
        return E_place
    
    def structured_statement(self):
        global token
        if token.getRecognizedString()=="if":
            self.if_stat()
        elif token.getRecognizedString()=="while":
            self.while_stat()
        else:
            #NO error HERE
            pass

    def if_stat(self):
        global token
        if token.getRecognizedString()=="if":
            token=self.get_token()
            if token.getRecognizedString()=="(":
                token=self.get_token()
                conditionList = self.condition()
                if token.getRecognizedString()==")":
                    backpatch(conditionList[1], nextQuad())
                    token=self.get_token()
                    if token.getRecognizedString()==":":
                        token=self.get_token()
                        if token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return" or token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
                            self.statement()
                            ifList = makeList(nextQuad())
                            genQuad('jump', '_', '_', '_')
                            backpatch(conditionList[0], nextQuad())
                            if token.getRecognizedString()=="else":
                                token=self.get_token()
                                if token.getRecognizedString()==":":
                                    token=self.get_token()       
                                    if token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return" or token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
                                        self.statement()
                                    elif token.getRecognizedString()=="#{":
                                        token=self.get_token()
                                        self.statements()
                                        if token.getRecognizedString()=="#}":
                                            token=self.get_token()
                                        else:
                                            self.error("#}_err")
                                    else:
                                        self.error("if_body_err")
                                else:
                                    self.error(":_exp_err")
                            else:
                                pass#oxi error
                            backpatch(ifList, nextQuad())
                        elif token.getRecognizedString()=="#{":
                            token=self.get_token()
                            self.statements()
                            ifList = makeList(nextQuad())
                            genQuad('jump', '_', '_', '_')
                            backpatch(conditionList[0], nextQuad())
                            if token.getRecognizedString()=="#}":
                                token=self.get_token()
                                if token.getRecognizedString()=="else":
                                    token=self.get_token()
                                    if token.getRecognizedString()==":":
                                        token=self.get_token()       
                                        if token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return" or token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
                                            self.statement()
                                        elif token.getRecognizedString()=="#{":
                                            token=self.get_token()
                                            self.statements()
                                            if token.getRecognizedString()=="#}":
                                                token=self.get_token()
                                            else:
                                                self.error("#}_err")
                                        else:
                                            self.error("if_body_err")
                                    else:
                                        self.error(":_exp_err")
                                else:
                                    pass#oxi error
                                backpatch(ifList, nextQuad())
                            else:
                                self.error("#}_err")
                        else:
                            self.error("if_body_err")
                    else:
                        self.error(":_exp_err")
                else:
                    self.error("assignment_stat_)_err")
            else:
                self.error("assignment_stat_(_err")
        else:
            #oxi error
            pass

    def while_stat(self):
        global token 
        if token.getRecognizedString()=="while":
            condQuad = nextQuad()
            token=self.get_token()
            if token.getRecognizedString()=="(":
                token=self.get_token()
                conditionList = self.condition()
                if token.getRecognizedString()==")":
                    backpatch(conditionList[1], nextQuad())
                    token=self.get_token()
                    if token.getRecognizedString()==":":
                        token=self.get_token()
                        if token.getFamily()=="Id" or token.getRecognizedString()=="print" or token.getRecognizedString()=="return" or token.getRecognizedString()=="if" or token.getRecognizedString()=="while":
                            self.statement()
                            genQuad('jump', '_', '_', condQuad)
                            backpatch(conditionList[0], nextQuad())
                        elif token.getRecognizedString()=="#{":
                            token=self.get_token()
                            self.statements()
                            if token.getRecognizedString()=="#}":
                                genQuad('jump', '_', '_', condQuad)
                                backpatch(conditionList[0], nextQuad())
                                token=self.get_token()
                            else:
                                self.error("#}_err")
                        else:
                            self.error("while_body_err")
                    else:
                        self.error(":_exp_err")
                else:
                    self.error("assignment_stat_)_err")
            else:
                self.error("assignment_stat_(_err")
        else:
            #oxi error
            pass
    
    def optional_sign(self):
        global token
        if token.getFamily()=="ADD_OP":
            token=self.get_token()  
        else:
            # NO error HERE
            pass

    def term(self):
        global token
        F1_place = self.factor()
        while token.getFamily()=="MUL_OP":
            mult_op = token.getRecognizedString()
            token=self.get_token()
            F2_place = self.factor()
            w = newTemp()
            genQuad(mult_op, F1_place, F2_place, w)
            F1_place = w

            temp = TemporaryVariable(w, "int")
            table.addEntity(temp)

        T_place = F1_place
        return T_place

    def factor(self):
        global token
        global local_id
        global func_name
        global listOfFuncNames
        global table
        if token.getFamily()=="Number":
            x = token.getRecognizedString()
            token=self.get_token()
            return x
        elif token.getRecognizedString()=="(":
            token=self.get_token()
            x = self.expression()
            if token.getRecognizedString()==")":
                token=self.get_token()
                return x
            else:
                self.error(")_exp_err")
        elif token.getFamily()=="Id":
            local_id = token.getRecognizedString()
            table.searchEntity(local_id)
            token=self.get_token()
            if token.getRecognizedString()=="(":#tha boume sigoura se sinartisi
                listOfFuncNames.append(local_id)
            x = self.idtail()
            return x
        else:
            self.error("expr_exp_err")


    def idtail(self):
        global token
        global local_id
        global func_name
        global listOfFuncNames
        global table
        if token.getRecognizedString()=="(":
            token=self.get_token()
            func_name = listOfFuncNames[-1]
            self.actual_par_list()
            listOfFuncNames.pop(-1)
            func_res = newTemp()
            genQuad('par', func_res, 'ret', func_name)
            genQuad('call', func_name, '_', '_')

            temp = TemporaryVariable(func_res, "int")
            table.addEntity(temp)

            if token.getRecognizedString()==")":
                token=self.get_token()
                return func_res
            else:
                self.error(")_exp_err")
        else:
            # NO error HERE
            return local_id
        
    def actual_par_list(self):
        global token
        global func_name
        if token.getFamily()=="ADD_OP" or token.getFamily()=="Number" or token.getRecognizedString()=="(" or token.getFamily()=="Id":        
            x = self.expression()
            genQuad('par', x, 'cv', func_name)
            while token.getRecognizedString()==",":
                token=self.get_token()
                x = self.expression()
                genQuad('par', x, 'cv', func_name)
        else:
            # NO error HERE
            pass

    def condition(self):
        global token
        B = []
        Q1 = self.bool_term()
        B_true = Q1[1]
        B_false = Q1[0]
        while token.getRecognizedString()=="or":
            backpatch(B_false, nextQuad())
            token=self.get_token()
            Q2 = self.bool_term()
            B_true = mergeList(B_true, Q2[1])
            B_false = Q2[0]
        B.append(B_false)
        B.append(B_true)
        return B

    def bool_term(self):
        global token
        Q = []
        R1 = self.bool_factor()
        Q_true = R1[1]
        Q_false = R1[0]
        while token.getRecognizedString()=="and":
            backpatch(Q_true, nextQuad())
            token=self.get_token()
            R2 = self.bool_factor()
            Q_false = mergeList(Q_false, R2[0])
            Q_true = R2[1]
        Q.append(Q_false)
        Q.append(Q_true)
        return Q

    def bool_factor(self):
        global token
        R = []
        if token.getRecognizedString()=="not":
            token=self.get_token()
            if token.getRecognizedString()=="[":
                token=self.get_token()
                B = self.condition()
                if token.getRecognizedString()=="]":
                    R_true = B[0]
                    R_false = B[1]
                    token=self.get_token()
                else:
                    self.error("]_exp_err")
            else:
                self.error("[_exp_err")
        elif token.getRecognizedString()=="[":
            token=self.get_token()
            B = self.condition()
            if token.getRecognizedString()=="]":
                R_true = B[1]
                R_false = B[0]
                token=self.get_token()
            else:
                self.error("]_exp_err")
        elif token.getFamily()=="ADD_OP" or token.getFamily()=="Number" or token.getRecognizedString()=="(" or token.getFamily()=="Id":
            E1_place = self.expression()
            if token.getFamily()=="REL_OP":
                rel_op = token.getRecognizedString()
                token=self.get_token()
                E2_place = self.expression()
                R_true = makeList(nextQuad())
                genQuad(rel_op, E1_place, E2_place, '_')
                R_false = makeList(nextQuad())
                genQuad('jump', '_', '_', '_')
            else:
                self.error("relOp_exp_err")
        else:
            self.error("cond_exp_err")
        R.append(R_false)
        R.append(R_true)
        return R

################ Endiamesos Kvdikas ################
global label_count
label_count = 0
global listOfQuads
listOfQuads = []
global count_temp
count_temp = 0

class Quad:
    def __init__(self, label, op, x, y, z):
        self.label = label
        self.op = op
        self.x = x
        self.y = y
        self.z = z
    
def genQuad(operator, operand1, operand2, operand3):
    global label_count
    global listOfQuads
    label_count = nextQuad()
    temp_quad = Quad(label_count, operator, operand1, operand2, operand3)
    listOfQuads.append(temp_quad)

def nextQuad():
    global label_count
    return label_count+1

def newTemp():
    global count_temp
    count_temp += 1
    temp_var = "T_" + str(count_temp)
    return temp_var

def emptyList():
    listOfLabels = []
    return listOfLabels

def makeList(label):
    listOfLabels = [label]
    return listOfLabels

def mergeList(list1, list2):
    return list1 + list2

def backpatch(list, setLabel):
    global listOfQuads
    for i in listOfQuads:
        for j in range(len(list)):
            if list[j] == i.label:
                i.z = setLabel

################ Symbol Table ################
class Entity:
    def __init__(self, name):
        self.name = name

class Constant(Entity):
    def __init__(self, name, datatype, value):
        super().__init__(name)
        self.datatype = datatype
        self.value = value

    def printEntities(self):
        return self.name + "/" + self.datatype + "/" + str(self.value)

class Variable(Entity):
    def __init__(self, name, datatype):
        super().__init__(name)
        self.datatype = datatype
        self.offset = 0

    def printEntities(self):
        return self.name + "/" + self.datatype + "/" + str(self.offset)

class FormalParameter(Entity):
    def __init__(self, name, datatype, mode):
        super().__init__(name)
        self.datatype = datatype
        self.mode = mode

    def printEntities(self):
        return self.name + "/" + self.datatype + "/" + self.mode

class Procedure(Entity):
    def __init__(self, name, startingQuad):
        super().__init__(name)
        self.startingQuad = startingQuad
        self.frameLength = 0
        self.listOfFormalParameters=[]

    def setStartingQuad(self, startingQuad):
        self.startingQuad=startingQuad

    def setFramelength(self, framelength):
        self.frameLength=framelength
   
    def addFormalParameterInListOfFormalParameters(self, name, datatype, mode):
        self.listOfFormalParameters.append(FormalParameter(name, datatype, mode))

    def printEntities(self):
        tempStr = ""
        count = 0
        for i in self.listOfFormalParameters:
            if count == 0:
                tempStr = i.name + "/" + i.datatype + "/" + i.mode
                count = 1
            else:
                tempStr = tempStr + " | " + i.name + "/" + i.datatype + "/" + i.mode
        return self.name + "/" + str(self.startingQuad) + "/" + str(self.frameLength) + "[" + tempStr + "]"


class TemporaryVariable(Variable):
    def __init__(self, name, datatype):
        super().__init__(name, datatype)

class Parameter(Variable):
    def __init__(self, name, datatype, mode):
        super().__init__(name, datatype)
        self.mode = mode

    def printEntities(self):
        return self.name + "/" + self.datatype + "/" + str(self.offset) + "/" + self.mode

class Function(Procedure):
    def __init__(self, name, startingQuad, datatype):
        super().__init__(name, startingQuad)
        self.datatype = datatype

class Scope:
    def __init__(self, level):
        self.listOfEntities=[]
        self.level=level
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level
        

class Table:
    global curentLevelCount
    global levelCount
    levelCount = -1

    def __init__(self):
        self.listOfScopes=[]

    def printTable(self):
        print("...PINAKAS SYBOLON...")
        for scope in reversed(self.listOfScopes):
            str1 = str(scope.level)
            for entity in scope.listOfEntities:
                str1 = str1 + " <- " + entity.printEntities()
            print(str1)

    def addEntity(self, entity):
        global offsetCount
        lastScope = self.listOfScopes[-1] #sto teleytaio Scope
        lastScope.listOfEntities.append(entity) #prosthetoume(stin teleutaia thesi) ena neo Entity
        if type(entity) == Variable or type(entity) == TemporaryVariable or type(entity) == Parameter:
            entity.offset = offsetCount
            offsetCount += 4

    def addScope(self):
        global levelCount
        global offsetCount
        offsetCount = 12
        sc = Scope(levelCount)
        levelCount += 1
        sc.setLevel(levelCount)
        self.listOfScopes.append(sc)

    def deleteScope(self):
        global levelCount
        global offsetCount
        sc = Scope(levelCount)
        levelCount -= 1
        sc.setLevel(levelCount)

        self.listOfScopes.pop(-1)

        flag = 0
        if len(self.listOfScopes) != 0:
            for entity in reversed(self.listOfScopes[-1].listOfEntities):
                if type(entity) == Variable or type(entity) == TemporaryVariable or type(entity) == Parameter:
                    offsetCount = entity.offset + 4
                    flag = 1
                    break
            if flag != 1:
                offsetCount = 12

    def updateFields(self, entity, startingQuad):
        global framelengthCount
        framelengthCount = 12
        entity.setStartingQuad(startingQuad)
        for entities in reversed(self.listOfScopes[-1].listOfEntities):
            if type(entities) == Variable or type(entities) == TemporaryVariable or type(entities) == Parameter:
                framelengthCount = framelengthCount + 4

        entity.setFramelength(framelengthCount)

    def addFormalParameter(self, name, dataType, mode):
        lastScope = self.listOfScopes[-2] #sto teleytaio Scope
        lastScope.listOfEntities[-1].addFormalParameterInListOfFormalParameters(name, dataType, mode)
    
    def searchEntity(self, name):
        global curentLevelCount
        x = len(self.listOfScopes)-1
        while(x >= 0):
            higherScopeToLower = self.listOfScopes[x]
            y = len(higherScopeToLower.listOfEntities)-1
            while(y >= 0):
                lastEntityToFirst = higherScopeToLower.listOfEntities[y]
                if name == lastEntityToFirst.name:
                    curentLevelCount=x
                    return lastEntityToFirst
                y -= 1
            x -= 1
        # An na ftasoume edo tha einai epeidi den ekane pote return, ara den to vrike pote to Entity
        # ARA edo tha xeiristoume to ERROR
        Parser().error("define_err")

################ Final Code ################
class Final:
    def __init__(self,x):
        self.x = x
    
def gnlvcode(v):
    global table
    global levelCount
    global curentLevelCount
    foundEntity = table.searchEntity(v)
    if type(foundEntity) == Variable or type(foundEntity) == Parameter:
        produce("lw t0","-4(sp)")
        for i in range(levelCount-(curentLevelCount+1)):
            produce("lw t0","-4(t0)")
        produce("addi t0","t0","-"+str(foundEntity.offset))

def loadvr(v, reg):
    global table
    global levelCount
    global curentLevelCount
    if v.isnumeric():
        produce("li "+str(reg), str(v))
    else:
        foundEntity = table.searchEntity(v)
        if (type(foundEntity) == Variable or type(foundEntity) == TemporaryVariable or type(foundEntity) == Parameter) and curentLevelCount==levelCount:
            produce("lw "+str(reg), "-"+str(foundEntity.offset)+"(sp)")
        elif (type(foundEntity) == Variable or type(foundEntity) == Parameter) and curentLevelCount<levelCount:
            gnlvcode(v)
            produce("lw "+str(reg), "(t0)")

def storerv(reg, v):
    global table
    global levelCount
    global curentLevelCount
    foundEntity = table.searchEntity(v)
    if (type(foundEntity) == Variable or type(foundEntity) == TemporaryVariable or type(foundEntity) == Parameter) and curentLevelCount==levelCount:
        produce("sw "+str(reg), "-"+str(foundEntity.offset)+"(sp)")
    elif (type(foundEntity) == Variable or type(foundEntity) == Parameter) and curentLevelCount<levelCount:
        gnlvcode(v)
        produce("sw "+str(reg), "(t0)")

def produce(command,reg1=None,reg2=None):
    with open("file.asm", "a") as myfile:
        if reg1 == None:
            myfile.write('\t'+str(command)+'\n')
        elif reg2 == None:
            myfile.write('\t'+str(command)+','+str(reg1)+'\n')
        else:
            myfile.write('\t'+str(command)+','+str(reg1)+','+str(reg2)+'\n')
    myfile.close()

def produceLabels(num):
    with open("file.asm", "a") as myfile:
        myfile.write('L'+str(num)+':\n')
    myfile.close()

################ RUN ################
f = open("file.asm", "w")
produce(".data")
produce("str_nl: .asciz \"\\n\"")
produce(".text")
produce("")
produceLabels(0)
produce("j Lmain")

parser1 = Parser()
parser1.syntax_analyzer()

print('...ENDIAMESOS KVDIKAS...')
for i in range(len(listOfQuads)):
    print(listOfQuads[i].label, ": ", listOfQuads[i].op,", ", listOfQuads[i].x, ", ", listOfQuads[i].y, ", ", listOfQuads[i].z)

'''
print('...ASSEMBLY CODE...')
for i in range(len(listOfQuads)):
    #produce("L"+str(listOfQuads[i].label)+':\n', 'aaa')
    if listOfQuads[i].op == ":=":
        loadvr(listOfQuads[i].x, "t0")
        storerv("t0", listOfQuads[i].z)
'''

'''
produce(1,2,3)
produce(2,3,1)
produce(3,1)
produce(1,3,2)
produce(2,1)
'''
f.close()

