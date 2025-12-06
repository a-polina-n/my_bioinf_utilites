# My bIoInF uTiLiTeS

This is my study project for the homework. I wrote scripts that can do some manipulations with DNA (mostly) and RNA sequences. 
Tools don`t require installation, you can use it considering that all tools were written with Python version 3.12.12.

## main

### Function run_dna_rna_tools

This function takes a series of strings (DNA or DNA sequences) for arguments, note that __the last string must be one of the procedures__ you want to perform:

* is_nucleic_acid: checks if given strings are nucleic acids at all; returns bool.
* reverse: for a DNA or RNA sequence returns reversed sequence string.
* transcribe: for a DNA sequence returns transcribed RNA sequence string.
* complement: for a DNA sequence returns complement sequence string.
* reverse_complement: for a DNA sequence returns reversed complement sequence string.

You can use both lowercase, UPPERCASE and mIxEd letters for nucleic acid sequences.

__Examples:__

```python
print(run_dna_rna_tools("ATGCTTCTCCCCTTC", "UTCGACCGTU", "is_nucleic_acid")) # [True, False]

print(run_dna_rna_tools("GTA", "reverse_complement")) # TAC
```

### Function filter_fastq

This function takes in a dictionary with fastq files, and filter for parameters as arguments:

* gc_bounds (tuple): a tuple with GC percentage boundaries (integer or float). Default is (0, 100).
* length_bounds (tuple): a tuple with length boundaries (only integer) Default is (0, 2**32). 
* quality_threshold (int): an integer or float number, lower boundary for mean quality. Default is 0.

The function returns a new, filtered dictionary.

## Contacts
Hope these tools may help you! :)
Any suggestions? Telegram: @a_polina_n
