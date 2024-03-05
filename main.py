from utils.parser import parse
from solutions.naive import naive


def main():
    file_path = 'D:\Projects\GoogleHashCode2016\challenges\\b_busy_day.in'
    challenge = parse(file_path)
    naive(challenge)


if __name__ == '__main__':
    main()
