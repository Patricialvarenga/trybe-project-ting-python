# Fonte: https://app.betrybe.com/course/computer-science/estrutura-de-dados-ii/
# no-e-listas-encadeadas  Implementação de uma LinkedList
from ting_file_management.node import Node


# Devemos informar que o elemento que estamos inserindo seja o novo head_value
class LinkedList:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length
#  o next será preenchido com o valor que está atualmente na head_value ,
# para que o novo valor, que estamos inserindo no início da lista,
# seja preenchido na variável head_value , se tornando a "cabeça" da lista

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

# Devemos informar que o elemento que estamos inserindo
# seja o último na nossa estrutura de cadeia de Nodes
# head_value ainda não possui valor. Para corrigir essa lógica,
# podemos utilizar a função insert_first escrita previamente.
    def insert_last(self, value):
        last_value = Node(value)
        current_value = self.head_value

        if self.is_empty():
            return self.insert_first(value)

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1

# Se o elemento tem a posição inferior a 1 ,
# será adicionado na posição inicial, utilizando a função insert_first.
# Se o elemento tem a posição igual ou superior a quantidade de elementos,
# será adicionado na posição final, utilizando a função insert_last.
    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.head_value
        while position > 1:
            current_value = current_value.next
            position -= 1
        next_value = Node(value)
        next_value.next = current_value.next
        current_value.next = next_value
        self.__length += 1

# Devemos fazer com que a nossa estrutura remova a "cabeça",
# em casos de estrutura vazia, devemos retornar None.
# fazemos com que o elemento next passe a ser o primeiro elemento,S
# já que a head_value irá referenciá-lo
    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

# informar que o elemento que estamos removendo
#  seja o último da nossa estrutura de cadeia de Nodes
    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()

        previous_to_be_removed = self.head_value

        while previous_to_be_removed.next.next:
            previous_to_be_removed = previous_to_be_removed.next

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = None
        self.__length -= 1
        return value_to_be_removed

# Se o elemento tem a posição inferior a 1 ,
# será removido na posição inicial, utilizando a função remove_first.
# Se o elemento tem a posição igual ou superior a quantidade de elementos,
# será removido na posição final, utilizando a função remove_last
    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.head_value

        while position > 1:
            previous_to_be_removed = previous_to_be_removed.next
            position -= 1

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self.__length -= 1

        return value_to_be_removed

# informar a posição do elemento que desejamos visualizar o conteúdo,
# esta função deve retornar uma cópia do Node existente em nossa estrutura.
# Se o elemento tem a posição inferior a 1 ,
# será retornado o conteúdo da posição inicial.
# Se o elemento tem a posição igual ou superior a quantidade de elementos,
# será retornado o conteúdo da posição final.
    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.head_value
        if 0 < position >= len(self) or position < 0:
            raise IndexError
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
                return value_returned
        else:
            raise IndexError

# informar se a estrutura está vazia
# O uso do not neste contexto nos informa se a estrutura está vazia,
# já que not 0 == True
    def is_empty(self):
        return not self.__length
