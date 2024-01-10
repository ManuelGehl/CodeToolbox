def reverse_complement(self, dna_sequence: str) -> str:
        """
        Compute the reverse complement of a DNA sequence.

        Args:
            sequence (str): The input DNA sequence for which the reverse complement is calculated.

        Returns:
            str: The reverse complement of the input DNA sequence.

        Takes a DNA sequence as input and computes its reverse complement.
        The reverse complement is obtained by reversing the input sequence and mapping
        each nucleotide to its complement (A to T, T to A, G to C, and C to G).

        Example:
            If the input sequence is 'ATGC', the reverse complement will be 'GCAT'.
        """
        # Reverse DNA sequence
        rev_seq = dna_sequence[::-1]
        # Define mapping dictionary
        mapping_dict = {"A": "T",
                        "T": "A",
                        "G": "C",
                        "C": "G"}
        # Map characters in sequence
        complement_seq = [mapping_dict[char] for char in rev_seq]
        return "".join(complement_seq)
