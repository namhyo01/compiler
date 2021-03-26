
class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.transition = 0
 
    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates.update(_dfa["AcceptedStates"])
 
    def PeekNextState(self, _input,_dfa):
        self.LoadTransitionTable(_dfa[self.transition])

        if  _input not in self.table[self.currentState]: #없다면
            return "change"
        nextState = self.table[self.currentState][_input]
           
        if nextState == "":
            return "finish"
        else:
            return nextState
    def GetState(self):
        return self.currentState
 
    def SetState(self, _state):
        self.currentState = _state
 
    def GetToken(self):
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