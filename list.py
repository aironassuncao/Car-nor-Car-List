funcionarios = ['ana', 'rodrigo', 'thiago', 'sofia', 'amanda', 'fabio']
turnoNoite = ['ana', 'sofia', 'amanda']
turnoDia = ['rodrigo', 'thiago', 'fabio']
temCarro = ['ana', 'rodrigo', 'amanda']

temCarro_noite = set(temCarro).intersection(turnoNoite)
print(temCarro_noite)

temCarro_dia = set(temCarro).intersection(turnoDia)
print(temCarro_dia)

naoTemCarro = set(funcionarios).difference(temCarro)
print(naoTemCarro)
