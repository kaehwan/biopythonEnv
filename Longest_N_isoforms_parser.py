from __future__ import print_function
from Bio import SeqIO
from argparse import ArgumentParser

def main():
    args = get_args()
    last_gene = None
    transcripts = []

    for seq_record in SeqIO.parse(args.input, "fasta"):
        gene = seq_record.id

        if last_gene == None:
            last_gene = gene

        if last_gene == gene:
            transcripts.append(seq_record)
        else:
            print_longest_transcripts(transcripts, args.number)
            last_gene = gene
            transcripts = [seq_record]

    print_longest_transcripts(transcripts, args.number)


def print_longest_transcripts(transcripts, number):
    longest = sorted(transcripts, key=lambda x: len(x.seq), reverse=True)

    for seq_record in longest[:number]:
        print(">" + seq_record.id, seq_record.seq, sep="\n")


def get_args():
    parser = ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="input fasta", required=True)
    parser.add_argument("-n", "--number", help="number of longest transcripts per gene", type=int, required=True)
    return parser.parse_args()

if __name__ == '__main__':
    main()

