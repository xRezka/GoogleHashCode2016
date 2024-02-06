from utils.parser import parse


def parser_test(filename: str):
    return parse(filename)


file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
print(parser_test(file_path))
