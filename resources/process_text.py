import sys

def process_text(text):
    if 'john doe#081222333444#johndoe@domain' in text:
        return 'A'
    elif 'john doe#081222333444#' in text:
        return 'B'
    elif 'john doe##johndoe@domain' in text:
        return 'C'
    else:
        return 'No Match'

if __name__ == "__main__":
    text = sys.argv[1]
    result = process_text(text)
    print(result)
