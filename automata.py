
import Tokens
class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.transition = 0
        self.past = False
        self.lexeme = ""
        self.digitletters=False  # -구분용

    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates={}
        self.acceptedStates.update(_dfa["AcceptedStates"])
 
    def PeekNextState(self, _input,_dfa,_sign=0):
        #print(_input, self.transition)
        #print(_input)
        if(self.transition == len(_dfa)):
            print('error')
            exit()
        
        self.LoadTransitionTable(_dfa[self.transition]) # "whitespace"
        if _input in self.table[self.currentState] and self.transition==0:
            return "finish"

        if  _input not in self.table[self.currentState] and self.past==False: #없다면
            self.transition += 1
            return self.PeekNextState(_input,_dfa,_sign)
        if(_input not in self.table[self.currentState] and self.past==True):
            #print("hi",_input)
            print(self.GetToken(),self.lexeme)
            self.Reset()
            return self.PeekNextState(_input,_dfa,_sign)
        if ('-' == _input):
            if(self.digitletters):
                self.transition=4
            else:
                self.transition=1
            self.LoadTransitionTable(_dfa[self.transition])

        if _input in self.table[self.currentState]:
            
            nextState = self.table[self.currentState][_input]
            self.past=True
            self.lexeme += _input
            

            #if _sign==1 or self.table[nextState][_input]=="":
            #if _sign==1:
                #self.SetState(nextState)
            #    return "finish"
            #if nextState == "" :
            #    return "finish"
            #if self.table[nextState][_input]=="":
            #    return ""
            #else:
            return nextState
 
    def SetState(self, _state):
        self.currentState = _state
 
    def GetToken(self):
        #print(self.lexeme, self.transition,self.acceptedStates)
        if self.lexeme in Tokens.symbols:
            return Tokens.symbols[self.lexeme]
        if self.currentState in self.acceptedStates:
            if(self.acceptedStates[self.currentState]=="Integer" or self.acceptedStates[self.currentState]=="ID"):
                self.digitletters=True
            else:
                self.digitletters=False
                
            return self.acceptedStates[self.currentState]
        else:
            print("ERROR")
            exit()
 
    def IsAccepted(self):
        if self.currentState in self.acceptedStates:
            return True
        else:
            return False
 
    def Reset(self):
        self.currentState = "T0"
        self.transition = 0
        self.past=False
        self.lexeme = ""
        #self.digitletters=False