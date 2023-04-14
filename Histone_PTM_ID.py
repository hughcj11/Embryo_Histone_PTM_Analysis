import csv
import re
with open('Code Testing Doc.csv') as csvfile:
    #For a new csv file, change the above parenthesis
    cellreader = csv.reader(csvfile, delimiter=',')
    count=0
    #For all rows, we collect "answers" in a list. These are the answers that we are getting as we go row by row
    answers=[]
    for row in cellreader:
        count=count+1
        if count<=2:
            continue
        ua=row[3]
        #For each row, we will get an answer
        answer=[row[1],row[2],row[5],row[6],ua]
        #Below defines which row we need to read to get several answers
        parts = ua.split(".")
        parts=parts[1:-1]
        parts=".".join(parts)
        #The above code looks for the periods in the row in order to pull out the peptide sequence and ptms. This should split that cell into 3 parts
        pep_seq=parts
        last_amino=""
        #unimod refers to the type of modifcation 
        #mod_amino refers to the residue being modified 
        #mod_pos refers to the position in that seqeunce being modified
        mod_amino=""
        unimod=""
        mod_pos=-1
        should_count=True
        for amino in pep_seq: 
            if amino==")":
                pep_mod_pos=mod_pos+int(row[5])
                answer.append(pep_mod_pos)
                answer.append(mod_amino)
                answer.append(unimod)
                #After the answer is recorded, the below text "resets" the code to count again
                mod_amino=""
                unimod=""
                should_count=True
                mod_pos = mod_pos -1
            else:
                if unimod!="":
                    unimod=unimod+amino
                if amino=="(":
                    should_count=False
                    mod_amino=last_amino
                if last_amino==":":
                    unimod=amino
            last_amino=amino
            if should_count:
                    mod_pos=mod_pos+1         
        answers.append(answer)
#The code below is transferring the information above into the first csv file
with open('IntermediatePTMSheet.csv', 'w') as csvfile:
    cellwriter = csv.writer(csvfile, delimiter=',')
    cellwriter.writerow(["","","", "","", "Modification 1", "", "", "Modification 2","", "", "Modification 3"])
    cellwriter.writerow(["Protein","Protein Description","Begin Pos", "End Pos","Unimod Acession", "Position", "Residue", "Unimod", "Position", "Residue", "Unimod", "Position", "Residue", "Unimod"])
    for row_answer in answers:
        cellwriter.writerow(row_answer)




#The code below is transferring the information above into the second csv file
with open('IntermediatePTMSheet2.csv', 'w') as csvfile:
    cellwriter = csv.writer(csvfile, delimiter=',')
    cellwriter.writerow(["Protein","Protein Description","Position","Residue","Unimod", "hPTM_ID"])
    library=[]
    for row_answer in answers:
        pattern = 'H\d[AB]?'
        string = row_answer[1]
        result = re.search(pattern, string)
        #print(result.group())
        all_mods=row_answer[5:]
        for i in range(len(all_mods)):
            if i%3==0:
                position=all_mods[i]
            if i%3==1:
                residue=all_mods[i]
            if i%3==2:
                unimod=all_mods[i]
                concat=row_answer[0]+"."+result.group()+"."+str(position)+"."+residue+"."+unimod
                library.append(concat)
                cellwriter.writerow([row_answer[0],result.group(),position,residue,unimod,concat])





with open('HistonePTMLibrary.csv', 'w') as csvfile:
    cellwriter = csv.writer(csvfile, delimiter=',')
    cellwriter.writerow(["hPTM_ID","Protein Accession","Protein Description","Position","Amino Acid","Amino Acid Position","Unimod","PTM Description","Biological Relevance"])
    library=set(library)
    for libraryanswer in library:
        cellwriter.writerow([libraryanswer])    