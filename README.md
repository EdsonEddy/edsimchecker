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
3. Install the package:
    ```sh
    python setup.py install
    ```

## Arguments

- `--path`, `-p`: Path to the directory containing the source code files.
- `--files`, `-f`: Specific input files to compare.
- `--recursive`, `-r`: Recursively search through directories.
- `--threshold`, `-t`: Similarity threshold (default: 0.7, range: 0.0 - 1.0).
- `--level`, `-l`: Obfuscation level (default: 0, range: 0 - 4).
- `--window-percentage`, `-w`: Window percentage (default: 1.0, range: 0.0 - 1.0).

## Usage

EdSimChecker can be used from the command line. Here are some usage examples:

### Compare Specific Files
```sh
edsimchecker --files file1.py file2.py
```

### Analyze an Entire Directory
```sh
edsimchecker --path /path/to/directory --recursive
```

### Adjust the Similarity Threshold
```sh
edsimchecker --path /path/to/directory --threshold 0.8
```

### Adjust the Obfuscation Level
```sh
edsimchecker --path /path/to/directory --level 2
```

### Adjust the Window Percentage
```sh
edsimchecker --path /path/to/directory --window-percentage 0.5
```

## Contributing

Contributions are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## Additional Documentation
For more information on the techniques used, you can refer to the following resources:

- [Edit Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Tokenization](https://en.wikipedia.org/wiki/Tokenization)
- [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Links

- [Repository](https://github.com/EdsonEddy/edsimchecker)
- [Documentation](https://github.com/EdsonEddy/edsimchecker/wiki)
- [Report a Bug](https://github.com/EdsonEddy/edsimchecker/issues)