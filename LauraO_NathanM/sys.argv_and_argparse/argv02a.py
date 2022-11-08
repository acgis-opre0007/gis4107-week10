import sys

def main():
    if len(sys.argv) == 1:
        print('Usage: argv02.py [-h] some_message')
        print('error:  the following arguments are required: some_message')
        sys.exit()

    if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '-help'):
        print('Usage: argv02.py [-h] some_message')
        print('')
        print('positional arguments:')
        print('some_message  Enter some message to echo to screen')
        print('')
        print('optional arguments:')
        print('-h, --help    show this help message and exit')
        sys.exit()

    msg = sys.argv[1]
    print(f'Message is: {msg}')

if __name__ == '__main__':
    main()


