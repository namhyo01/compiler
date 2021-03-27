import string 
from automata import FiniteAutomaton
letter = list(string.ascii_lowercase)+list(string.ascii_uppercase)
digit = ['0','1','2','3','4','5','6','7','8','9',' ']
letters =letter + digit

dict_Literal = {key: "T1" for key in dict.fromkeys(letters).keys()}
dict_Literal['"']="T2"
single_string = ['!', '@', '#', '$', '%', '^', '&', '*', "(", ')','-','+','=','/','|','.',',','?','~','`',' ']
letter+=['_']
dict_identifier = {key: "T1" for key in dict.fromkeys(letter).keys()} # 숫자가 들어가냐 안들어가냐
letters = letter + ['0','1','2','3','4','5','6','7','8','9',]
dict_identifier2 = {key: "T1" for key in dict.fromkeys(letters).keys()} # 숫자가 들어가냐 안들어가냐

white_space = [' ','\t','\n']
symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}

#c


#whitespace = {
#    "AcceptedStates":{
#        "T1": "whitespace",
#        "T2": "whitespace",
#        "T3": "whitespace",
#    },
#    "Table":{
#    "T0":{" ":"T1","\n":"T2","\t":"T3"},
#    "T1":{" ":"","\n":"","\t":""},
#    "T2":{" ":"","\n":"","\t":""},
#    "T3":{" ":"","\n":"","\t":""}
#    }
#}
#dfa표
Integer = {
    "AcceptedStates":{
        "T1": "Integer",
        #"T2": "Zero",
        #"T3": "Minus",
        "T4": "Negative integer"
    },
    "Table":{
    "T0":{"-":"T3","0":"T2","1":"T1","2":"T1","3":"T1","4":"T1","5":"T1","6":"T1","7":"T1","8":"T1","9":"T1"},
    "T1":{"0":"T1","1":"T1","2":"T1","3":"T1","4":"T1","5":"T1","6":"T1","7":"T1","8":"T1","9":"T1"},
    "T2":{},
    "T3":{"1":"T4","2":"T4","3":"T4","4":"T4","5":"T4","6":"T4","7":"T4","8":"T4","9":"T4"},
    "T4":{"0":"T4","1":"T4","2":"T4","3":"T4","4":"T4","5":"T4","6":"T4","7":"T4","8":"T4","9":"T4"},
    }
}

Literal = {
    "AcceptedStates":{
        #"T1": "Error",
        "T2": "Literal_String",
        
    },
    "Table":{
    "T0":{'"':"T1"},
    "T1":dict_Literal,
    "T2":{},
    }
}
ID = {
    "AcceptedStates":{
        "T1": "ID",
    },
    "Table":{
    "T0":dict_identifier, #_빼먹었다
    "T1":dict_identifier2,
    }
}

Operator = {
    # 산술연산자
    "AcceptedStates": {
        "T1": "ADD",
        "T2": "MINUS",
        "T3": "MUL",
        "T4": "DIVIDE"
    },
    "Table": {
        "T0": {"+": "T1", "-": "T2", "*": "T3", "/": "T4"},
        "T1": { },
        "T2": { },
        "T3": { },
        "T4": { },
    }
}

Comparioson = {
    # 비교
    "AcceptedStates": {
        "T1": "ASSIGN",
        "T2": "COMPARISON",
        "T3": "COMPARISON",
        "T4": "COMPARISON",
        "T5": "COMPARISON",
        "T6": "COMPARISON",
        "T7": "COMPARISON",
        
    },
    "Table": {
        "T0": {"=": "T1", ">": "T2", "<": "T3", "!": "T8"},
        "T1": {"=": "T4",},
        "T2": {"=": "T6",},
        "T3": {"=": "T7",},
        "T4": {},
        "T5": {},
        "T6": {},
        "T7": {},
        "T8": {"=": "T5" },
    }
}

PAIRToken={
    "AcceptedStates": {
        "T1": "LPAREN",
        "T2": "LB",
        "T3": "LSB",
        "T4": "RPAREN",
        "T5": "RB",
        "T6": "RBP",

    },
    "Table": {
        "T0": {"(": "T1", "{": "T2", "[": "T3", ")": "T4","}":"T5","]":"T6"},
        "T1": {},
        "T2": {},
        "T3": {},
        "T4": {},
        "T5": {},
        "T6": {},
    }
}

OtherToken={
    "AcceptedStates": {
        "T1": "COMMA",
        "T2": "SEMI",

    },
    "Table": {
        "T0": {",":"T1",";":"T2"},
        "T1": {},
        "T2": {},
    }
}

#dict_Character = {key: "T1" for key in dict.fromkeys(letter).keys()}
dict_Character = {key: "T1" for key in dict.fromkeys(letter+digit+single_string).keys()}
dict_Character["'"]="T2"
Single = {            # 작은따옴표 한번해봤음 아직안됨 '인식을못함 수정할예정
    "AcceptedStates":{
        #"T1": "Error",
        "T2": "Single_Character",
                           
    },
    "Table":{
    "T0":{"'":"T1"},
    "T1":dict_Character,
    "T2":{},
    
    }
}
#작은따음표 아직 ㅎ



transitiontable =[Integer, Literal, ID,Operator,Comparioson,PAIRToken, OtherToken,Single]



# DFA를 ARITHMETIC_OPERATOR로 초기화

dfa = FiniteAutomaton()

#에러사항 '*'같은거 할시 이상한 걸로 출력
input_string= "0025"


lexeme = ""
for i,character in enumerate(input_string):

    if character not in white_space:

        if(i==(len(input_string)-1)):
            nextState=dfa.PeekNextState(character,transitiontable,1)
        else:
            nextState=dfa.PeekNextState(character,transitiontable)
        if(nextState=="에러"):
            print("에러")
            exit()
        if(nextState!="finish"):
            #lexeme+=character
            dfa.SetState(nextState)
        else:#끝난경우
            
            print(dfa.GetToken(),dfa.lexeme)
            
            dfa.Reset()

    else:
        if(dfa.lexeme!=""):
            print(dfa.GetToken(),dfa.lexeme)
        dfa.Reset()

