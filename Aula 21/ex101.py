def voto(nasc):
    from datetime import date
    id = date.today().year - nasc
    if id < 16:
        return f'Você esta com {id} anos: VOTO NEGADO.'
    elif 18 <= id < 65:
        return f'Você esta com {id} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Você esta com {id} anos: VOTO OPCIONAL.'


print(voto(int(input('Digite o ano de nascimento: '))))