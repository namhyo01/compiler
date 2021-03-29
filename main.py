import string 
from automata import FiniteAutomaton
letter = list(string.ascii_lowercase)+list(string.ascii_uppercase)
digit = ['0','1','2','3','4','5','6','7','8','9',' ']
letters =letter + digit
tempo = ["'"]  #임시 수정
tempo2 = ['"'] #임시 수정
letters1 = letter + digit + tempo # "" 큰따옴표안에있는 작음따옴표를 만나면 unknown token으로 뜨길래 수정했음 이걸로 큰따옴표내에 있는 작은따옴표는 완전무시로 바꿈

dict_Literal = {key: "T1" for key in dict.fromkeys(letters1).keys()}
dict_Literal['"']="T2"
single_string = ['!', '@', '#', '$', '%', '^', '&', '*', "(", ')','-','+','=','/','|','.',',','?','~','`',' ',';',':','|']
letter+=['_']
dict_identifier = {key: "T1" for key in dict.fromkeys(letter).keys()} # 숫자가 들어가냐 안들어가냐
letters = letter + ['0','1','2','3','4','5','6','7','8','9',]
dict_identifier2 = {key: "T1" for key in dict.fromkeys(letters).keys()} # 숫자가 들어가냐 안들어가냐


white_space = [' ','\t','\n']
symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}

#c


