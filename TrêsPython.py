nome = input('Nome do aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('Somando {:.1f}, {:.1f}, {:.1f} e {:.1f}, a média do aluno {} é {:.1f}'.format(nota1, nota2, nota3, nota4, nome, media))
if media <6:
    print('O aluno {} está REPROVADO.'.format(nome))
elif media >=6:
    print('O aluno {} está APROVADO.'.format(nome))