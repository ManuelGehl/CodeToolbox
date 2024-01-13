# Define dictionaries with codons for mapping
RNA_CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L",
    "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I", "AUC": "I",
    "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V",
    "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T",
    "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A", "GCC": "A",
    "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "Stop",
    "UAG": "Stop", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D",
    "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C", 
    "UGA": "Stop", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R",
    "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", 
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
DNA_CODON_TABLE = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T',
    'ACT': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S', 'ATA': 'I', 'ATC': 'I',
    'ATG': 'M', 'ATT': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H', 'CCA': 'P',
    'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
    'GAT': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GGA': 'G', 'GGC': 'G',
    'GGG': 'G', 'GGT': 'G', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'TAC': 'Y',
    'TAT': 'Y', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TGC': 'C', 'TGG': 'W',
    'TGT': 'C', 'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F', "TAG": "Stop", "TGA": "Stop",
    "TAA": "Stop"}

# Define class for custom exception
class InvalidModeError(ValueError):
    pass
    
def codon_mapping(sequence: str, mode: str) -> str:
    """
    Maps codons (3-mers) of a sequence against amino acids.

    Parameters:
    - sequence (str): DNA or RNA sequence.
    - mode (str): Specifies the type of sequence ("DNA" or "RNA").

    Returns:
    - str: Amino acid sequence.
    """
    # Check if mode is correct
    if mode not in ["DNA", "RNA"]:
        raise InvalidModeError("Invalid mode. Mode must be either 'DNA' or 'RNA'")
    
    # Select appropriate codon table
    codon_table = DNA_CODON_TABLE if mode == "DNA" else RNA_CODON_TABLE
    
    # Loop trough the sequence and map each codon to an amino acid
    amino_acid_seq = []
    for codon_index in range(0, len(sequence), 3):
        current_amino = codon_table.get(sequence[codon_index:codon_index+3], None)
    # Print a message when unknown codon is in sequence
        if current_amino is None:
            print(f"Unknown codon at position: {codon_index}-{codon_index+3}")
        if current_amino != "Stop":
            amino_acid_seq.append(current_amino)
            
    # Combine list to string
    return "".join(amino_acid_seq)
    