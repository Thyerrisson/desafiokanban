def validar_notas(notas):
    return len(notas) > 0

def calcular_media(notas):
    if not validar_notas(notas):
        return "dados inválidos"
    media_calculada = sum(notas) / len(notas)
    if media_calculada < 5:
        return "reprovado"
    elif media_calculada < 7:
        return "recuperação"
    elif media_calculada <= 9:
        return "aprovado"
    else:
        return "Aluno exemplar!"

def processar_alunos(alunos):
    alunos_em_recuperacao = []  
    medias_dos_alunos = {}
    
    for nome_do_aluno, lista_de_notas in alunos:  
        if validar_notas(lista_de_notas):
            media_calculada = sum(lista_de_notas) / len(lista_de_notas)
            medias_dos_alunos[nome_do_aluno] = media_calculada
            if media_calculada < 7:
                alunos_em_recuperacao.append((nome_do_aluno, media_calculada))
        else:
            medias_dos_alunos[nome_do_aluno] = "dados inválidos"
    
    nome_do_top = "Nenhum"
    media_do_top = 0
    for nome_atual, valor_atual in medias_dos_alunos.items():
        if isinstance(valor_atual, (int, float)) and valor_atual > media_do_top:
            nome_do_top = nome_atual
            media_do_top = valor_atual
    top_student = (nome_do_top, media_do_top)
    
    return alunos_em_recuperacao, top_student


