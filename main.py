from stats import count_symbols, get_dict_report, count_words
import sys

def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def print_report(report: list[dict], book_path: str, num_words: int):
    """
    Prints the report in a readable format.
    
    Args:
        report (list[dict]): The report to print.
    """
    print(f'============ BOOKBOT ============ \n\
Analyzing book found at {book_path}...\n\
----------- Word Count ----------\n\
Found {num_words} total words\n\
--------- Character Count -------\n')
    for entry in report:
        for symbol, count in entry.items():
            print(f"{symbol}: {count}")
    print("============= END ===============")


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Path to the book file
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)

    symbols_map = count_symbols(book_text)

    report = get_dict_report(symbols_map)

    num_words = count_words(book_text)

    print_report(report, book_path, num_words)


if __name__ == "__main__":
    main()
