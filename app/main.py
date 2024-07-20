import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    error = False

    with open(filename) as file:
        file_contents = file.read()

    for c in file_contents:
        match c:
            case "(":
                print("LEFT_PAREN ( null")
            case ")":
                print("RIGHT_PAREN ) null")
            case "{":
                print("LEFT_BRACE { null")
            case "}":
                print("RIGHT_BRACE } null")
            case "*":
                print("STAR * null")
            case ".":
                print("DOT . null")
            case ",":
                print("COMMA , null")
            case "+":
                print("PLUS + null")
            case "-":
                print("MINUS - null")
            case ";":
                print("SEMICOLON ; null")
            case "==":
                print("EQUAL_EQUAL == null")
            case "=":
                print("EQUAL = null")
            case _:
                print("[line 1] Error: Unexpected character: " + c, file=sys.stderr)
                error = True
        
    print("EOF  null") # Placeholder, remove this line when implementing the scanner
    if error:
        exit(65)

if __name__ == "__main__":
    main()
