import sys
import re
symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
parser_symbols={',':'COMMA',';':'SEMI','+':'ADD','=':'Assign','-':'MINUS','*':'MUL','/':'DIV','<':'COMPARISON','>':'COMPARISON','==':'COMPARISON','!=':'COMPARISON','<=':'COMPARISON','>=':'COMPARISON'}

# "" : STR, '' : CHR
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}

def check_symbols(word): #아직 큰따음표 작은따음표 못함
    if word in symbols:
        print(symbols[word])
    elif '0'<=word[0]<='9': #숫자로 시작하는 경우 아직 음수는 체크 안함
        
        num = ""
        for i in word:
            if('0'<=i<='9'):
                num+=i
            else: # 즉 오류
                print('error')
                return -1
        print('INTEGER',num)
    elif 'A'<=word[0]<='Z' or 'a'<=word[0]<='z' or word[0]=='_': #이건 식별자
        print("ID",word)

        

def parser(word):
    start = 0
  #  print("special",word)
    
    for i in range(len(word)):
        
        if word[i] in parser_symbols:
            if(start==i):
                print(parser_symbols[word[i]])
                return
            check_symbols(word[start:i])
            print(parser_symbols[word[i]])
            start = i+1
        elif word[i] in open_symbols:
            if(start==i):
                print(open_symbols[word[i]])
                return
            check_symbols(word[start:i])
            print(open_symbols[word[i]])
            if word[i+1:] in symbols:
                print(symbols[word[i+1:]])
                return

            start=i+1
        elif word[i] in close_symbols:
            if(start==i):
                print(close_symbols[word[i]])
                return
            check_symbols(word[start:i])
            print(close_symbols[word[i]])
            start=i+1
    if(start<(len(word)-1)):
        check_symbols(word[start:len(word)])
    elif(start==len(word)-1):
        check_symbols(word[start])


#구현해야하는것이 여러가지가있다 특히 식별자(ID)랑 정수는 아직 구현 안함
with open('words.txt','r') as f:
    lines = f.readlines()
    for line in lines: #이 라인 을 파싱할거다
        #line = str(line)
        line.strip()
        words = line.split()
        #print(words)
        for word in words:
            
            if(word in symbols):
                print(symbols[word])
            else:
                parser(word)
#        print(words)

