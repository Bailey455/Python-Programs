#function to check all of the parameters
def checkWord(word, worksheet):
    special_signs = ["?", ",", ":", ";", "(", ")", "."]
    multiple_entries = []
    full_phrase = ""
    mult_phrase = ""
    sign_num = 0
    row = 0
    col = 0
    header = False

    count = 0
    
    #traversing through all of the file
    for line in f:
        i = 0
        line_split = line.split()
        
        #checking special signs
        for x in range(len(special_signs)):
            special_word = word + special_signs[x]
            if special_word in line_split:
                word = special_word
                
        #getting first name
        if word == "Attached" and count == 0:
            if word in line_split:
                index = line_split.index(word)
                first_name = line_split[index + 5]
                
                if "for" not in first_name:
                    return(first_name)
            
        
        #getting name
        elif word == "poster":
            if word in line_split:
                #print(line_split)
                index = line_split.index(word)
                poster = line_split[index + 3]
 
                for n in range(len(poster)):
                    full_phrase = full_phrase + poster[n] + " "

                #checking for commas at the ends
                if "," in full_phrase[len(full_phrase) -1]:
                    full_phrase = full_phrase[0:len(full_phrase) -1]
                if "," in full_phrase[len(full_phrase) -2]:
                    full_phrase = full_phrase[0:len(full_phrase) -2]

                return full_phrase
        
        #getting age
        elif word == "age":
            if word in line_split:
                index = line_split.index(word)
                age = line_split[index + 1]
            
                #checking for commas at the end
                if "," in age[len(age) -1]:
                    age = age[0: len(age) - 1]
                if "," in age[len(age) -2]:
                    age = age[0: len(age) - 2]
            
                return age
            
        #geting gender
        elif word == "who":
            if word in line_split:
                index = line_split.index(word)
                gender = line_split[index - 1]
                
                if "," in gender[len(gender) -1]:
                    gender = gender[0: len(gender) - 1]
                if "," in gender[len(gender) -2]:
                    gender = gender[0: len(gender) - 2]
                
                return gender
        
        #getting how long missing
        elif word == "missing":
            if word in line_split:
                index = line_split.index(word)
                missing = line_split[index + 2: index + 5]
            
                for n in range(len(missing)):
                    if missing[n] == "since":
                        break
                    full_phrase = full_phrase + missing[n] + " "
            
                return full_phrase
        
        #getting date missing
        elif word == "since":
            if word in line_split:
                index = line_split.index(word)
                last_index = len(line_split)
                date = line_split[index + 1: last_index]
                
                for n in range(len(date)):
                    full_phrase = full_phrase + date[n] + " "
                    
                if "." in full_phrase[len(full_phrase) -1]:
                    full_phrase = full_phrase[0: len(full_phrase) - 1]
                if "." in full_phrase[len(full_phrase) -2]:
                    full_phrase = full_phrase[0: len(full_phrase) - 2]
                    
                return full_phrase
        
        
        #getting parameters other than poster, age, and missing
        elif word in line_split:        
            count += 1   
            #print(count)
            
            index = line_split.index(word)
            last_index = len(line_split) -1

            phrase = line_split[index + 1: last_index + 1]
            
            if count == 1:
                for num in range(len(phrase)):
                    full_phrase = full_phrase + phrase[num] + " "
                
                if word == "locations" and word in line_split:
                    full_phrase = ""
                
            if count > 1:
                for num in range(len(phrase)):
                    mult_phrase = mult_phrase + phrase[num] + " "
                    
            full_phrase = full_phrase + mult_phrase
                                    
    return (full_phrase)
                
                
#beginning of main method                
import xlsxwriter
import pandas as pd
import os

workbook = xlsxwriter.Workbook('H://Desktop/missing_kids.xlsx')
worksheet = workbook.add_worksheet()

entries = 0
col = 0

#loop to check for each value
while True:
    directory = str(input("What folder do you want to use? (Please use H://Desktop/____ or H://Downloads/___) Enter quit to end  "))
    
    if directory == "quit":
        break
        
    else:
        titles = ["First Name", "Last Name", "Age", "Gender", "Missing From", "Date Missing", "Physical Identifiers", "Incident", "Missing Episodes", "Risks", "Possible Locations", "Social Media", "Last School Attended", "Nickname/Alias", "Possible Companions"]
        for t in range(len(titles)):
            #print(worksheet)
            worksheet.write(0, col, titles[t])
            col+= 1
        col = 0
        entries += 1

       
        parameters = ["Attached", "poster", "age", "who", "missing", "since", "identifiers", "Incident","episodes", "Risks", "locations", "media", "Attended", "Nickname/Alias", "companion"]

        #to navigate through orginal pathway, years, and files within month folders
        for folder in os.listdir(directory):
            for file in os.listdir(directory + "/" + folder):
                for filename in os.listdir(directory + "/" + folder + "/" + file):
                    if filename.endswith(".txt"):
                        #print(file, filename)
                        for i in range(len(parameters)):
                            f = open(directory + "/" + folder + "/" + file + "/" + filename)
                            #print(checkWord(parameters[i], worksheet))
                            worksheet.write(entries, col, checkWord(parameters[i], worksheet))
                            col +=1 
                    entries += 1
                    col = 0    
            col = 0
        
f.close()
workbook.close()