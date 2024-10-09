# Obfuscation Levels

EdSimChecker provides multiple levels of code obfuscation to help analyze and detect similarities in source code. Each level applies different transformations to the code.

#### Level 0: No Transformations
At this level, no transformations are applied to the source code. The code remains as it was provided.

#### Level 1: Docstring Cleaning
At this level, comments and docstrings are removed from the source code. This helps reduce the code size and remove unnecessary information that could be used to understand the purpose of the code.

- **Method Used**: `DocstringCleaner`
  - **Description**: Removes docstrings from functions and classes in the abstract syntax tree (AST).

#### Level 2: Unused Variable Cleaning
At this level, in addition to docstring cleaning, unused variables are removed from the code. This helps reduce clutter and improve code efficiency.

- **Methods Used**:
  - `DocstringCleaner`
  - `UnusedVariablesCleaner`
    - **Description**: Removes variable assignments that are not used in the code.

#### Level 3: Unused Function Cleaning
At this level, in addition to the transformations of the previous levels, unused functions are removed from the code. This helps reduce the code size and eliminate unnecessary functions.

- **Methods Used**:
  - `DocstringCleaner`
  - `UnusedVariablesCleaner`
  - `UnusedFunctionsCleaner`
    - **Description**: Removes function definitions that are not called in the code.

#### Level 4: Function Inlining
At this level, in addition to the transformations of the previous levels, function inlining is performed. This means that function calls are replaced with the function body, which can improve code efficiency by eliminating the overhead of function calls.

- **Methods Used**:
  - `DocstringCleaner`
  - `UnusedVariablesCleaner`
  - `UnusedFunctionsCleaner`
  - `FunctionInliner`
    - **Description**: Replaces function calls with the corresponding function body.

### Example Usage
```python
code_string = """
def foo():
    '''This is a docstring.'''
    x = 10
    y = 20
    return x + y

def bar():
    return foo()

print(bar())
"""

# Level 0: No transformations
print(code_cleaner(code_string, level=0))

# Level 1: Docstring cleaning
print(code_cleaner(code_string, level=1))

# Level 2: Unused variable cleaning
print(code_cleaner(code_string, level=2))

# Level 3: Unused function cleaning
print(code_cleaner(code_string, level=3))

# Level 4: Function inlining
print(code_cleaner(code_string, level=4))
```

## Purpose
*The purpose of applying the code cleaner at various levels of obfuscation is to simplify the source code, making it easier to compare with other code. By progressively removing docstrings, unused variables, and unused functions, and by inlining function calls, the code cleaner reduces the code size and eliminates unnecessary elements. This process helps in analyzing and detecting similarities in source code more effectively.*
