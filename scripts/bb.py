import argparse


def display(x):
    s = bin(x)[2:]
    return '0' * (32 - len(s)) + s


def dump(x):
    return x.to_bytes(4, byteorder='little', signed=False)


def main(args):
    number = int(args.number, 16)
    if args.option == 'd':
        args.file.write(dump(number))
    else:
        x = display(number)
        print(x[args.first_bit:args.last_bit])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manipulates 32-bit numbers')
    parser.add_argument('number', type=str, help='number to manipulate')
    subparsers = parser.add_subparsers(help='option', dest='option')

    parser_p = subparsers.add_parser('p', help='(p)rint human readable')
    parser_p.add_argument('first_bit', type=int, default=0, nargs='?', help='begin bit position')
    parser_p.add_argument('last_bit', type=int, default=32, nargs='?', help='end bit position')

    parser_d = subparsers.add_parser('d', help='(d)ump/append to binary file')
    parser_d.add_argument('file', type=argparse.FileType('ab'))

    main(parser.parse_args())
