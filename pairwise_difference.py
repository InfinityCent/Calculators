from typing import List, Any, Dict, Union


## Author: Alex Daiejavad (1004020828)
## Purpose: this calculator detemines the mean pairwise difference
## per nucleotide when given a list of genomic sequences. It was
## written for a 4th year university course assignment.

def compare_seqs(seq1: str, seq2: str) -> int:
    """Return the number of sites that differ between <seq1> and <seq2>.

    Precondition: len(seq1) == len(seq2)

    >>> seq1 = 'ATTCGAATCCTATATCGGGGTACCC'
    >>> seq2 = 'ATTGGAATCCTATATCGGGGTACCC'
    >>> seq7 = 'AATCGATTCCTATATCGTGGCACCC'
    >>> compare_seqs(seq1, seq2)
    1
    >>> compare_seqs(seq1, seq7)
    4
    >>> compare_seqs(seq2, seq7)
    5

    """
    diffs = 0
    for i in range(len(seq1)):
        if not seq1[i] == seq2[i]:
            diffs += 1

    return diffs


def create_matrix(length: int) -> List[List[int]]:
    """Given a <length> n, this will return a list containing
    n nested lists, each with n 0s.

    >>> create_matrix(4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    """
    matrix = []
    for i in range(length):
        matrix.append([])

    for lst in matrix:
        for i in range(length):
            lst.append(0)

    return matrix


def calculate_matrix(seq_list: List[str]) -> List[List[int]]:
    """Returns a pairwise matrix that contains the number of differences
    between each pair of sequences in <seq_list>.

    """
    matrix = create_matrix(len(seq_list))

    for i in range(len(seq_list)):
        for j in range(len(seq_list)):
            matrix[i][j] = compare_seqs(seq_list[i], seq_list[j])

    return matrix


def str_matrix(matrix: List[List[Any]]) -> None:
    """Print a list of list in a readable manner.

    """

    for sublist in matrix:
        print(*sublist)


def calculate_pi(seq_list: List[str]) -> Dict[str, Union[int, float]]:
    """Calculate mean pairwise difference per nucleotide given a <seq_list>.

    """
    matrix = calculate_matrix(seq_list)
    num_comparisons = 0
    total_diffs = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i >= j:
                pass
            else:
                num_comparisons += 1
                total_diffs += matrix[i][j]

    upper_pi_value = total_diffs / num_comparisons
    lower_pi_value = upper_pi_value / len(seq_list[0])

    return {'Number of pairwise comparisons': num_comparisons,
            'Sum of all pairwise differences': total_diffs,
            'Sequence length L': len(seq_list[0]),
            'Mean pairwise difference': upper_pi_value,
            'Mean pairwise difference per nucleotide': lower_pi_value}


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    seq_lst1 = ['ATTCGAATCCTATATCGGGGTACCC', 'ATTGGAATCCTATATCGGGGTACCC',
               'AATCGATTCCTTTATCGGGGTACCC', 'ATTGGAATCCTTTATCGTGGCACCC',
               'AATCGATTCCTTTATCGGGGTACCC', 'ATTCGATTCCTTTATCGGGGTACCA',
               'AATCGATTCCTATATCGTGGCACCC', 'AATCGATTCCTTTATCGGGGTACCC',
               'ATTCGATTCCTTTATCGGGGTACCA', 'ATTGGAATCCTATATCGGGGTACCC']

    calculate_pi(seq_lst1)


