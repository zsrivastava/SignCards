# coding=utf-8
import random
from fpdf import FPDF
signs = {2: "Second Sign", 3: "Third Sign", 5: "Chase 1", 6: "Chase 2", \
         7: "Chase 3", 4: "Chase 4", 8: 'Outs + 1', 9: 'Outs + 2'}

eng_span = {"First Sign": "Primera Seña", "Second Sign": "Segunda Seña", "Third Sign": "Tercera Seña", \
            "Last Sign": "Última Seña", "Chase 1": "Después de 1", "Chase 2": "Después de 2", \
            "Chase 3": "Después de 3", "Chase 4": "Después de 4", 'Outs + 1': 'Outs + 1', 'Outs + 2': 'Outs + 2'}

special_signs = {1: "Glove", 2: "Mask", 3: "Chest", 4: "1st Touch", 5: "2nd Touch"}

special_span = {"1st Touch": "Primer Toque", "2nd Touch": "Segundo Toque", "Glove": "Guante", \
            "Mask": "Máscara", 'Chest': 'Pecho'}

def cards(pitcher, catcher, special, f, g): #1 for eng, 0 for span
    player_names = []
    num_players = int(input('How many players do you need sign-cards for? '))
    i = 0
    while(i < num_players):
        player = input("Player " + str(i+1) + " name: ")
        player_names.append(player)
        i += 1

    for x in range(len(player_names)):
        eng_list = []
        span_list = []
        eng_num = 1
        if(special == 0):
            num_signs = 5
            list = random.sample(range(2, 10), 5)
            for elem in list:
                eng_list.append(signs[elem])
                span_list.append(eng_span[signs[elem]])
        else:
            num_signs = 5
            list = random.sample(range(1, 6), 5)
            for elem in list:
                eng_list.append(special_signs[elem])
                span_list.append(special_span[special_signs[elem]])

        if pitcher: # is english
            f.write(player_names[x])
            f.write('\n\n')
            for i in range(num_signs):
                f.write(str(i+1)+': '+eng_list[i])
                f.write('\n')
            f.write('\n\n')
            
#            if(special == 1):
#                f.write('\n')

        else:
            f.write(player_names[x])
            f.write('\n\n')
            for i in range(num_signs):
                f.write(str(i + 1) + ': ' + span_list[i])
                f.write('\n')
            f.write('\n\n')
            
#            if (special == 1):
#                f.write('\n')

        if(catcher == 1 or catcher == 2): # is english speaking
            g.write(player_names[x])
            g.write('\n\n')
            for i in range(num_signs):
                g.write(str(i+1)+': '+eng_list[i])
                g.write('\n')
            g.write('\n\n') 
            if(special == 1):
                g.write('\n')
        
        if(catcher == 0 or catcher == 2):
            g.write(player_names[x])
            g.write('\n\n')
            for i in range(num_signs):
                g.write(str(i + 1) + ': ' + span_list[i])
                g.write('\n')
            g.write('\n\n')
            if (special == 1):
                g.write('\n')
                


with open('signcards.txt', 'w') as f, open('catchercards.txt', 'w') as g:
    # If you don't want to don't need to be asked something, comment the lines out with a #
    good = False
    while(not good):
        catch = input("Catcher cards in English or Spanish? (E for English, S for Spanish, B for Both): ")
        if(catch == 'E'):
            catch = 1
            good = True
        elif(catch == 'B'):
            catch = 2
            good = True
        elif(catch == 'S'):
            catch = 0
            good = True
        
    print()    
    print("English Pitchers (Regular)")
    cards(1, catch, 0, f, g)
    print()
    
    print("Spanish Pitchers (Regular)")
    cards(0, catch, 0, f, g)
    print()
#    
#    print("Spanish Only")
#    cards(0, 1, 0, f)
#    
    print("Special Only English")
    cards(1, catch, 1, f, g)
    print()

    
    print("Special Spanish Only")
    cards(0, catch, 1, f, g)
    print() 
    print('Sign Cards Generated!')
#    print("Type 'cat signcards.txt' below")
    
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=9)
pdf.set_auto_page_break(True, 0)
f = open('signcards.txt', 'r')
g = open('catchercards.txt', 'r')
start = 20
i = 0
for x in f:
    if(i > 60):
        pdf.cell(30)
#    print(x)
    if(i % 9 == 0):
        pdf.set_font("Arial", size=9, style='B')
        layout = 'L'
    else:
        pdf.set_font("Arial", size=9)
        layout = 'L'

    if(i % 54 == 0): # resets column
        pdf.y = 10
    col = i // 54 + 1

    if(col == 1):
        pdf.x = 10
        pdf.multi_cell(30, 5, txt=x, align = layout)
        
    elif(col == 2):
        pdf.x = 90
        pdf.multi_cell(30, 5, txt=x, align = layout)
        
    elif(col == 3):
        pdf.x = 170
        pdf.multi_cell(30, 5, txt=x, align = layout)
    i += 1
    if(i % 162 == 0):
        pdf.add_page()
        i = 0
    
pdf.add_page() 
text = ''
width = 75
height = 7
i = 1
for x in g:
    if(i % 31 == 0):
        pdf.y = 0
    col = i // 31 + 1
    if(x != '\n'):
        if(col == 1):
            pdf.x = 10
        elif(col == 2):
            pdf.x = 125
        if((i-1) % 6 == 0):
            if(i != 1):
                pdf.y += 10
#            name_len = len(x)-1
            pdf.set_font("Arial", size=10, style='BU')
            text = x
            pdf.multi_cell(width, height, txt=text, border='TLR', align='C')
        else:
#            fpdf.set_font(family="Arial", style='')
            pdf.set_font("Arial", size=9)
            text = x
            if(i % 6 == 0):
                pdf.multi_cell(width, height, txt=text, border='LRB', align='C')
            else:
                pdf.multi_cell(width, height, txt=text, border='LR', align='C')
        i += 1
        if(i % 61 == 0):
            pdf.add_page()
            pdf.y = 10
            i = 1
        
pdf.output("signcards.pdf")
