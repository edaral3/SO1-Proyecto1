
texto = "aaaa.aaaa.a.a.a.a.a.a.a.a.a.56578dcf.er.f.erf.ertg.e.tr.etrger"
oraciones = texto.split(".")

autor = "Edgar Arnoldo"

for oracion in oraciones:
    json = {
        "autor":autor,
        "nota":oracion
    }
    print(json)