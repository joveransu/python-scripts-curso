def CenterLine(txt, tamanho=0, lineExtra=False):
    if tamanho == 0:
        tam = len(txt) + 4
    else:
        tam = tamanho

    line1 = '=' * tam
    conteudo = txt.center(tam)

    if lineExtra:
        final_text = f"""
{line1}
{conteudo}    
{line1}
"""
    else:
        final_text = conteudo

    return final_text