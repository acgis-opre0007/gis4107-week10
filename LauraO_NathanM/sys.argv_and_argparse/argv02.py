import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: argv02.py some_message')
        sys.exit()

    msg = sys.argv[1]
    print(f'Message is: {msg}')

if __name__ == '__main__':
    main()


