def word_occurrences(lines, word):
    occurrences = []
    for line_index, line in enumerate(lines):
        if (word.lower() in line.lower()):
            occurrences.append({'linha': line_index + 1})
    return occurrences


def search_file(instance):
    len_files = len(instance)
    instance_index = 0
    files_list = []

    if len_files:
        while instance_index < len_files:
            file = instance.search(instance_index)
            files_list.append(file)
            instance_index += 1
    return files_list


def exists_word(word, instance):
    exists_word_report = search_file(instance)
    formated_list = []
    if not exists_word_report:
        return []
    for file in exists_word_report:
        lines = file['linhas_do_arquivo']
        occurrences = word_occurrences(lines, word)
        if occurrences:
            formated_list.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": occurrences
            })
    return formated_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
