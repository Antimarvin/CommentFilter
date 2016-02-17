__author__ = 'Richard L. Sweat Jr.'
import codehandler as ch

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    my_code_handler = ch.CodeHandler()
    line = 1
    for row in data:
        if not row.isspace():
            my_code_handler.process_line(line=row, index=line)
        line += 1

    if my_code_handler.in_comment:
        raise ValueError('Unclosed Comment in file')



if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()