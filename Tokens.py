symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
parser_symbols={',':'COMMA',';':'SEMI','+':'ADD','=':'Assign','-':'MINUS','*':'MUL','/':'DIV','<':'COMPARISON','>':'COMPARISON','==':'COMPARISON','!=':'COMPARISON','<=':'COMPARISON','>=':'COMPARISON'}

# "" : STR, '' : CHR
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}


white_space = [' ','\t','\n']
for i,character in enumerate(input_string):
    
    dfa.LoadTransitionTable(transitiontable[transition])    
    nextState = dfa.PeekNextState(character)
    if(nextState!="finish"):
        dfa.SetState(nextState)
    elif(nextState="change"):

    else:
        print("토큰이 {}로 분류되었습니다.".format(dfa.GetToken()))
        dfa.Reset()
        
print("토큰이 {}로 분류되었습니다.".format(dfa.GetToken()))
# dfa를 사용을 마쳤으면 종료
dfa.Reset()
print("-----------")