def calc_gc(seq: str) -> float:
    """
    Counts the GC content of a given sequence string.

    Args:
        seq (str): a nucleic acid sequence string.

    Returns:
        float: GC count, or "Sequence lenght is zero" string if string lengh is 0.
    """
    if not seq:
        return "Sequence lenght is 0"
    gc_count = sum(1 for c in seq.upper() if c in "GC")
    return (gc_count / len(seq)) * 100


def calc_mean_quality(qual_str: str) -> float:
    """
    Checks if the mean quality of a read is acceptable

    Args:
        qual_str (str): a string of phed33 quality scores per each nucleotide.

    Returns:
        float: mean quality for a sequence.
    """
    if not qual_str:
        return 0.0
    return sum(ord(c) - 33 for c in qual_str) / len(qual_str)


def in_bounds(value: int, bounds: tuple) -> bool:
    """
    Checks if the given sequence string is of allowed length.

    Args:
    - value (int): a nucleic acid string lenght value.
    - bounds (tuple): a tuple with lower and upper length boundaries.

    Returns:
        bool
    """
    if isinstance(bounds, (int, float)):
        return value <= bounds
    elif isinstance(bounds, (tuple, list)) and len(bounds) == 2:
        low, high = bounds
        return low <= value <= high

