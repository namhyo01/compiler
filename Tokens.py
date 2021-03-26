symbols={'int':'INT','char':'CHAR','string':'STRING','boolean':'BOOLEAN','true':'TRUE','false':'FALSE','if':'IF','else':'ELSE','while':'WHILE','class':'CLASS','return':'RETURN'}
parser_symbols={',':'COMMA',';':'SEMI','+':'ADD','=':'Assign','-':'MINUS','*':'MUL','/':'DIV','<':'COMPARISON','>':'COMPARISON','==':'COMPARISON','!=':'COMPARISON','<=':'COMPARISON','>=':'COMPARISON'}

# "" : STR, '' : CHR
open_symbols={'{':'LB','(':'LPAREN','[':'LSB'}
close_symbols={'}':'RB',')':'RPAREN',']':'RSB'}
white_space = [' ','\t','\n']
