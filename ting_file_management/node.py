# Fonte: https://app.betrybe.com/course/computer-science/estrutura-de-dados-ii
# /no-e-listas-encadeadas  Implementação de um Node

class Node:
    def __init__(self, value):
        self.value = value   # dado a ser armazenado
        self.next = None   # forma de apontar para outro nó
