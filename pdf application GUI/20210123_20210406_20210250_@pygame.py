import os
import PyPDF2
import pygame
import sys

pygame.init()

#the application functions to apply on pdfs
def main():
 def extract(pdf_1,page_num):
    pdf_name = open(pdf_1,'rb')
    reader = PyPDF2.PdfFileReader(pdf_name)
    output_page = PyPDF2.PdfFileWriter()
    output_page.addPage(reader.getPage(page_num-1))
    output_file = '{}.-{}.pdf'.format(pdf_1,page_num)

    with open(output_file,'wb') as out :
        output_page.write(out)


 def split(pdf_1):
    file_name = os.path.splitext(os.path.basename(pdf_1))[0]
    pdf = PyPDF2.PdfFileReader(pdf_1)
    for page in range(pdf.getNumPages()):
        pdf_1_writer = PyPDF2.PdfFileWriter()
        pdf_1_writer.addPage(pdf.getPage(page))
        output_file = '{}-{}.pdf'.format(file_name,page+1)

        with open(output_file,'wb') as out:
            pdf_1_writer.write(out)



 def merge(pdf_1,pdf_2):
    
    pdfs = [pdf_1,pdf_2]
    merger = PyPDF2.PdfFileMerger()
    for pdfs in pdfs :
        merger.append(pdfs)
    merger.write('merged file.pdf')

##############################################################################################################

