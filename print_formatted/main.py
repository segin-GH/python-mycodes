def print_formatted(text, color=None, style=None):
    """
    Prints the given text with the specified formatting using ANSI escape codes.

    Args:
        text (str): The text to print.
        color (str): The color to apply to the text. Can be one of 'black', 'red', 'green', 'yellow',
                     'blue', 'magenta', 'cyan', 'white', or None for the default color.
        style (str): The style to apply to the text. Can be one of 'bold', 'underline', 'italic', or None
                     for no style.
    """
    # ANSI escape code constants
    ANSI_RESET = "\033[0m"
    ANSI_COLORS = {
        'black': "\033[30m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m"
    }
    ANSI_STYLES = {
        'bold': "\033[1m",
        'underline': "\033[4m",
        'italic': "\033[3m"
    }

    # Build the ANSI escape code sequence
    ansi_sequence = ""
    if color in ANSI_COLORS:
        ansi_sequence += ANSI_COLORS[color]
    if style in ANSI_STYLES:
        ansi_sequence += ANSI_STYLES[style]

    # Apply the formatting and print the text
    formatted_text = f"{ansi_sequence}{text}{ANSI_RESET}"
    print(formatted_text)


if __name__ == "__main__":
    # get input from user what do you want to type and in what color
    data = input("Enter the data you want to print: ")
    # print in all the formats
    print_formatted(data)

    print_formatted(data, color='red')
    print_formatted(data, style='bold')
    print_formatted(data, color='green')
    print_formatted(data, style='underline')
    print_formatted(data, color='yellow')
    print_formatted(data, style='italic')
    print_formatted(data, color='blue')
    print_formatted(data, style='bold')
    print_formatted(data, color='magenta')
    print_formatted(data, style='underline')
    print_formatted(data, color='cyan')
    print_formatted(data, style='italic')
    print_formatted(data, color='white')
    print_formatted(data, style='bold')
    print_formatted(data, color='red', style='underline')
    print_formatted(data, color='green', style='italic')
    print_formatted(data, color='yellow', style='bold')
    print_formatted(data, color='blue', style='underline')
    print_formatted(data, color='magenta', style='italic')
    print_formatted(data, color='cyan', style='bold')
    print_formatted(data, color='white', style='underline')
    print_formatted(data, color='red', style='italic')
    print_formatted(data, color='green', style='bold')
    print_formatted(data, color='yellow', style='underline')
    print_formatted(data, color='blue', style='italic')
    print_formatted(data, color='magenta', style='bold')
    print_formatted(data, color='cyan', style='underline')
    print_formatted(data, color='white', style='italic')
    print_formatted(data, color='red', style='bold')
    print_formatted(data, color='green', style='underline')
    print_formatted(data, color='yellow', style='italic')
    print_formatted(data, color='blue', style='bold')
    print_formatted(data, color='magenta', style='underline')
    print_formatted(data, color='cyan', style='italic')
    print_formatted(data, color='white', style='bold')
    print_formatted(data, color='red', style='underline')
    print_formatted(data, color='green', style='italic')
    print_formatted(data, color='yellow', style='bold')
    print_formatted(data, color='blue', style='underline')
    print_formatted(data, color='magenta', style='italic')
    print_formatted(data, color='cyan', style='bold')
    print_formatted(data, color='white', style='underline')
    print_formatted(data, color='red', style='italic')
    print_formatted(data, color='green', style='bold')
    print_formatted(data, color='yellow', style='underline')
    print_formatted(data, color='blue', style='italic')
    print_formatted(data, color='magenta', style='bold')
    print_formatted(data, color='cyan', style='underline')
    print_formatted(data, color='white', style='italic')
    print_formatted(data, color='red', style='bold')
    print_formatted(data, color='green', style='underline')
    print_formatted(data, color='yellow', style='italic')
