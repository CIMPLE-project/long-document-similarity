import re


# min_length = 120
# typical_length = 160
# max_length = 200


def split_line(line):
    line = line.strip()
    sentences = re.split(r'[\.!\?]', line)
    return [sentence.strip() for sentence in sentences if len(sentence) > 0]


def split_file(file_name:str, mode:str='p')->[str]:
    """
    Function splits a file given by file_name to a list of chunks which are either paragraphs or sentences.
    :param file_name: Name of the input file
    :param mode: Either 'p' for paragraphs or 's' for sentences
    :return: list of sentences or paragraphs
    """
    lns = [] # lines
    if mode not in ['s', 'p']:
        return lns

    file = open(file_name, encoding='utf-8-sig')

    for line in file:
        line = line.replace('\r', '')
        line = line.replace('\n', '')
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.replace('"', '')
        line = line.replace('“', '')
        line = line.replace('”', '')

        if mode == 's':
            lns.extend(split_line(line))
        else:
            lns.append(line)

    file.close()

    return lns

