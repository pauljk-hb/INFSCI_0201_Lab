import ast
import os

class PythonStyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.analyzer = CodeAnalyzer(file_path)
        self.report_generator = ReportGenerator(self.file_name)

    def run(self):
        results = self.analyzer.analyze()
        self.report_generator.generate_report(results)

class CodeAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.results = {
            'line_count': 0,
            'imports': [],
            'classes': [],
            'functions': [],
            'missing_docstrings': [],
            'missing_type_annotations': [],
            'naming_violations': []
        }
        self.tree = self._parse_file()

    def _parse_file(self):
        with open(self.file_path, 'r') as file:
            self.results['line_count'] = sum(1 for _ in file)
            file.seek(0)
            return ast.parse(file.read())

    def analyze(self):
        self.results['imports'] = self.get_imports()
        self.results['classes'], self.results['functions'] = self.get_classes_and_functions()
        self.results['missing_docstrings'] = self.extract_docstrings()
        self.results['missing_type_annotations'] = self.check_type_annotations()
        self.results['naming_violations'] = self.check_naming_conventions()
        return self.results

    def get_imports(self):
        return [node.names[0].name for node in ast.walk(self.tree) if isinstance(node, ast.Import)]

    def get_classes_and_functions(self):
        classes = []
        functions = []

        for node in self.tree.body:
            if isinstance(node, ast.ClassDef):
                classes.append(node)
            elif isinstance(node, ast.FunctionDef):
                functions.append(node)

        return classes, functions

    def extract_docstrings(self):
        missing_docstrings = []
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and ast.get_docstring(node) is None:
                missing_docstrings.append(f"{node.name}: DocString not found")
        return missing_docstrings

    def check_type_annotations(self):
        missing_annotations = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not any(arg.annotation for arg in node.args.args) or node.returns is None:
                    missing_annotations.append(node.name)
        return missing_annotations

    def check_naming_conventions(self):
        naming_violations = {'classes': [], 'functions': []}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                if not node.name[0].isupper():
                    naming_violations['classes'].append(node.name)
            elif isinstance(node, ast.FunctionDef):
                if not node.name.islower() or '_' not in node.name:
                    naming_violations['functions'].append(node.name)
        return naming_violations

class ReportGenerator:
    def __init__(self, file_name):
        self.file_name = file_name

    def generate_report(self, results):
        report_name = f"style_report_{self.file_name}.txt"
        with open(report_name, 'w') as report_file:
            report_file.write(f"File Structure\nTotal Lines: {results['line_count']}\n\n")
            report_file.write(f"Imports: {', '.join(results['imports'])}\n\n")
            report_file.write(f"Classes: {', '.join(cls.name for cls in results['classes'])}\n\n")
            report_file.write(f"Functions: {', '.join(func.name for func in results['functions'])}\n\n")
            report_file.write("DocStrings:\n" + "\n".join(results['missing_docstrings']) + "\n\n")
            report_file.write("Type Annotations:\n" + "\n".join(results['missing_type_annotations']) + "\n\n")
            report_file.write("Naming Violations:\n" + "\n".join(f"{k}: {', '.join(v)}" for k, v in results['naming_violations'].items()))
        print(f"Report generated: {report_name}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python style_checker.py <file_to_check.py>")
    else:
        checker = PythonStyleChecker(sys.argv[1])
        checker.run()
