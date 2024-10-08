import tokenize
import io
from utils import UnionFind
from utils import edit_distance_optimized

def get_tokenized_code(code_string):
    code_file = io.StringIO(code_string)
    return [token.type for token in tokenize.generate_tokens(code_file.readline)]

def similarity_grouper(file_names, file_contents, threshold, window_percentage):
    file_number = len(file_names)
    uf = UnionFind(file_number)

    tokenized_files = [get_tokenized_code(file) for file in file_contents]

    for i in range(file_number - 1):
        for j in range(i + 1, file_number):
            if not uf.is_same_set(i, j):
                if edit_distance_optimized(tokenized_files[i], tokenized_files[j], window_percentage) < threshold:
                    uf.union(i, j)

    groups = {}
    for i in range(file_number):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(file_names[i])

    return list(groups.values())