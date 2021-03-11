#CV application
#Create 5 dictionaries. Each dictionary should represent a CV.
#Create a CV containing the information of the 5 created people.
#Print the information on CVs created on the screen.

#Question 1
CV1 = {"Ad":"Tuğra", "Soyad":"Ergin", "Yaş":20, "Meslek":"Bilgisayar Mühendisi", "Yetenekler":["Python","C++","C#"]}
CV2 = {"Ad":"Neriman", "Soyad":"Demir", "Yaş":25, "Meslek":"Endüstri Mühendisi", "Yetenekler":["Programlama","Organizasyon"]}
CV3 = {"Ad":"Ayşegül", "Soyad":"Çelik", "Yaş":21, "Meslek":"Makine Mühendisi", "Yetenekler":["Otomotiv","AutoCad","Solidworks"]}
CV4 = {"Ad":"Yusuf", "Soyad":"Çılgın", "Yaş":22, "Meslek":"Kimya Mühendisi", "Yetenekler":["Laboratuvar","GMP-GLP"]}
CV5 = {"Ad":"Aziz", "Soyad":"Ergin", "Yaş":24, "Meslek":"Elektrik Mühendisi", "Yetenekler":["Devreler","Aurdino","Boks"]}

for i,j in CV1.items():
  print(i, ":", j)

print("\n")

for i,j in CV2.items():
  print(i, ":", j)

print("\n")

for i,j in CV3.items():
  print(i, ":", j)

print("\n")

for i,j in CV4.items():
  print(i, ":", j)

print("\n")

for i,j in CV5.items():
  print(i, ":", j)
