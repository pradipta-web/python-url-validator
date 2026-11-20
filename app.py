from urllib.parse import urlparse
from colorama import init, Fore

init(autoreset=True)


def validate_url(url):
    try:
        parsed = urlparse(url)

        if parsed.scheme not in ["http", "https"]:
            return False, "Invalid protocol. Use HTTP or HTTPS."

        if not parsed.hostname:
            return False, "Missing hostname or domain."

        if " " in url:
            return False, "URL cannot contain spaces."

        return True, "URL format is valid."

    except ValueError:
        return False, "Invalid URL format."


def main():
    print("=" * 45)
    print("              URL VALIDATOR")
    print("=" * 45)

    while True:
        print("\nEnter URL (or type 'exit' to quit):")
        url = input("> ").strip()

        if url.lower() == "exit":
            print("\nThank you for using URL Validator!")
            break

        if not url:
            print(Fore.RED + "URL cannot be empty!")
            continue

        is_valid, message = validate_url(url)

        print("\n" + "-" * 45)

        if is_valid:
            print(Fore.GREEN + "Status: VALID")
        else:
            print(Fore.RED + "Status: INVALID")

        print(f"Message: {message}")
        print("-" * 45)


if __name__ == "__main__":
    main()