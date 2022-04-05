from ting_file_management.linked_list_content import LinkedList


# Fonte: https://app.betrybe.com/course/  , gabarito, exercício 2 bônus
class Queue:
    def __init__(self):
        self.__data = LinkedList()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.insert_last(value)

    def dequeue(self):
        return self.__data.remove_first().value

    def search(self, index):
        try:
            return self.__data.get_element_at(index).value
        except IndexError:
            raise IndexError
