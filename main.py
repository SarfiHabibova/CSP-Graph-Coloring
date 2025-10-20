import sys
from parser_utils import parse_input
from csp_solver import solve_csp
from utils import print_header

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    print_header()
    filename = sys.argv[1]
    solve_csp(filename, parse_input)

if __name__ == "__main__":
    main()
