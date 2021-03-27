
import Tokens
class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.transition = 0
        self.past = False
        self.lexeme = ""

    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates.update(_dfa["AcceptedStates"])
 
    def PeekNextState(self, _input,_dfa,_sign=0):
        #print(_input)
        if(self.transition == len(_dfa)):
            return "에러"
        self.LoadTransitionTable(_dfa[self.transition])
        if _input in self.table[self.currentState] and self.transition==0:
            return "finish"
        if  _input not in self.table[self.currentState] and self.past==False: #없다면
            self.transition += 1
            return self.PeekNextState(_input,_dfa,_sign)
        if(_input not in self.table[self.currentState] and self.past==True):
            print(self.GetToken(),self.lexeme)
            self.Reset()
            return self.PeekNextState(_input,_dfa,_sign)
        if _input in self.table[self.currentState]:
            #print('qerqrewr')
            nextState = self.table[self.currentState][_input]
            self.past=True
            self.lexeme += _input
            #print(nextState)
            #if _sign==1 or self.table[nextState][_input]=="":
            if _sign==1:
                self.SetState(nextState)
                return "finish"
            if nextState == "" :
                return "finish"
            #if self.table[nextState][_input]=="":
            #    return ""
            else:
                return nextState
 
    def SetState(self, _state):
        self.currentState = _state
 
    def GetToken(self):
        if self.lexeme in Tokens.symbols:
            return Tokens.symbols[self.lexeme]
        if self.currentState in self.acceptedStates:
            return self.acceptedStates[self.currentState]
        else:
            return "Unknown Token"
 
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