

path_fna = "genome.fna"

with open(path_fna, 'r') as file:

    get_lines= file.readlines()
    num_rows= len(get_lines)
    print(f"The number of rows in the file is {num_rows}")

    file.seek(0)
    i=0
    a=0
    NB=0
    old_len_bn= None
    nitrogen_bases=[]

    for line in file:
        bn_per_line=len(line.strip())
        first_character=line.strip()[0]

        if(i==0 and first_character == '>'):
            print("GOOD :: the first line of the file starts with '>' ")
            a+=1

        if(i>0):
            NB+=bn_per_line
            for nbase in line:
                if(nbase != '\n'):
                    nitrogen_bases.append(nbase)
                    if(nbase not in ('A','C','G','T')):
                        print(f"BAD :: The file has letters different to A,T,C,G :{nbase} in position: {i}")
                        a-=1
                
                    
        
        if(i>1 ):
            
            if(bn_per_line != old_len_bn and i < num_rows-2 ):
                print("BAD :: The file HAS NOT the same number of Nitrogen BAses in each line")
                print(i)
                break
            if(i== num_rows-2):
                print("GOOD :: the file has the same number of Nitrogen Bases in each line")
                a+=1
        
        old_len_bn=bn_per_line
        i+=1
    
    if(a==2):
        print('GOOD :: Valid FASTA file¡¡')
    
    print(f"Nitrogen Bases = {NB}")
    print('')

#Vamos a iniciar por definir los 64 codones posibles, y vamos a crear un dccionario con estos codones para contar cuantas 
#veces aparecen en el FASTA     
    print('Iniciando diccionario de codones ADN:')

codons = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT',
          'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT',
          'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT',
          'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']

codon_dictionary= {codon: 0 for codon in codons}


n = len(nitrogen_bases)

for i in range(2,n):
    codon= nitrogen_bases[i-2] + nitrogen_bases[i-1] + nitrogen_bases[i]
    if (codon in codon_dictionary):
        codon_dictionary[codon] += 1
    else:
        print(f"ERROR: A 'codon' could not be found in the dictionary: {codon}")

# Print the codon counts
for codon, count in codon_dictionary.items():
    print(f"{codon}: {count} occurrences")
