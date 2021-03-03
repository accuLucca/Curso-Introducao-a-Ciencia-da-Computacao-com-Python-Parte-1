segundos= input("Por favor, entre com o número de segundos que deseja converter: ")
totalSegundos=int(segundos)
dias=totalSegundos // 86400
segRestantesdia=totalSegundos % 86400
horas=segRestantesdia // 3600
segRestanteshora=segRestantesdia %3600
minutos = segRestanteshora // 60
segundosrestante= segRestanteshora % 60

print(dias,"dias,",horas,"horas, ",minutos,"minutos e ",segundosrestante, "segundos. ")