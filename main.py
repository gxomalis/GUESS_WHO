import time

print("Εισαγωγή δεδομένων ατόμου! ")
total=0
while True:
  try:
    total=int(input("Πόσα άτομα θα εισάγεις; "))
    if total>0:
      break
    else:
      print("Δώσε θετικό ακέραιο...")

  except:
    print("Δώσε θετικό ακέραιο...")
onoma={x:0 for x in range(total)}
matia={x:0 for x in range(total)}
fagito={x:0 for x in range(total)}
tainia={x:0 for x in range(total)}
skoularikia={x:0 for x in range(total)}
gualia={x:0 for x in range(total)}
# νέο λεξικό εδώ


x=0
while x<total:
    print()
    print("|__________________________________________|")
    print()
    print("Εισαγωγή ατόμου νούμερο {}".format(x+1))
    joker=input("Δώσε όνομα: ")
    onoma[x]=joker

    joker = input("Δώσε χρώμα ματιών: ")
    matia[x]=joker

    joker = input("Δώσε αγαπημένο φαγητό: ")
    fagito[x]=joker

    joker = input("Δώσε τίτλο αγαπημένης ταινίας: ")
    tainia[x]=joker

    while True:
      joker = input("Έχεις σκουλαρίκια(NAI/OXI): ")
      if joker=="ΝΑΙ":
          break
      elif joker=="ΟΧΙ":
          break
      else:
          print("Δώσε ΝΑΙ ή ΟΧΙ...")
    skoularikia[x] = joker

    while True:
        joker = input("Γυαλιά φοράς;(NAI/OXI): ")
        if joker == "ΝΑΙ":
            break
        elif joker == "ΟΧΙ":
            break
        else:
            print("Δώσε ΝΑΙ ή ΟΧΙ...")
    gualia[x] = joker
#νέα ερώτηση και ανάθεση


    x += 1
print("|__________________________________________|")
print("Τώρα θα κάνω ερωτήσεις και θα μαντέψω ποιος τις απαντάει! ")
print("|__________________________________________|")
print()
endflag="ΝΑΙ"
while endflag=="ΝΑΙ":
    g_tainia=input("Ποια είναι η αγαπημένη σου ταινία; ")
    g_skoularikia=input("Φοράς σκουλαρίκια; ")
    g_matia=input("Τι χρώμα είναι τα μάτια σου; ")
    g_fagito=input("Ποιο είναι το αγαπημένο σου φαγητό; ")
    g_gualia=input("Φοράς γυαλιά; ")
  #νέα ερώτηση
    g_onoma=''
    flag=0
    for x in range(total):
        if matia[x]==g_matia:
            flag+=1

        if fagito[x]==g_fagito:
            flag+=1

        if tainia[x]==g_tainia:
            flag+=1

        if skoularikia[x]==g_skoularikia:
            flag+=1

        if gualia[x]==g_gualia:
            flag+=1

        if flag==5: #αλλάζω την τιμή της flag
            g_onoma=onoma[x]
            break
        flag = 0
    if flag==0:
        print("ωωωχ! Δεν κατάλαβα ποιος είσαι :(")
    else:
        print("Μαντεύω οτι είσαι ο/η {}! Το πέτυχα;;".format(g_onoma))
    time.sleep(2)
    endflag=input("Θες να συνεχίσεις και σε άλλες μαντεψιές; Γράψε ΝΑΙ ή ΟΧΙ: ")

