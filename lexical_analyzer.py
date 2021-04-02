import string 
from automata import FiniteAutomaton
import sys
from Tokens import *




transitiontable =[whitespace, Integer, Literal, ID, Operator, Comparioson, PAIRToken, Single, OtherToken]



# DFA를 ARITHMETIC_OPERATOR로 초기화

dfa = FiniteAutomaton()

#에러사항 '*'같은거 할시 이상한 걸로 출력

filename = sys.argv[1]
output_file = filename + '_output.txt'

with open(filename,'r') as f:
    f2 = open(output_file,'w')
    lines = f.readlines()

    line_num = 1 # 파일 줄수
    for line in lines: #이 라인 을 파싱할거다
        
        line+='\n' # 그 줄의 마지막을 의미
        
        dfa.digitletters=False
        for i,character in enumerate(line):
            
            nextState=dfa.PeekNextState(character,transitiontable)
            
            if nextState=="need_continue":
                if(dfa.lexeme!=""):
                    #print(dfa.GetToken())
                    if dfa.GetToken() == "error":
                        error_string = str(line_num)+"th file's line errors ERROR TOKEN VARIABLE  "  + str(dfa.lexeme) + ' in this '+str(line)
                        f2.write(error_string)
                        f2.close()
                        exit()
                    dfa.lexeme = dfa.lexeme[:-1]        
                    out = dfa.GetToken()
                    out+='\t'+dfa.lexeme+ '\n'
                    f2.write(out)
                    #print(dfa.GetToken(),dfa.lexeme)
                dfa.Reset()
                nextState=dfa.PeekNextState(character,transitiontable)
            if(nextState=="error"):
                #print('hi')
                error_string = str(line_num)+"th file's line errors ERROR TOKEN VARIABLE  "  + str(dfa.lexeme) + ' in this '+str(line)
                f2.write(error_string)
                f2.close()
                #print(line_num, "th line errors ERROR UNKNOWN TOKEN VARIABEL",sep='')
                exit()
            if(nextState!="finish"):
                dfa.SetState(nextState)
            else:#끝난경우
                if(dfa.lexeme!=""):
                    if dfa.GetToken() == "error":
                        #print(character)
                        error_string = str(line_num)+"th line errors ERROR TOKEN VARIABLE  "   + str(dfa.lexeme) + ' in this '+str(line)
                        f2.write(error_string)
                        f2.close()
                        exit()
                    out = dfa.GetToken()
                    out+='\t'+dfa.lexeme + '\n'
                    f2.write(out)
                    #print(dfa.GetToken(),dfa.lexeme)
                dfa.Reset()
        line_num += 1 # line줄수 증가
    f2.close()