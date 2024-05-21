"""cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
cand5 = 0
cand6 = 0
mayor = 0
candidatoGanador = ""

#documentos = []

for i in range(5):
    #documentos.append(input("Ingrese el documento: "))
    voto = int(input("Ingrese su voto 1, 2, 3, 4, 5, 6: "))
    if voto == 1:
        cand1 += 1
    if voto == 2:
        cand2 += 1
    if voto == 3:
        cand3 += 1
    if voto == 4:
        cand4 += 1
    if voto == 5:
        cand5 += 1
    if voto == 6:
        cand6 += 1

if(cand1 > cand2 and cand1 > cand3 and cand1 > cand4 and cand1 > cand5 and cand1 > cand6):
    mayor = cand1
    candidatoGanador = "Candidato 1"
elif(cand2 > cand1 and cand2 > cand3 and cand2 > cand4 and cand2 > cand5 and cand2 > cand6):
    mayor = cand2
    candidatoGanador = "Candidato 2"
elif(cand3 > cand1 and cand3 > cand2 and cand3 > cand4 and cand3 > cand5 and cand3 > cand6):
    mayor = cand3
    candidatoGanador = "Candidato 3"
elif(cand4 > cand1 and cand4 > cand2 and cand4 > cand3 and cand4 > cand5 and cand4 > cand6):
    mayor = cand4
    candidatoGanador = "Candidato 4"
elif(cand5 > cand1 and cand5 > cand2 and cand5 > cand3 and cand5 > cand4 and cand5 > cand6):
    mayor = cand5
    candidatoGanador = "Candidato 5"
elif(cand6 > cand1 and cand6 > cand2 and cand6 > cand3 and cand6 > cand4 and cand6 > cand5):
    mayor = cand5
    candidatoGanador = "Candidato 6"

print(f"\nEl que obtuvo mas votos fue {candidatoGanador} con {mayor} votos\n")

print(f"El candidato 1 tiene {cand1} votos")
print(f"El candidato 2 tiene {cand2} votos")
print(f"El candidato 3 tiene {cand3} votos")
print(f"El candidato 4 tiene {cand4} votos")
print(f"El candidato 5 tiene {cand5} votos")
print(f"El candidato 6 tiene {cand6} votos")

#print(f"Las personas que votaron fueron {documentos}")"""

cand1 = []
cand2 = []
cand3 = []
cand4 = []
cand5 = []
cand6 = []

for i in range(5):
    voto = int(input("Ingrese su voto 1, 2, 3, 4, 5, 6: "))
    if voto == 1:
        cand1.append(1)
    if voto == 2:
        cand2.append(1)
    if voto == 3:
        cand3.append(1)
    if voto == 4:
        cand4.append(1)
    if voto == 5:
        cand5.append(1)
    if voto == 6:
        cand6.append(1)

lista = [cand1, cand2, cand3, cand4, cand5, cand6]
lista.sort(reverse=True)

print(lista)
