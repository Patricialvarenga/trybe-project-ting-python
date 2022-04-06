# módulo para recebermos valores externos
import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                lines = file.read()
                return lines.split('\n')
        except OSError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return print("Formato inválido", file=sys.stderr)
# file=sys.stderr: modificar a saída padrão para a saída de erros
