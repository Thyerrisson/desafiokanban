from processamento import processar_alunos

lista_de_alunos = [
    ("Hugo Souza", [8.5, 7.0, 9.0]),
    ("Jesse Lingard", [6.0, 5.5]),
    ("Memphis Depay", [4.0, 3.5, 5.0, 4.5]),
    ("Kaio Cesar", [9.5, 10.0, 9.8]),
    ("Yuri Alberto", [])  
]

alunos_em_recuperacao, top_student = processar_alunos(lista_de_alunos)

