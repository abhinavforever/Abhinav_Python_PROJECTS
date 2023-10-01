#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open('../Mail Merge Project Start/Input/Names/invited_names.txt',mode="r") as file:
    names=file.readlines() #list of names
    for i in range(len(names)):
        if i != len(names) - 1:
            name=names[i]
            name_l=list(name) #list of each character in the name
            name_l.remove("\n") #remove the last \n character from each name so that when creating a new file on line 18 no problem happens
            name="".join(name_l)
        with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as file1:
            x="[name]"
            letter=file1.readlines() #list of all the lines in the letter
            for line in letter:
                if x in line:
                    replacement=line.replace(x,name) #got hint from gfg
                    letter[0]=replacement #replace first line with a new line where the [name] is replaced by the actual name
            with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.txt",mode="w") as file2:
                file2.write("".join(letter))

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp