# mostro i possibili casi
print("")
print("A: tutti x sono y")
print("I: qualche x è y")
print("E: nessun x è y")
print("O: non tutti x sono y")
print("")

# chiedo in input le premesse e la conclusione
premessa1 = str(input("Qual'è la prima premessa? (minuscolo): "))
premessa2 = str(input("Qual'è la seconda premessa? (minuscolo): "))
conclusione = str(input("Qual'è la conclusione? (minuscolo): "))
print("")

sillogismo = premessa1 + premessa2 + conclusione

# verifico la correttezza dei dati
 # prima figura
correctsyntaxarray_figura1_modo1 = "tutti m sono ptutti s sono mtutti s sono p"
correctsyntaxarray_figura1_modo2 = "nessun m è ptutti s sono mnessun s è p"
correctsyntaxarray_figura1_modo3 = "tutti m sono pqualche s è mqualche s è p"
correctsyntaxarray_figura1_modo4 = "nessun m è pqulche s è mnon tutti s sono p"
 # seconda figura
correctsyntaxarray_figura2_modo1 = "nessun p è mtutti s sono mnessun s è p"
correctsyntaxarray_figura2_modo2 = "tutti p sono mnessun s è mnessun s è p"
correctsyntaxarray_figura2_modo3 = "nessun p è mqualche s è mnon tutti s sono p"
correctsyntaxarray_figura2_modo4 = "tutti p sono mnon tutti s sono mnon tutti s sono p"
 # terza figura
correctsyntaxarray_figura3_modo1 = "tutti m sono ptutti m sono squalche s è p"
correctsyntaxarray_figura3_modo2 = "nessun m è ptutti m sono snon tutti s sono p"
correctsyntaxarray_figura3_modo3 = "qualche m è ptutti m sono squalche s è p"
correctsyntaxarray_figura3_modo4 = "tutti m sono pqualche m è squalche s è p"
correctsyntaxarray_figura3_modo5 = "nessun m è pqulche m è snon tutti s sono p"
correctsyntaxarray_figura3_modo6 = "non tutti m sono ptutti m sono snon tutti s sono p"
 # quarta figura
correctsyntaxarray_figura4_modo1 = "tutti s sono mtutti m sono pqualche s è p"
correctsyntaxarray_figura4_modo2 = "tutti s sono mnessun m è pnessun s è p"
correctsyntaxarray_figura4_modo3 = "qualche s è mtutti m sono pqualche s è p"
correctsyntaxarray_figura4_modo4 = "nessun s è mtutti m è pnon tutti s sono p"
correctsyntaxarray_figura4_modo5 = "nessun s è mqualche m è pnon tutti s sono p"

sillogismocorretto = False
risposta = ""
def verificadelsillogismo():
  while sillogismocorretto==False:
    if sillogismo==correctsyntaxarray_figura1_modo1:
      print("Sillogismo corretto!")
      print("Figura: 1")
      print("Modo: 1")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura1_modo2:
      print("Sillogismo corretto!")
      print("Figura: 1")
      print("Modo: 2")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura1_modo3:
      print("Sillogismo corretto!")
      print("Figura: 1")
      print("Modo: 2")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura1_modo4:
      print("Sillogismo corretto!")
      print("Figura: 1")
      print("Modo: 4")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura2_modo1:
      print("Sillogismo corretto!")
      print("Figura: 2")
      print("Modo: 1")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura2_modo2:
      print("Sillogismo corretto!")
      print("Figura: 2")
      print("Modo: 2")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura2_modo3:
      print("Sillogismo corretto!")
      print("Figura: 2")
      print("Modo: 3")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura2_modo4:
      print("Sillogismo corretto!")
      print("Figura: 2")
      print("Modo: 4")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo1:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 1")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo2:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 2")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo3:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 3")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo4:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 4")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo5:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 5")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura3_modo6:
      print("Sillogismo corretto!")
      print("Figura: 3")
      print("Modo: 6")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura4_modo1:
      print("Sillogismo corretto!")
      print("Figura: 4")
      print("Modo: 1")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura4_modo2:
      print("Sillogismo corretto!")
      print("Figura: 4")
      print("Modo: 2")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura4_modo3:
      print("Sillogismo corretto!")
      print("Figura: 4")
      print("Modo: 3")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura4_modo4:
      print("Sillogismo corretto!")
      print("Figura: 4")
      print("Modo: 4")
      sillogismocorretto = True
    elif sillogismo==correctsyntaxarray_figura4_modo5:
      print("Sillogismo corretto!")
      print("Figura: 4")
      print("Modo: 5")
      sillogismocorretto = True
    else:
      risposta = str(input("Sillogismo errato! Riprovare? (si/no): "))
      if risposta=="si":
        sillogismocorretto = False
        print("faccio ripartire")
        verificadelsillogismo()
      elif risposta=="no":
        break
      else:
        while risposta!="si" or risposta!="no":
          risposta = str(input("Sillogismo errato! Riprovare? (si/no): "))

# chiamo la funzione
verificadelsillogismo()
