import argparse
from pathlib import Path
from file_handler import process_files
from similarity_checker import similarity_grouper

def get_file(file_path):
    if not Path(file_path).is_file():
        raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist.")
    return file_path

def get_threshold(value):
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid threshold value: {value}")
    if fvalue < 0.0 or fvalue > 1.0:
        raise argparse.ArgumentTypeError(f"Threshold must be between 0.0 and 1.0")
    return fvalue

def get_level(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid level value: {value}")
    if ivalue < 0 or ivalue > 4:
        raise argparse.ArgumentTypeError(f"Level must be between 0 and 4")
    return ivalue

def get_window_percentage(value):
    fvalue = float(value)
    if fvalue < 0.0 or fvalue > 1.0:
        raise argparse.ArgumentTypeError(f"Window percentage must be between 0.0 and 1.0")
    return fvalue

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='EdSimChecker: Detect similarity between source codes.')
    
    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add the 'path' argument to the group
    group.add_argument('--path', '-p', type=str, help='Path to the directory containing the source code files')
    
    # Add the 'files' argument to the group
    group.add_argument('--files', '-f', type=get_file, nargs=2, help='The input files')
    
    # Add the 'recursive' argument
    parser.add_argument('--recursive', '-r', action='store_true', help='Recursively search through directories')

    # Add the 'threshold' argument with range validation (0.0 - 1.0)
    parser.add_argument('--threshold', '-t', type=get_threshold, default=0.75, help='The similarity threshold (default: 0.75, range: 0.0 - 1.0)')

    # Add the 'level' argument with range validation (0 - 4)
    parser.add_argument('--level', '-l', type=get_level, default=0, help='The obfuscation level (default: 0, range: 0 - 4)')
    
    # Add the 'window-percentage' argument with range validation (0.0 - 1.0)
    parser.add_argument('--window-percentage', '-w', type=get_window_percentage, default=1.0, help='The window percentage (default: 1.0, range: 0.0 - 1.0)')

    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if len(file_names) > 1:
        # Group the files based on similarity
        groups = similarity_grouper(file_names, file_contents, args.threshold, args.window_percentage)

        # Display the grouped files
        for group_index, file_group in enumerate(groups):
            print(f"Group {group_index + 1}:")
            for file in file_group:
                print(file)
    else:
        print("No files to compare.")

if __name__ == "__main__":
    main()