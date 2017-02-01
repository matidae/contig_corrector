import sys
from Bio import SeqIO
from Bio.Seq import Seq

fasta = SeqIO.index(sys.argv[2], "fasta")

with open(sys.argv[1]) as fh:
    for i in fh:
        contig_name = i.split()[3].split('_')[0]
        gene_name = i.split()[3]
        strand = i.split()[5]
        vec_pos = i.rstrip().split()[6].replace('<','').replace('>','').split(",")
        contig_seq = str(fasta[contig_name].seq)
        cds_seq = ""
        for j in vec_pos:
            try:
                start = int(j.split(":")[0])
                end = int(j.split(":")[1])
                cds_seq += contig_seq[start-1:end] 
            except:
                pass
        print ">" + gene_name, strand, vec_pos
        if strand == "+":
            print cds_seq
            #print ">" + gene_name+"_pep", strand, vec_pos
            #print Seq(cds_seq).translate()
        else:
            print Seq(cds_seq).reverse_complement()
            #print ">" + gene_name+"_pep", strand, vec_pos
            #print Seq(cds_seq).reverse_complement().translate()