whitespace = {
    "AcceptedStates":{
        "T1": "whitespace",
        "T2": "whitespace",
        "T3": "whitespace",
    },
    "Table":{
    "T0":{" ":"T1","\n":"T2","\t":"T3"},
    "T1":{},
    "T2":{},
    "T3":{}
    }
}
#dfa표
#Integer = {
#    "AcceptedStates":{
#        "T1": "Integer",
#        "T2": "Integer",
#        "T3": "Integer",
#    },
#    "Table":{
#    "T0":{"0":"T3","-":"T1","1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
#    "T1":{"1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
#    "T2":{"0":"T2","1":"T2","2":"T2","3":"T2","4":"T2","5":"T2","6":"T2","7":"T2","8":"T2","9":"T2"},
#    "T3":{}
#    }
#}
Integer = {
    "AcceptedStates":{
        "T1": "Integer",
        "T2": "Integer",
        #"T3": "Minus",
        "T4": "Integer"
    },
    "Table":{
    "T0":{"-":"T3","0":"T2","1":"T1","2":"T1","3":"T1","4":"T1","5":"T1","6":"T1","7":"T1","8":"T1","9":"T1"},
    "T1":{"0":"T1","1":"T1","2":"T1","3":"T1","4":"T1","5":"T1","6":"T1","7":"T1","8":"T1","9":"T1","a":"T6","b":"T6","c":"T6","d":"T6","e":"T6","f":"T6","g":"T6","h":"T6","i":"T6","j":"T6","k":"T6","l":"T6","m":"T6","n":"T6","o":"T6","p":"T6","q":"T6","r":"T6","s":"T6","t":"T6","u":"T6","v":"T6","w":"T6","x":"T6","y":"T6","z":"T6","A":"T6","B":"T6","C":"T6","D":"T6","E":"T6","F":"T6","G":"T6","H":"T6","I":"T6","J":"T6","K":"T6","L":"T6","M":"T6","N":"T6","O":"T6","P":"T6","Q":"T6","R":"T6","S":"T6","T":"T6","U":"T6","V":"T6","W":"T6","X":"T6","Y":"T6","Z":"T6","_":"T6"},
    "T2":{"0":"T5","1":"T5","2":"T5","3":"T5","4":"T5","5":"T5","6":"T5","7":"T5","8":"T5","9":"T5","a":"T6","b":"T6","c":"T6","d":"T6","e":"T6","f":"T6","g":"T6","h":"T6","i":"T6","j":"T6","k":"T6","l":"T6","m":"T6","n":"T6","o":"T6","p":"T6","q":"T6","r":"T6","s":"T6","t":"T6","u":"T6","v":"T6","w":"T6","x":"T6","y":"T6","z":"T6","A":"T6","B":"T6","C":"T6","D":"T6","E":"T6","F":"T6","G":"T6","H":"T6","I":"T6","J":"T6","K":"T6","L":"T6","M":"T6","N":"T6","O":"T6","P":"T6","Q":"T6","R":"T6","S":"T6","T":"T6","U":"T6","V":"T6","W":"T6","X":"T6","Y":"T6","Z":"T6","_":"T6"},
    "T3":{"1":"T4","2":"T4","3":"T4","4":"T4","5":"T4","6":"T4","7":"T4","8":"T4","9":"T4"},
    "T4":{"0":"T4","1":"T4","2":"T4","3":"T4","4":"T4","5":"T4","6":"T4","7":"T4","8":"T4","9":"T4","a":"T6","b":"T6","c":"T6","d":"T6","e":"T6","f":"T6","g":"T6","h":"T6","i":"T6","j":"T6","k":"T6","l":"T6","m":"T6","n":"T6","o":"T6","p":"T6","q":"T6","r":"T6","s":"T6","t":"T6","u":"T6","v":"T6","w":"T6","x":"T6","y":"T6","z":"T6","A":"T6","B":"T6","C":"T6","D":"T6","E":"T6","F":"T6","G":"T6","H":"T6","I":"T6","J":"T6","K":"T6","L":"T6","M":"T6","N":"T6","O":"T6","P":"T6","Q":"T6","R":"T6","S":"T6","T":"T6","U":"T6","V":"T6","W":"T6","X":"T6","Y":"T6","Z":"T6","_":"T6"},
    "T5":{"0":"T5","1":"T5","2":"T5","3":"T5","4":"T5","5":"T5","6":"T5","7":"T5","8":"T5","9":"T5","a":"T6","b":"T6","c":"T6","d":"T6","e":"T6","f":"T6","g":"T6","h":"T6","i":"T6","j":"T6","k":"T6","l":"T6","m":"T6","n":"T6","o":"T6","p":"T6","q":"T6","r":"T6","s":"T6","t":"T6","u":"T6","v":"T6","w":"T6","x":"T6","y":"T6","z":"T6","A":"T6","B":"T6","C":"T6","D":"T6","E":"T6","F":"T6","G":"T6","H":"T6","I":"T6","J":"T6","K":"T6","L":"T6","M":"T6","N":"T6","O":"T6","P":"T6","Q":"T6","R":"T6","S":"T6","T":"T6","U":"T6","V":"T6","W":"T6","X":"T6","Y":"T6","Z":"T6","_":"T6"},
    "T6":{"0":"T6","1":"T6","2":"T6","3":"T6","4":"T6","5":"T6","6":"T6","7":"T6","8":"T6","9":"T6","a":"T6","b":"T6","c":"T6","d":"T6","e":"T6","f":"T6","g":"T6","h":"T6","i":"T6","j":"T6","k":"T6","l":"T6","m":"T6","n":"T6","o":"T6","p":"T6","q":"T6","r":"T6","s":"T6","t":"T6","u":"T6","v":"T6","w":"T6","x":"T6","y":"T6","z":"T6","A":"T6","B":"T6","C":"T6","D":"T6","E":"T6","F":"T6","G":"T6","H":"T6","I":"T6","J":"T6","K":"T6","L":"T6","M":"T6","N":"T6","O":"T6","P":"T6","Q":"T6","R":"T6","S":"T6","T":"T6","U":"T6","V":"T6","W":"T6","X":"T6","Y":"T6","Z":"T6","_":"T6"},#문자에 숫자가 나오는경우
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
        "T1": "ID", # 식별자가 문자만받은경우
        "T2": "ID"  # 식별자가 정수로 끝나는경우 letter를 다시받으면 멸망
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
dict_Character = {key: "T2" for key in dict.fromkeys(letter+digit+single_string+tempo2).keys()}  # tempo2를 추가로 받게해서 '"' 를인식하게함 작은따옴표내에 있는 큰따옴표
dict_Character["'"]="T4"
dict_Character2 = {key: "T3" for key in dict.fromkeys(letter+digit+single_string).keys()}
dict_Character2["'"]="T4"

Single = {            # 작은따옴표 한번해봤음 아직안됨 '인식을못함 수정할예정
    "AcceptedStates":{
        #"T1": "Error",
        "T4": "Single_Character",
                           
    },
    "Table":{
    "T0":{"'":"T1"},
    "T1":dict_Character,                   
    "T2":dict_Character2,
    "T3":{key: "T3" for key in dict.fromkeys(letter+digit+single_string+["'"]).keys()},
    "T4":{}
    }
}




transitiontable =[whitespace, Integer, Literal, ID, Operator, Comparioson, PAIRToken, Single, OtherToken]



# DFA를 ARITHMETIC_OPERATOR로 초기화

dfa = FiniteAutomaton()

#에러사항 '*'같은거 할시 이상한 걸로 출력


with open('words.txt','r') as f:
    lines = f.readlines()
        # brackets = [  ] # ()
        # sbrackets = [  ] # {}
        # lsbrackets = [  ] # []
     
         # if character == '(':              # 단일문자가 lines 인지 character인지 몰라서 일단 lines 라 하고 여기다 집어넣음
        #     brackets.append('1'))       
        # if character == ')':
        #       if len(brackets) == 0   # 만약 () 스택에 넣어진게 없을때 )를받으면
        #           return -1    # 오류
        #       else       
        #           brackets.remove('1')
        # if character == '{':
        #     sbrackets.append('2'))
        # if character == '}':
        #       if len(sbrackets) == 0      # 만약 {} 스택에 없으면
        #            return -1              # 오류처리
        #       else
        #           sbrackets.remove('2')
        # if characters == '[':
        #     lsbrackets.append('3'))
        # if character == ']':
        #       if len(lsbrackets) == 0     # 만약 [] 스택에 없으면
        #           return -1               #오류처리
        #       else
        #           lsbrackets.remove('3')

    for line in lines: #이 라인 을 파싱할거다

        line+='\n'
        #print(line)
        dfa.digitletters=False
        for i,character in enumerate(line):
            #print(character)
            #if(i==(len(line)-1)):
            #    nextState=dfa.PeekNextState(character,transitiontable,1)
            #else:
            #    nextState=dfa.PeekNextState(character,transitiontable)
            #if(i==(len(line)-1)):
             #   nextState=dfa.PeekNextState(character,transitiontable,1)
            #else:
            nextState=dfa.PeekNextState(character,transitiontable)
            if(nextState=="에러"):
                print("에러")
                exit()
            if(nextState!="finish"):
                #lexeme+=character
                dfa.SetState(nextState)
            else:#끝난경우
                if(dfa.lexeme!=""):
                    print(dfa.GetToken(),dfa.lexeme)
                #print(dfa.GetToken(),dfa.lexeme)
                dfa.Reset()
            #dfa.Reset()
# if len(brackets)!=0 or len(brackets)!=0 or len(brackets)!=0 # 파일읽기가 끝났을때 스택에 하나라도 남았으면
# return -1  # 오류처리