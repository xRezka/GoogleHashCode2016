from utils.parser import parse
from solutions.naive import naive


def main():
    file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
    challenge = parse(file_path)
    naive(challenge)


if __name__ == '__main__':
    main()
