from Bio import SeqIO

fasta_file = "CHO.fasta"

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    if len(str(seq_record.seq)) >= 500:
        print(seq_record.id)

import json
