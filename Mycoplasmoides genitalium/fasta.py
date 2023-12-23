

path_fna = "genome.fna"

with open(path_fna, 'r') as file:

    get_lines= file.readlines()
    num_rows= len(get_lines)
    print(f"The number of rows in the file is {num_rows}")

    file.seek(0)
    i=0
    a=0
    AA=0
    old_len_aa= None

    for line in file:
        aa_per_line=len(line.strip())
        first_character=line.strip()[0]

        if(i==0 and first_character == '>'):
            print("GOOD :: the first line of the file starts with '>' ")
            a+=1

        if(i>0):
            AA+=aa_per_line
                    
        
        if(i>1 ):
            
            if(aa_per_line != old_len_aa and i < num_rows-2 ):
                print("BAD :: The file HAS NOT the same number of Amino Acids in each line")
                print(i)
                break
            if(i== num_rows-2):
                print("GOOD :: the file has the same number of AA in each line")
                a+=1
        
        old_len_aa=aa_per_line
        i+=1
    
    if(a==2):
        print('GOOD :: Valid FASTA file¡¡')
        print(f"Amino Acids = {AA}")
        