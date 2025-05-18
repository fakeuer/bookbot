def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_symbols(text: str) -> dict:
    """
    Counts the number of symbols in a given text.
    
    Args:
        text (str): The text to count symbols in.
        
    Returns:
        int: The number of symbols in the text.
    """
    map = dict()
    for char in text:
        char = char.lower()
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    
    return map

def get_dict_report(report: dict) -> list[dict]:
    """
    Converts a dictionary to a list of dictionaries for better readability.
    
    Args:
        report (dict): The dictionary to convert.
        
    Returns:
        list[dict]: A list of dictionaries with the key and value pairs.
    """
    data = [{k: v} for k, v in report.items()]
    data.sort(key=lambda x: list(x.values())[0], reverse=True)
    return data



    