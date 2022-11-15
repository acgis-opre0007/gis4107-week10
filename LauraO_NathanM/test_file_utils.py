
import os
import file_utils as fu

def test_get_file_content():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    
    file_name = os.path.join(script_folder, "data", "demo.txt")
    expected = 'hi'
    actual = fu.get_file_content(file_name)
    assert expected == actual

    file_name = os.path.join(script_folder, "data", "demo_x.txt")
    expected = f'{file_name} does not exist.'
    actual = fu.get_file_content(file_name)
    assert expected == actual

def test_write_to_file():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name=os.path.join(script_folder, "data", "TestFile.txt")
    content = 'something\n'
    expected = content
    fu.write_to_file(file_name, content)
    actual = fu.get_file_content(file_name)
    assert expected == actual








