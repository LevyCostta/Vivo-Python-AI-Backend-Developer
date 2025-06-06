import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope

@meu_decorador
def ola_mundo(nome, qualquer_coisa):
    print(f'Olá Mundo {nome}!')

print(ola_mundo.__name__)
