import sys
from analyser import total_sales_by_console
from importer import import_from_json


def main():
    path_file = sys.argv[1]
    file_data = import_from_json(path_file)
    print(total_sales_by_console(file_data))


if __name__ == "__main__":
    main()