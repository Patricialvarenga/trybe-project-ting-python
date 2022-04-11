# Fonte: repositório das aulas ao vivo


class Queue:
    FIRST_ELEMENT = 0  # Guardião da posição do elemento

    def __init__(self):
        self._data = []  # iniciando uma classe, local onde armazena a fila

    def __len__(self):
        return len(self._data)  # tamanho do ou imprimir toda a fila

    def enqueue(self, value):
        if value not in self._data:
            self._data.append(value)  # método q faz o push no fim da fila

    def dequeue(self):  # remove do início da fila
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):  # método faz a busca e lança exceção se inválido
        if (index < 0 or index >= len(self._data)):
            raise IndexError()
        else:
            return self._data[index]
