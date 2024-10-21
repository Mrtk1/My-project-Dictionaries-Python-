language=input("Which language do you speak - Hangi dil konuşuyorsun?")
if language=="Türkçe":
    meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "COOL":"Baya şaşırtıcı ve güzel bir şey",
                "CHALLENGE":"Bir meydan okuma gibi bir şey",
                "LETS GO":"Hadi gidelim anlamına gelir.",
                }
    word = input("Anlamadığınız bir kelime yazınız. Lütfen büyük harfle yazınız.")

            if word in meme_dict.keys():
            if word=="COOL":
                print(meme_dict["COOL"])
            elif word=="LOL":
                print(meme_dict["LOL"])
            elif word=="CHALLENGE":
                print(meme_dict["CHALLENGE"])
            elif word=="CRINGE":
                print(meme_dict["CRINGE"])
            elif word=="LETS GO":
                print(meme_dict["LETS GO"])
        else:
            print("Böyle bir kelime bulunamadı.")

```
#if language == "English":
        #meme_dict = {
                #"GARIP": "A weird or cringe thing",
                #"LOL": "Answer to a funny message",
                #"COOL":"A shocking good thing",
                #"CHALLENGE":"You probably already know this",
                #"LETS GO":"You probably know this too",
                     #}
    #word = input("Type a word that you don't know in big letters")
    
        #if word in meme_dict.keys():
        #if word=="COOL":
                #print(meme_dict["COOL"])
        #elif word=="LOL":
                #print(meme_dict["LOL"])
        #elif word=="CHALLENGE":
                #print(meme_dict["CHALLENGE"])
        #elif word=="CRINGE":
            #print(meme_dict["CRINGE"])
        #elif word=="LETS GO":
            #print(meme_dict["LETS GO"])
    #else:
        #print("There isn't the word you are asking in the dictionary")
```
