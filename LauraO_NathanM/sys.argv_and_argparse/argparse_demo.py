import sys
import argparse

def main():
    argparser = get_arg_parser()
    args = argparser.parse_args()
    if args.infile == None:
        argparser.print_usage()
        sys.exit()
    print(args)
    print(vars(args))
    print(args.__dict__)


def get_arg_parser():
    usage = '%(prog)s [options] infile <outfile>\n%(prog)s -h for help'
    parser = argparse.ArgumentParser(description='Program description',
                                     usage=usage)

    parser.add_argument('-a',
                        help="If included, value for a must be provided")
    parser.add_argument('-b', type=int,
                        help="If included, value must be an int")
    parser.add_argument('-c', action='store_const', const=1,
                        help='If included, value will be 1')
    parser.add_argument('-d', action='store_true',
                        help='If included, value will be True, else False')
    parser.add_argument('-e', action='store_false',
                        help='If included, value will be False, else True')
    parser.add_argument('-f', action='store', type=int, nargs=2,
                        help='If included, two integers must be provided')
    # Double dash means option will be interpreted as multi-character option
    # abc rather than -a -b -c          
    parser.add_argument('--abc',
                        help="If included, abc must be provided")
    # Provide short and long options for one argument
    parser.add_argument('-s', '--long',
                        help="If included, access -s and --long values using long")
    parser.add_argument('-g', dest='Good',
                        help="If included, Good is the property name in \
                              Namespace returned by parse_args")
    parser.add_argument('-i', metavar='Heavy',
                        help="If included, i is the property name in \
                              Namespace returned by parse_args.")

    parser.add_argument('-v', action='version', 
                        help='If specified, all other options are ignored')

    parser.add_argument('infile',
                        help='This is one required postional argument')
    parser.add_argument('outfile',
                        help='This is another postitional argument but is optional',
                        nargs='?')
    parser.version = '0.1'
    return parser
# print([a for a in dir(parser) if a[0] != '_'])

if __name__ == '__main__':
    main()

# Command line syntax:
# 
#     program option(s) arg(s)
# 
# where option(s) are optional and position does not matter
#       arg(s) are usually required and position does matter
# 
# e.g. dir /b C:\
#
# In Linux/Unix and Python, command line options are prefixed with a - or --
# by default.  The option prefix can be changed to / by passing 
# prefix_chars='/' to argparse.ArgumentParser
#
# Options are used to control the behaviour of a script
# Short options - Single character option prefixed with one dash (e.g. -a)
#                 Meant to be used in combination with other short options
#                 e.g. -abc is the same as -a -b -c
# Long options - Multi-character option prefixed with 2 dashes (e.g. --abc)
#                Ensures --abc will not be confused with -a -b -c
#
# argparse.ArgumentParser arguments
#
#   prog = name of program to dusplay in usage (Default: .py file name)
#   usage = usage for the program. %(prog)s can be used to inlude prog
#           in usage.  Default: program [all options] [all args]
#   description = description of what the program does.  Displayed before
#                 help text (i.e. -h)
#   epilog = Text displayed after help text.
#   from_file_prefix_chars = character to signify arguments will come
#                            file specifies after prefix (e.g. @args.txt)
# 
# ArgumentParser.add_argument arguments:
#
#   name(s) = name of option(s) (e.g. -a, --a_long_name).  Names without
#             dashes represent positional arguments
#   help = text that will display when -h option is provided
#   action = action to perform if option is provided.  
#       Can be:
#       store = stores the input value to the Namespace object. 
#               (This is the default action.)
#       store_const = stores a constant value when the option is provided.
#       store_true = if option specified, store True, else False
#       store_false = if option specified, store False, else True
#       version = shows the version of the program (ArgumentParser.version) 
#                 and exits.  Any other option will be ignored
#       <Custom> = class that inherits from argparse.Action.  Must have 
#                  call to super().__init__ in __init__ and __call__
#                  defined.
#   choices = [list of possible choices] for given option/argument
#   required = True if option is required.  Default: False
#   nargs = number of arguments that must follow option. Default is 1  
#       Can be:
#       number = number of values that must be specified with the option
#       ? = a single value, which can be optional
#       * = multiple values, which will be gathered into a list
#       + = 1 or more values
#       argparse.REMAINDER = all values remaining on the command line
#   metavar = more verbose option name shown in help.  Default is 
#             uppercase version of the option name(s)
#   dest = name of the Namespace property which will be associated
#          with the option value
#   default = default value if not specified
#   type = specify the type for the option/argument
#
#  ArgumentParser.add_mutually_exclusive_group arguments:
#
#   required = True if required.  Default: False
#   
#  add_argument on group returned by call to add_mutually_exclusive_group
#  will add arguments that are mutually exclusive (e.g. silent and verbose)
#