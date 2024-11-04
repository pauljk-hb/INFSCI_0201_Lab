# Python Style Checker

This Python Style Checker is a tool designed to analyze Python source files for various style issues, including missing docstrings, type annotations, and naming convention violations. It generates a report summarizing the findings.

## Features

- Counts the total number of lines in the file.
- Lists all the imports used in the file.
- Identifies all classes and functions defined in the file.
- Checks for missing docstrings in classes and functions.
- Checks for missing type annotations in function arguments and return types.
- Checks for naming convention violations in class and function names.

## Usage

To use the Python Style Checker, run the following command:

```sh
python style_checker.py <file_to_check.py>
```

Replace <file_to_check.py> with the path to the Python file you want to check.

## Example

```sh
python style_checker.py example.py
```

This will generate a report file named `style_report_example.py.txt` in the same directory.

## Output

The generated report includes the following sections:

- **File Structure**: Total number of lines in the file.
- **Imports**: List of all imports used in the file.
- **Classes**: List of all classes defined in the file.
- **Functions**: List of all functions defined in the file.
- **DocStrings**: List of classes and functions missing docstrings.
- **Type Annotations**: List of functions missing type annotations.
- **Naming Violations**: List of classes and functions with naming convention violations.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.
