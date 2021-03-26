import sys
symbols={'int':'INT','float':'FLOAT','char':'CHAR','string':'STRING','boolean':'BOOLEAN',',':'COMMA',';':'SEMI','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN','+':'ADD','=':'Assign','-':'MINUS','*':'MUL','/':'DIV','<':'COMPARISON','>':'COMPARISON','==':'COMPARISON','!=':'COMPARISON','<=':'COMPARISON','>=':'COMPARISON','true':'TRUE','false':'FALSE'}
# "" : STR, '' : CHR
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}

with open('a.txt','r') as f:
