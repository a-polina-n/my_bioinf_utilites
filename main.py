
import modules.nucleic_tools as nt
import modules.fastq_tools as ft


def run_dna_rna_tools(*args: str):
    """
    Performs some procedures for nucleic acids.
    
    Args:
        args(str): a series of strings with DNA or RNA sequences, separated by a coma.
    Last argument must proceed a procedure:
        is_nucleic_acid: checks if given strings are nucleic acids at all; returns bool.
        reverse: for a DNA or RNA sequence returns reversed sequence string.
        transcribe: for a DNA sequence returns transcribed RNA sequence string.
        complement: for a DNA sequence returns complement sequence string.
        reverse_complement: for a DNA sequence returns reversed complement sequence string.
    """
    if args[-1] == "is_nucleic_acid":
        return nt.is_nucleic_acid(*args[:-1])
    if args[-1] == "transcribe":
        return nt.transcribe(*args[:-1])
    if args[-1] == "reverse":
        return nt.reverse(*args[:-1])
    if args[-1] == "complement":
        return nt.complement(*args[:-1])
    if args[-1] == "reverse_complement":
        return nt.reverse_complement(*args[:-1])
    else:
        return "Unknown function"
    

def filter_fastq(seqs: dict, gc_bounds=(0, 100), 
                length_bounds=(0, 2**32), quality_threshold=0) -> dict:
    """
    Filters fastq file with DNA and RNA sequences.

    Args:
        seqs (dict): a dictionary 
        gc_bounds (tuple): a tuple with GC percentage boundaries (integer or float). Default is (0, 100).
        length_bounds (tuple): a tuple with length boundaries (only integer) Default is (0, 2**32). 
        quality_threshold (int): an integer or float number, lower boundary for mean quality. Default is 0.

    Returns:
        dict: a new dictionary that contains sequences corresponding to the given filter parameters.
    """
    filtered = {}
    for name, (seq, qual) in seqs.items():
        gc = ft.calc_gc(seq)
        length = len(seq)
        mean_q = ft.calc_mean_quality(qual)

        if (ft.in_bounds(gc, gc_bounds)
                and ft.in_bounds(length, length_bounds)
                and mean_q >= quality_threshold):
            filtered[name] = (seq, qual)

    return filtered 