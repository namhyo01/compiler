import string 
from automata import FiniteAutomaton
import sys
from Tokens import *


transitiontable =[whitespace, Integer, Literal, ID, Operator, Comparioson, PAIRToken, Single, OtherToken]#Tramsition Table


dfa = FiniteAutomaton() # 실행



filename = sys.argv[1]
output_file = filename + '_output.txt'

with open(filename,'r') as f:
    f2 = open(output_file,'w')
    lines = f.readlines()

    line_num = 1 # 파일 줄수
    for line in lines: #이 라인 을 파싱할거다
        
        line+='\n' # 파일에서 읽어올때 '\n'을 지워버려서 어차피 의미 없는 '\n'을 넣어(whitespace) 좀 쉽게 그 문자열의 끝임을 표시하였습니다
        
        dfa.digitletters=False
        for i,character in enumerate(line): 
            
            nextState=dfa.PeekNextState(character,transitiontable) #dfa랑 맞는 지 실행 
            
            if nextState=="need_continue": # need continue인경우는 다시 단어를 집어넣어서 실행해주어야하ㅑㄴ다.
                if(dfa.lexeme!=""): # 문자열이 비어있지않는 경우
                    
                    if dfa.GetToken() == "error": #만약에 에러시
                        error_string = str(line_num)+"th file's line errors ERROR TOKEN VARIABLE  "  + str(dfa.lexeme) + ' in this '+str(line) # 파일에서 몇번째 줄에 어떤 문맥이 어떤 문자열에서 에러가 나는지 보여준다.
                        f2.write(error_string)
                        f2.close()
                        exit() # 프로그램 종료

                    dfa.lexeme = dfa.lexeme[:-1]#마지막은 무쓸모        
                    out = dfa.GetToken()
                    out+='\t'+dfa.lexeme+ '\n' # 파일에 잘보여드릴려고 '\t'와 '\n'을 넣어 보여드렸습니다.
                    f2.write(out)
                    
                dfa.Reset() #dfa초기화
                nextState=dfa.PeekNextState(character,transitiontable) #다시 그 단어를 집어넣는다.
            if(nextState=="error"): # 다음 스테이트가 에러라면
                
                error_string = str(line_num)+"th file's line errors ERROR TOKEN VARIABLE  "  + str(dfa.lexeme) + ' in this '+str(line)
                f2.write(error_string)
                f2.close()
                
                exit()
            if(nextState!="finish"):#finish가 아닌경우 state를 다음 state로 설정한다
                dfa.SetState(nextState)
            else:#끝난경우 즉 finish인 경우(white space인 경우)
                if(dfa.lexeme!=""):
                    if dfa.GetToken() == "error":
                        error_string = str(line_num)+"th line errors ERROR TOKEN VARIABLE  "   + str(dfa.lexeme) + ' in this '+str(line)
                        f2.write(error_string)
                        f2.close()
                        exit()
                    out = dfa.GetToken()
                    out+='\t'+dfa.lexeme + '\n'
                    f2.write(out)
                dfa.Reset()
        line_num += 1 # line줄수 증가
    f2.close()

