import string 
from asd import FiniteAutomaton
letter = list(string.ascii_lowercase)+list(string.ascii_uppercase)
digit = ['0','1','2','3','4','5','6','7','8','9',' ']
letters =letter+ digit

dict_Literal = {key: "T1" for key in dict.fromkeys(letters).keys()}
dict_Literal['"']="T2"
dict_identifier = {key: "T1" for key in dict.fromkeys(letter).keys()}
letters = letter + ['0','1','2','3','4','5','6','7','8','9','_']
dict_identifier2 = {key: "T1" for key in dict.fromkeys(letters).keys()}

white_space = [' ','\t','\n']
symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}




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
Integer = {
    "AcceptedStates":{
        "T1": "Integer",
        "T2": "Integer",
        "T3": "Integer",
    },
    "Table":{
    "T0":{"0":"T3","-":"T1","1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
    "T1":{"1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
    "T2":{"0":"T2","1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
    "T3":{"0":""}
    }
}

Literal = {
    "AcceptedStates":{
        "T1": "Literal_String",
        "T2": "Literal_String",
        
    },
    "Table":{
    "T0":{'"':"T0"},
    "T1":dict_Literal,
    "T2":{'"':""},
    }
}
ID = {
    "AcceptedStates":{
        "T1": "ID",
    },
    "Table":{
    "T0":dict_identifier,
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
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T2": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T3": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T4": {"+": "",   "-": "",   "*": "",   "/": ""  },
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
        "T0": {"=": "T1", ">": "T2", "<": "T3", "==": "T4","!=":"T5",">=":"T6","<=":"T7"},
        "T1": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
        "T2": {"=": "",   ">": "",   "<": "",   "==": ""  ,"!=":"",">=":"","<=":""},
        "T3": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
        "T4": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
        "T5": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
        "T6": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
        "T7": {"=": "",   ">": "",   "<": "",   "==": "" , "!=":"",">=":"","<=":""},
    }
}
OtherToken={
    "AcceptedStates": {
        "T1": "LPAREN",
        "T2": "LB",
        "T3": "LSB",
        "T4": "RPAREN",
        "T5": "RB",
        "T6": "RBP",
        "T7": "COMMA",
        "T8": "SEMI"
    },
    "Table": {
        "T0": {"(": "T1", "{": "T2", "[": "T3", ")": "T4","}":"T5","]":"T6",",":"T7",";":"T8"},
        "T1": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T2": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T3": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T4": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T5": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T6": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T7": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
        "T8": {"(": "",   "{": "",   "[": "",   ")": "" , "}":"","]":"",",":"",";":""},
    }
}


#작은따음표 아직 ㅎ



transitiontable =[whitespace, Integer, Literal, ID,Operator,Comparioson,OtherToken]



# DFA를 ARITHMETIC_OPERATOR로 초기화

dfa = FiniteAutomaton()


input_string="adsdsds+dasds"


lexeme = ""
for i,character in enumerate(input_string):
    if character not in white_space:
        dfa.PeekNextState(character,transitiontable)
    else:
        dfa.Reset()

