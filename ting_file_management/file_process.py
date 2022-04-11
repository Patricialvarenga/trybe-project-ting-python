from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines_in_file = txt_importer(path_file)
    content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines_in_file),
            "linhas_do_arquivo": lines_in_file,
    }
    instance.enqueue(content)
    print(content, file=sys.stdout)
# https://pythonguides.com/python-stderr-stdin-and-stdout/
# Python stdout é conhecido como saída padrão.
# Possui função write imprimi diretamente qualquer string.


def remove(instance):
    file_to_remove = instance.dequeue()
    if not file_to_remove:
        print("Não há elementos", file=sys.stdout)
    else:
        file_removed_ok = file_to_remove["nome_do_arquivo"]
        print(
            f"Arquivo {file_removed_ok} removido com sucesso", file=sys.stdout
            )


def file_metadata(instance, position):
    try:
        position_item_ok = instance.search(position)
        print(position_item_ok)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
