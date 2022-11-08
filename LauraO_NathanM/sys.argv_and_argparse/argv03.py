import sys

def main():
    print(sys.argv)

    for i, item in enumerate(sys.argv):
        print(f'{i}: {item} ({sys.argv[i]})')

    print(sys.argv[len(sys.argv)])

if __name__ == '__main__':
    main()


