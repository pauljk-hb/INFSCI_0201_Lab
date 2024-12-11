import ast
import os

def get_file_path():
    return input("Enter the path to the Python source file: ")

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        file.seek(0)
        tree = ast.parse(file.read())
    return line_count, tree

def get_imports(tree):
    return [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]

def get_classes_and_functions(tree):
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return classes, functions

def extract_docstrings(tree):
    docstrings = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            docstrings[node.name] = docstring if docstring else f"{node.name}: DocString not found"
    return docstrings

def check_type_annotations(tree):
    missing_annotations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not node.returns or not all(arg.annotation for arg in node.args.args):
                missing_annotations.append(node.name)
    return missing_annotations

def check_naming_conventions(classes, functions):
    naming_violations = {
        'classes': [cls for cls in classes if not cls[0].isupper()],
        'functions': [func for func in functions if not func.islower() and '_' not in func and len(func.split('_')) > 1]
    }
    return naming_violations

def generate_report(file_path, line_count, imports, classes, functions, docstrings, missing_annotations, naming_violations):
    report_path = os.path.join(os.path.dirname(file_path), f"style_report_{os.path.basename(file_path)}.txt")
    with open(report_path, 'w') as report:
        report.write(f"File structure\n")
        report.write(f"Total number of lines of code in the file: {line_count}\n")
        report.write(f"Imports: {', '.join(imports)}\n")
        report.write(f"Classes: {', '.join(classes)}\n")
        report.write(f"Functions: {', '.join(functions)}\n\n")
        
        report.write("Doc Strings\n")
        for name, docstring in docstrings.items():
            report.write(f"{name}: {docstring}\n\n")
        
        report.write("Type Annotation Check\n")
        if missing_annotations:
            report.write(f"Functions and methods without type annotations: {', '.join(missing_annotations)}\n")
        else:
            report.write("All functions and methods use type annotations.\n")
        
        report.write("Naming Convention Check\n")
        if naming_violations['classes']:
            report.write(f"Classes not adhering to naming convention: {', '.join(naming_violations['classes'])}\n")
        else:
            report.write("All classes adhere to the naming convention.\n")
        
        if naming_violations['functions']:
            report.write(f"Functions not adhering to naming convention: {', '.join(naming_violations['functions'])}\n")
        else:
            report.write("All functions adhere to the naming convention.\n")

def main():
    file_path = get_file_path()
    line_count, tree = parse_file(file_path)
    imports = get_imports(tree)
    classes, functions = get_classes_and_functions(tree)
    docstrings = extract_docstrings(tree)
    missing_annotations = check_type_annotations(tree)
    naming_violations = check_naming_conventions(classes, functions)
    generate_report(file_path, line_count, imports, classes, functions, docstrings, missing_annotations, naming_violations)

if __name__ == "__main__":
    main()