from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines_in_file = txt_importer(path_file)
    content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines_in_file),
            "linhas_do_arquivo": lines_in_file,
    }
    print(content, file=sys.stdout)
    instance.enqueue(path_file)
    return content
# https://pythonguides.com/python-stderr-stdin-and-stdout/
# Python stdout é conhecido como saída padrão.
# Possui função write imprimi diretamente qualquer string.


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
