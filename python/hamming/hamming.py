def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The lenght of two strands are different.')
    else:
        return len([1 for a, b in zip(strand_a, strand_b) if a != b])