#the graphics codes 
 screen_color = (205, 255, 205)
 font = pygame.font.Font(None, 60)
 font1 = pygame.font.Font(None,45)
 pygame.display.set_caption("PDF application")
 screen = pygame.display.set_mode((800, 700))
 extract_button_color = (200, 190, 199)
 outline_color = (190, 190, 190)
 text_1_extract = font.render("Enter pdf name",True,(0,0,0))
 text_2_extract = font.render("Enter page number",True,(0,0,0))
 text_1_split=font.render("Enter pdf name",True,(0,0,0))
 text_1_merge=font.render("Enter first pdf",True,(0,0,0))
 text_2_merge=font.render("Enter second pdf",True,(0,0,0))
 text_ok = font.render("OK",True,(255,255,255))
 text_back= font.render("Back",True,(255,255,255))


 def extract_button():

    clock = pygame.time.Clock()
    user_text1 = ''
    user_text2 = ''
    active1 = False
    active2 = False
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            # getting input from the user for the extract() function 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False

            if event.type == pygame.KEYDOWN :
                if active1 == True :
                    if event.key == pygame.K_BACKSPACE:
                            user_text1 = user_text1[:-1]
                    else:
                            user_text1 += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec2.collidepoint(event.pos):
                     active2 = True
                else:
                    active2 = False

            if event.type == pygame.KEYDOWN :
                if active2 == True :
                    if event.key == pygame.K_BACKSPACE:
                            user_text2 = user_text2[:-1]
                    else:
                        user_text2 += event.unicode

            # applying the application extract() function on the entered texts 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok.collidepoint(event.pos):
                        extract(user_text1,int(user_text2))
            # click back button to return to the main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    main()

    
            screen.fill((0, 255, 255))
            screen_text1 = font1.render(user_text1,True,(0,0,0))
            screen_text2 = font1.render(user_text2,True,(0,0,0))
            screen.blit(text_1_extract, (20, 145))
            rec1 = pygame.draw.rect(screen, ("#ececec") ,(365,145,360,50))
            screen.blit(text_2_extract, (20, 290))
            rec2 =pygame.draw.rect(screen, ("#ececec") ,(426, 290, 300, 50))
            ok = pygame.draw.circle(screen,'lightgreen',(600,600),65,0)
            back =pygame.draw.circle(screen,'#FF6863',(150,600),65,0)
            screen.blit(screen_text1,(rec1.x+5,rec1.y+5))
            screen.blit(screen_text2,(rec2.x+5,rec2.y+5))
            screen.blit(text_ok,(565,580))
            screen.blit(text_back,(100,580))
            pygame.display.flip()
            clock.tick(15)
            pygame.display.update()



 def split_button():
    clock = pygame.time.Clock()
    user_text = ''
    active = False
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            # getting input from the user for the split() function 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            # applying the split() function on the entered text 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok.collidepoint(event.pos):
                        split(user_text)
            # click back button to return to the main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    main()

        screen.fill((153, 255, 153))
        screen_text = font1.render(user_text,True,(0,0,0))
        rec = pygame.draw.rect(screen, ("#ececec"), (365, 145, 360, 50))
        screen.blit(screen_text,(rec.x+5,rec.y+5))
        screen.blit(text_1_split, (20, 145))
        ok = pygame.draw.circle(screen,'lightgreen',(600,600),65,0)
        back = pygame.draw.circle(screen,'#FF6863',(150,600),65,0)
        screen.blit(text_ok,(565,580))
        screen.blit(text_back,(100,580))
        pygame.display.flip()
        clock.tick(15)
        pygame.display.update()


 def merge_button():

    user_text3 = ''
    user_text4 = ''
    active3 = False
    active4= False
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            # getting input from the user for the merge() function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec3.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False
            if event.type == pygame.KEYDOWN:
                if active3 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text3 = user_text3[:-1]
                    else:
                        user_text3 += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec4.collidepoint(event.pos):
                    active4 = True
                else:
                    active4 = False

            if event.type == pygame.KEYDOWN:
                if active4==True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text4 = user_text4[:-1]
                    else:
                        user_text4 += event.unicode
            # applying teh merge() function on the entered texts 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok.collidepoint(event.pos):
                    merge(user_text3,user_text4)
            # click back button to return to the main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    main()

            
        screen.fill((255, 255, 155))
        screen_text3 = font1.render(user_text3,True,(0,0,0))
        screen_text4 = font1.render(user_text4,True,(0,0,0))
        screen.blit(text_1_merge, (20, 145))
        rec3 = pygame.draw.rect(screen, ("#ececec"), (365, 145, 360, 50))
        screen.blit(text_2_merge, (20, 290))
        rec4 = pygame.draw.rect(screen, ("#ececec"), (426, 290, 300, 50))
        screen.blit(screen_text3,(rec3.x+5,rec3.y+5))
        screen.blit(screen_text4,(rec4.x+5,rec4.y+5))
        back =pygame.draw.circle(screen,'#FF6863',(150,600),65,0)
        ok = pygame.draw.circle(screen,'lightgreen',(600,600),65,0)
        screen.blit(text_ok,(565,580))
        screen.blit(text_back,(100,580))
        pygame.display.update()


 def exit_button():
    pygame.quit()
    sys.exit()

 running = True
 while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.fill(screen_color)
    mouse=pygame.mouse.get_pos()
    pygame.draw.rect(screen, outline_color, (270, 105, 260, 118))
    pygame.draw.rect(screen, outline_color, (260, 265, 270, 118))
    pygame.draw.rect(screen, outline_color, (270, 425, 260, 118))
    pygame.draw.rect(screen, outline_color, (270, 585, 260, 118))
    pygame.draw.rect(screen, (0, 255, 255), (250, 100, 270, 110))     #first button
    pygame.draw.rect(screen, (153, 255, 153), (250, 260, 270, 110))    #second button
    pygame.draw.rect(screen, (255, 255, 155), (250, 420, 270, 110)) #third button
    pygame.draw.rect(screen, (255, 153, 153), (250, 580, 270, 110)) #forth  button
    text_1 = font.render("EXTRACT",True,(224,244,244))
    text_2 = font.render("SPLIT", True, (255, 255, 255))
    text_3 = font.render("MERGE", True, (200, 200, 200))
    text_4 = font.render("EXIT", True, (255, 255, 255))
    screen.blit(text_1, (290,145))
    screen.blit(text_2, (330, 305))
    screen.blit(text_3, (315, 465))
    screen.blit(text_4, (335, 620))

    if 250+270>mouse[0]>250 and 100+110>mouse[1]>100:
        pygame.draw.rect(screen,(80,200, 200), (250, 100, 270, 110))
        screen.blit(text_1, (290,145))
        if event.type==pygame.MOUSEBUTTONDOWN:
            extract_button()

    if 250+270>mouse[0]>250 and 260+110>mouse[1]>260:
        pygame.draw.rect(screen, (102,255,102), (250, 260, 270, 110))
        screen.blit(text_2, (330, 305))
        if event.type==pygame.MOUSEBUTTONDOWN:
            split_button()
    if 250+270>mouse[0]>250 and 420+110>mouse[1]>420:
        pygame.draw.rect(screen, (255,255,51), (250, 420, 270, 110))
        screen.blit(text_3, (315, 465))
        if event.type == pygame.MOUSEBUTTONDOWN:
            merge_button()
    if 250+270>mouse[0]>250 and 580+110>mouse[1]>580:
        pygame.draw.rect(screen, (255,102,102), (250, 580, 270, 110))
        screen.blit(text_4, (335, 620))

        if event.type == pygame.MOUSEBUTTONDOWN:
            exit_button()
    pygame.display.update()

 pygame.quit()
main()