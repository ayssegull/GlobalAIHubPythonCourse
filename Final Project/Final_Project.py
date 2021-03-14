#Write a knowledge competition program.
#It should consist of 10 questions in total.
#Each question will have only one answer.
#Adjust the answers of the questions according to case sensivity.
#Each question should be worth 10 points.
#If User answers 5 or fewer questions, it will be considered unsuccessful.
#If the user answers more than 5 questions correctly, it will be considered successful.




questions = {"Türkiye'nin başkenti neresidir?":"ankara",
             "Güney Kore'nin başkenti neresidir?":"seul",
             "Avusturalya'nın başkenti neresidir?":"kanberra",
             "Yeni Zellanda'nın başkenti neresidir?":"wellington",
             "Amerikan'nın başkenti neresidir?":"washington,DC",
             "İngiltere'nin başkenti neresidir?":"londra",
             "Fransa'nın başkenti neresidir?":"paris",
             "Japonya'nın başkenti neresidir?":"tokyo",
             "Rusya'nın başkenti neresidir?":"moskova",
             "Almanya'nın başkenti neresidir?":"berlin"}

scores = 0

for i,j in questions.items():
    print(i)
    answer = input()
    if (j == answer.lower()):
        print("\nTebrikler! 10 puan kazandınız!\n")
        scores += 10
    else:
        print(f'\nÜzgünüm! Doğru cevap {j.title()} olacaktı.\n')
    
if(scores > 50):
    print(f'\nYarışmayı başarıyla tamamladınız. Toplam {scores} puan kazandınız!')
else:
    print(f'\nYarışmayı başarıyla tamamlayamadınız. Toplam {scores} puan kazandınız!')
    
