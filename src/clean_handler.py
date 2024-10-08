import ast

class FunctionCollector(ast.NodeVisitor):
    """
    A class to collect information about function calls, variable assignments, 
    and variable usages in an abstract syntax tree (AST).
    Attributes:
        called_funcs (set): A set of names of called functions.
        assigned_vars (set): A set of names of assigned variables.
        load_vars (set): A set of names of variables used in load context.
        store_vars (set): A set of names of variables used in store context.
    Methods:
        visit_Call(node): Collects function call names.
        visit_Assign(node): Collects assigned variable names.
        visit_Name(node): Collects variable names used in load and store contexts.
    """
    def __init__(self):
        self.called_funcs = set()
        self.assigned_vars = set()
        self.load_vars = set()
        self.store_vars = set()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.called_funcs.add(node.func.id)
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.assigned_vars.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.load_vars.add(node.id)
        if isinstance(node.ctx, ast.Store):
            self.store_vars.add(node.id)

class UnusedFunctionsCleaner(ast.NodeTransformer):
    """
    A class to remove unused functions from an abstract syntax tree (AST).
    Attributes:
        used_funcs (set): A set of names of used functions.
    Methods:
        visit_FunctionDef(node): Removes functions that are not in the used_funcs set.
    """
    def __init__(self, used_funcs):
        self.used_funcs = used_funcs

    def visit_FunctionDef(self, node):
        if node.name not in self.used_funcs:
            return None
        return node

class DocstringCleaner(ast.NodeTransformer):
    """
    A class to remove docstrings from an abstract syntax tree (AST).
    Methods:
        visit_Expr(node): Removes docsstrings.
    """
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return None
        return node

class UnusedVariablesCleaner(ast.NodeTransformer):
    """
    A class to remove unused variables from an abstract syntax tree (AST).
    Attributes:
        unused_vars (set): A set of names of unused variables.
    Methods:
        visit_Assign(node): Removes assignments that contain unused variables.
    """
    def __init__(self, unused_vars):
        self.unused_vars = unused_vars
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in self.unused_vars:
                return None
        return node

class FunctionInliner(ast.NodeTransformer):
    """
    A class to inline function calls in an abstract syntax tree (AST).
    Attributes:
        func_defs (dict): A dictionary mapping function names to their AST nodes.
    Methods:
        visit_FunctionDef(node): Collects function definitions.
        visit_Call(node): Inlines function calls.
    """
    def __init__(self):
        self.func_defs = {}

    def visit_FunctionDef(self, node):
        self.func_defs[node.name] = node
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.func_defs:
            func_def = self.func_defs[node.func.id]
            if len(func_def.args.args) == len(node.args):
                inline_body = []
                for arg, param in zip(node.args, func_def.args.args):
                    assign = ast.Assign(targets=[ast.Name(id=param.arg, ctx=ast.Store())], value=arg)
                    inline_body.append(assign)
                inline_body.extend(func_def.body)
                return ast.Module(body=inline_body, type_ignores=[])
        return self.generic_visit(node)

def code_cleaner(code_string, level):
    """
    Removes unused functions, variables, and docstrings from the given Python code string and inlines functions.
    Args:
        code_string (str): The Python code as a string.
        level (int): The level of obfuscation to apply.
    Returns:
        str: The cleaned Python code with unused features removed.
    """
    tree = ast.parse(code_string)

    # Collect function calls, variable assignments, and usages
    collector = FunctionCollector()
    collector.visit(tree)

    # Apply transformations based on the level
    if level >= 1:
        # Clean docstrings
        docstring_cleaner = DocstringCleaner()
        tree = docstring_cleaner.visit(tree)

    if level >= 2:
        # Clean unused variables
        unused_vars = collector.store_vars - collector.load_vars - collector.called_funcs
        variable_cleaner = UnusedVariablesCleaner(unused_vars)
        tree = variable_cleaner.visit(tree)

    if level >= 3:
        # Clean unused functions
        function_cleaner = UnusedFunctionsCleaner(collector.called_funcs)
        tree = function_cleaner.visit(tree)

    if level >= 4:
        # Inline functions
        inliner = FunctionInliner()
        tree = inliner.visit(tree)

    # Reconstruct the tree
    tree = ast.fix_missing_locations(tree)
    
    return ast.unparse(tree)