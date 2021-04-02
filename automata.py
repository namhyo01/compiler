
from Tokens import *
class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.transition = 0
        self.past = False # 이전에 처리하고 있던 문자들이 있었나 확인
        self.lexeme = "" # 문자들이 테이블에 해당되면 문자열로 엮어주기위해존재
        self.digitletters=False  # -구분용

    def LoadTransitionTable(self, _dfa): # 트랜지션 테이블 생성
        self.table = _dfa["Table"]
        self.acceptedStates={}
        self.acceptedStates.update(_dfa["AcceptedStates"])#트랜지션 딕셔너리에서 AcceptedStates가 Key인 Values들을 집어넣는다.
 
 #_input은 입력 단어, _dfa는 트랜지션 테이블입니다.(리스트 형식)
    def PeekNextState(self, _input,_dfa):
        
        if(self.transition == len(_dfa)): #그 만약에 transition테이블 전체를 다 돌았는데도 맞아 떨어지는 값이 없다면 에러를 내뱉는다
            return "error"
        
        self.LoadTransitionTable(_dfa[self.transition]) # "whitespace"
        if _input in self.table[self.currentState] and self.transition==0: #whitespace인 경우 다음것으로 넘어가기
            return "finish" #finish인 경우 다음 단어로 넘어갑니다

        if  _input not in self.table[self.currentState] and self.past==False: # 트랜지션 테이블에 해당하는 입력값이 없고 이전에 체크되던것이 없는 완전 새로운 단어인경우
            self.transition += 1 #다음 트랜지션 테이블을 찾으라고 1을 증가시키고
            return self.PeekNextState(_input,_dfa) #다음것을 찾아 떠난다
        if(_input not in self.table[self.currentState] and self.past==True):#만약에 해당 트랜지션테이블에 해당되는 것이 없는데 이전에 체크되던것이 있다. 예를들어 띄어쓰기를 안한 int a=2인 경우 a랑 =과 2를 다 따로 분리하기 위해서 만든 코드입니다
            
            self.lexeme+=_input 
            return "need_continue" # 이부분은 현재 단어는 그 이전까지의 테이블트랜지션과는 다르지만 다른 트랜지션테이블에 맞는지 체크하기위해서 다시 돌려보기 위해 씁니다
        if ('-' == _input): # -처리를 하기 위해 존재한다.
            if(self.digitletters): # -는 만약에 앞에 숫자나 문자가 처리되고 있었다면 그것은 마이너스의 의미로 사용되어야한다.(Operator)
                self.transition=4 # Operator Table번호
            else:
                self.transition=1 # 아닌경우는 음수의 의미인 정수이다.
            self.LoadTransitionTable(_dfa[self.transition]) # 그 테이블을 로드한다.

        if _input in self.table[self.currentState]: # 만약 그 인풋이 그 테이블에 있다면
            
            nextState = self.table[self.currentState][_input] # 다음 스테이트는 그 현재상테에서 입력값이 가야하는 스테이트를 바라본다
            self.past=True # 그리고 이제 문자가 처리중이니 past는 True
            self.lexeme += _input # 문자열에 그 문자들을 집어넣는다

            return nextState
 
    def SetState(self, _state): # 현재 스테이트 상태를 저장
        self.currentState = _state
    
    def IsAccepted(self): # 내가낸 결과물이 dfa에 있는지 확인
        if self.currentState in self.acceptedStates:
            return True
        else:
            return False
    

    def GetToken(self):
        
        if self.currentState in self.acceptedStates:
            if(self.acceptedStates[self.currentState]=="Integer" or self.acceptedStates[self.currentState]=="ID"):
                self.digitletters=True
            else:
                self.digitletters=False
                
            return self.acceptedStates[self.currentState]
        else:
            return "error"
 
 
    def Reset(self): # 초기화
        self.currentState = "T0" # 다시 스테이트 상태를 T0로 초기화
        self.transition = 0 # 현재 트렌지션은 0
        self.past=False # 이전에 들어온 값이 당연히 없어야하니 False
        self.lexeme = "" # 현재까지 저장된 문자열을 비워준다
        #self.digitletters=False

    

    

    