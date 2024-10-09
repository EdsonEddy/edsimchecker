import tokenize
import io
from utils import UnionFind
from utils import optimized_edit_distance
from utils import get_similarity_coefficient

def get_tokenized_code(code_string):
    """
    Tokenizes the given code string.

    Args:
        code_string (str): The source code as a string.

    Returns:
        list: A list of token types from the tokenized code.
    """
    code_file = io.StringIO(code_string)
    return [token.type for token in tokenize.generate_tokens(code_file.readline)]

def similarity_grouper(file_names, file_contents, threshold, window_percentage):
    """
    Groups files based on their similarity.

    Args:
        file_names (list): A list of file names.
        file_contents (list): A list of file contents corresponding to the file names.
        threshold (float): The similarity threshold for grouping.
        window_percentage (float): The window percentage for the edit distance calculation.

    Returns:
        list: A list of groups, where each group is a list of file names that are similar.
    """
    file_number = len(file_names)
    uf = UnionFind(file_number)

    tokenized_files = [get_tokenized_code(file) for file in file_contents]

    for i in range(file_number - 1):
        seq_a = tokenized_files[i]
        len_a = len(tokenized_files[i])
        for j in range(i + 1, file_number):
            if not uf.is_same_set(i, j):
                seq_b = tokenized_files[j]
                len_b = len(tokenized_files[j])
                edit_distance = optimized_edit_distance(seq_a, seq_b, window_percentage)
                similarity_percentage = get_similarity_coefficient(edit_distance, len_a, len_b)
                if similarity_percentage > threshold:
                    uf.union(i, j)

    groups = {}
    for i in range(file_number):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(file_names[i])

    return list(groups.values())