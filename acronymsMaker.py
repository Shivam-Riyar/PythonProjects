wordinput = str(input("ENTER A PHRASE : "))
text = wordinput.split()
acr = " "
for i in text : 
  acr = acr + str(i[0].upper()
print("ACRONYM FOR : " + wordinput + " IS : " + acr)
