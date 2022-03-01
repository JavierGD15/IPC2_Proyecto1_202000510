from graphviz import Digraph, Graph

x = ""
y = '''<TD BGCOLOR="white"><FONT >line3</FONT></TD>'''
tr_inicio = '''<TR>'''
tr_fin = '''</TR>'''
cuerpo = ""

for i in range(4):
    for j in range(4):
        if j == 2 or i == 3:
            x = x+'''<TD BGCOLOR="black"><FONT COLOR="white">line2</FONT></TD>'''
        else:
            x = x+'''<TD BGCOLOR="white"><FONT >line2</FONT></TD>'''
    
    cuerpo = cuerpo +tr_inicio+x+tr_fin
    x = ""
    
            



dot = Digraph(filename='Grafica de pisos', format= 'png')
#generar tabla

dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
			
            '''+cuerpo+'''

    </TABLE>>''')

dot.view()