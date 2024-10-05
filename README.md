# EdSimChecker

EdSimChecker is a tool designed to detect similarity between source codes, even when they have been obfuscated using various techniques. It is ideal for programming teachers and students who want to verify the originality of the code.

## Key Features

- **Similarity Detection:** Detects similarity between source codes, even if they contain obfuscation techniques.
- **Advanced Analysis:** Utilizes abstract syntax trees, tokenization, and edit distance to perform the analysis.
- **No Additional Dependencies:** Implemented in pure Python, with no need to install additional libraries.

## Technologies Used

- **Python:** Main programming language.
- **Abstract Syntax Trees (AST):** To analyze the structure of the code.
- **Tokenization:** To break down the code into basic elements.
- **Edit Distance:** To measure the similarity between different code fragments.

## Installation

No additional dependencies are required. You only need to have Python installed on your system.

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/edsimchecker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd edsimchecker
    ```
3. Run the main script:
    ```sh
    python main.py
    ```

## Usage

Here is a basic example of how to use EdSimChecker:

```python
from edsimchecker import EdSimChecker

checker = EdSimChecker()
similarity_score = checker.compare('code1.py', 'code2.py')
print(f'Similarity Score: {similarity_score}')
```

## Contribution
Users can contribute by testing the tool and reporting bugs or cases where the tool does not work correctly. To report an issue, open an issue on the GitHub repository.

## Additional Documentation
For more information on the techniques used, you can refer to the following resources:

- [Edit Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Tokenization](https://en.wikipedia.org/wiki/Tokenization)
- [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

## License
This project is licensed under the MIT License. See the LICENSE file for more details.