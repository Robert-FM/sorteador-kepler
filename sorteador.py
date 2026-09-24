from random import randint


def sorteador(num_a: int, num_b: int) -> int:
    if num_a > num_b:
        raise ValueError('O limite mínimo não pode ser maior que o máximo.')

    return randint(num_a, num_b)
