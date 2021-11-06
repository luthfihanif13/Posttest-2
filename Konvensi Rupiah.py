#Konvensi mata uang Rupiah

def idrtousd(rupiah):
    return(rupiah/15000)
def idrtosgd(rupiah):
    return(rupiah/10000)
def idrtoeur(rupiah):
    return(rupiah/20000)
def idrtojpy(rupiah):
    return(rupiah/5000)

uangrupiah = int(input("masukkan nominal rupiah : Rp"))
uangusd = idrtousd(uangrupiah)
uangsgd = idrtosgd(uangrupiah)
uangeur = idrtoeur(uangrupiah)
uangjpy = idrtojpy(uangrupiah)

print("Uang dollar saya sebesar: ",uangusd, "USD")
print("Uang dollar singapura saya sebesar: ",uangsgd, "SGD")
print("Uang euro saya sebesar: ",uangeur, "EUR")
print("Uang yen jepang saya sebesar: ",uangjpy, "JPY")

