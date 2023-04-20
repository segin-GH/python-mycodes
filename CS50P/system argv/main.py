import sys


def main():
    try:
        print("hello,", sys.argv[1])

    # trunk-ignore(ruff/E722)
    except:
        print("Error ::  Did you write your name ? ")


if __name__ == "__main__":
    main()
