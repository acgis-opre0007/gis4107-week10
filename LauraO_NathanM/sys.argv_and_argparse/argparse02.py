import argparse

def main():
    argparser = get_arg_parser()
    args = argparser.parse_args()
    msg = args.some_message
    print(f'Message is: {msg}')

def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('some_message',
                        help='Enter some message to echo to screen')
    return parser

if __name__ == '__main__':
    main()
