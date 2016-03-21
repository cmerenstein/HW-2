#Carter Merenstein
#MATH0216 HW2
# This script counts words that are used by females, males, and total. It uses a "bag of words" approach, meaning it totally ignores context, and jumbles all essays together

import re

pattern = re.compile('\W|\d') # not an alphanumeric

male_words = {}
female_words = {}
all_words = {}

with open("essays.csv", mode = 'r', encoding = "utf8") as profiles:
    current_line = ""
    for line in profiles:
        current_line = current_line + line
        if "@@@" in line:
            female = False
            if "FEMALE$$" in current_line:
                female = True
            words_in_line = {} # dict is faster
            current_line_words = current_line.split(" ")
            for word in current_line_words:
                word = re.sub(pattern, '', word) #get rid of commas and stuff
                word = word.lower()
                
                try:
                    words_in_line[word]
                    #nothing happens here, we've already seen this word (I'm counting number of people that used a word, so I don't count duplicates in a line)
                except:
                    words_in_line[word] = 1
                    try:
                            all_words[word] += 1
                    except:
                            all_words[word] = 1
                    if female:
                        try:
                            female_words[word] += 1
                        except:
                            female_words[word] = 1
                    else:
                        try:
                            male_words[word] += 1
                        except:
                            male_words[word] = 1
                 
            current_line = ""

            
with open("word_count.csv", mode = 'w', newline="") as f_out:
    f_out.write("word" + "," + "in_females" + "," + "in_males" + "," +"in_total" + ",\n")
    for word in all_words.keys():
        if all_words[word]> 50: ## only want words that occur in > 50 entries
            row = word + ","
            try:
                row = row + str(female_words[word]) + ","
            except:
                row = row + "0,"
            try:
                row = row + str(male_words[word]) + ","
            except:
                row = row + "0,"
            row = row + str(all_words[word]) + ",\n"
            f_out.write(row)
