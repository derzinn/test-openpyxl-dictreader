import openpyxl_dictreader

reader = openpyxl_dictreader.DictReader("test.xlsx", "Sheet1")

"""
input:

foo | bar | baz
  1 |   2 |   3
    |   2 |   3
  1 |     |   3

output:

{'foo': 1, 'bar': 2, 'baz': 3}
{'foo': None, 'bar': 2, 'baz': None}
{'foo': 1, 'bar': None, 'baz': None}

expected output:

{'foo': 1, 'bar': 2, 'baz': 3}
{'foo': None, 'bar': 2, 'baz': 3}
{'foo': 1, 'bar': None, 'baz': 3}
"""

if __name__ == "__main__":
    for row in reader:
        print(row)