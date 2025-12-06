def is_nucleic_acid(*seqs: str) -> bool:
    nucleotides = "ATCGUatcgu"
    result = []
    for seq in seqs:
        rna = False
        dna = False
        not_nuc = False
        if seq == "":
            result.append(False)
            continue
        for i in seq:
            if i not in nucleotides:
                not_nuc = True
                break
            if i == "T" or i == "t":
                dna = True
            if i == "U" or i == "u":
                rna = True
        if not_nuc or (dna and rna):
            result.append(False)
        else:
            result.append(True)
    if len(result) == 1:
        return result[0]
    return result


def transcribe(*seqs: str):
    table = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G",
        "a": "u",
        "t": "a",
        "g": "c",
        "c": "g",
    }
    result = []
    for seq in seqs:
        rna = ""
        is_nuc = is_nucleic_acid(seq)
        for c in seq:
            if is_nuc and c in table:
                rna += table[c]
            else:
                rna = "Not a DNA sequence, transcript can`t be made"
                break
        result.append(rna)
    if len(result) == 1:
        return result[0]
    return result


def reverse(*seqs: str):
    result = []
    for seq in seqs:
        rev = ""
        is_nuc = is_nucleic_acid(seq)
        for c in seq[::-1]:
            if not is_nuc:
                rev = "Not a nucleic acid"
                break
            else:
                rev += c
        result.append(rev)
    if len(result) == 1:
        return result[0]
    return result


def complement(*seqs: str):
    table = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "a": "t",
        "t": "a",
        "g": "c",
        "c": "g",
    }
    result = []
    for seq in seqs:
        complement = ""
        is_nuc = is_nucleic_acid(seq)
        for c in seq:
            if is_nuc and c in table:
                complement += table[c]
            else:
                complement = "Not a DNA sequence, complement sequence can`t be made"
                break
        result.append(complement)
    if len(result) == 1:
        return result[0]
    return result


def reverse_complement(*seqs: str):
    table = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "a": "t",
        "t": "a",
        "g": "c",
        "c": "g",
    }
    result = []
    for seq in seqs:
        rev_complement = ""
        is_nuc = is_nucleic_acid(seq)
        for c in seq[::-1]:
            if is_nuc and c in table:
                rev_complement += table[c]
            else:
                rev_complement = (
                    "Not a DNA sequence, reverse complement sequence can`t be made"
                )
                break
        result.append(rev_complement)
    if len(result) == 1:
        return result[0]
    return result