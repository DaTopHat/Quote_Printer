#!/usr/bin/python


APP_NAME = "Quote Printer"


def get_quote():
    import random
    from quotes import quotes
    quote = random.choice(quotes)
    return quote


def print_quote_console():
    console.print(get_quote(), style="bold blue")


def print_notify():
    import subprocess
    quote = get_quote()
    subprocess.run(['notify-send', '-a', APP_NAME, APP_NAME, quote])


def run_server():
    import time
    while True:
        print_notify()
        time.sleep(600)


def main():
    import sys
    global console
    args = sys.argv
    if len(args) != 0:
        del args[0]
    if not sys.platform.startswith('linux'):
        console.log("Platform not linux", style="bold red")
        sys.exit()
    if "-N" in args or "--notification" in args:
        print_notify()
    if "-C" in args or "--console" in args:
        print_quote_console()
    if "-S" in args or "--server" in args:
        run_server()


if __name__ == "__main__":
    from rich.console import Console
    console = Console()
    main()
