#imports a library included in Python to give extra functions
from collections import Counter

"""function takes in a filepath then opens & parses the
fasta file returning a dictionary {'label':'seq'}."""
def open_and_parse_fasta(filepath):
    FASTA_file = open(f"{filepath}", "r")
    FASTA_dict = {} 
    FASTA_label = ""
    for line in FASTA_file: 
        line = line.rstrip() #removes spaces and newline chars each line
        if line.startswith(">"): #catches sequence label
            FASTA_label = line[1:] #set the label as 1st char and after
            #set sequence label in dict with empty string
            FASTA_dict[FASTA_label] = "" 
        else: #must be sequence
            #add sequence to end of dict entry
            FASTA_dict[FASTA_label] += line 
    return FASTA_dict

#function to count base occurence and print results
def count_bases():
  #run our open FASTA function and set returned FASTA_dict to FASTA variable
  FASTA = open_and_parse_fasta("/GCF_000010365.1_ASM1036v1_genomic.fna")
  #select the sequence we want to look at from the dict
  carsonella_ruddi = FASTA.get('NC_008512.1 Candidatus Carsonella ruddii PV DNA, complete genome')
  #counts and prints the bases in the genome
  print(Counter(carsonella_ruddi)


if __name__ == "__main__"
  count_bases()