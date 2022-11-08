def get_file_content(file_name):
    try:
        with open(file_name) as infile:
            return infile.read()
    except FileNotFoundError:
        error = f'{file_name} does not exist.'
        return error

def write_to_file(file_name, content):
    """_summary_

    Args:
        file_name (_type_): _description_
        content (_type_): _description_
    """
    with open(file_name, 'w') as outfile:
        content = outfile.write('something\n')
    