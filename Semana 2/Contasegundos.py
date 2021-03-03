segundos= input("Por favor insira o total de segundos para converter: ")
totalSegundos=int(segundos)
horas= totalSegundos // 3600
segRestantes = totalSegundos % 3600
minutos = segRestantes // 60
segRestantes2= segRestantes % 60

print(horas,"horas, ",minutos,"minutos e ",segRestantes2, "segundos. ")