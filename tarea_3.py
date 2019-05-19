from operator import itemgetter
# Ejercicio atencion en un hospital

# Agenda del hospital

agenda_hospital = []

# Entra 1 persona:

persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')

# Agregamos 1 persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
# print(agenda_hospital)

print "Paciente %s %s Ced: %d Edad: %d Num Poliza: %d Motivo: %s" % (persona)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')

# agregamos otra persona
agenda_hospital.append(persona)
#print agenda_hospital

#for x in agenda_hospital:
 #   print "Paciente %s %s Ced: %d Edad: %d Num Poliza: %d Motivo: %s" % (x)

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36, 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15, 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42, 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10, 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 02,  99313131, 'dolor')
          ]

agenda_hospital.extend(persona)
for x in agenda_hospital:
    print "* Paciente: %s %s Ced: %d Edad: %d Num Poliza: %d Motivo: %s" % (x)

# Pregunta 1. Cuantos pacientes llegaron en total?

print "Llegaron ",len(agenda_hospital)," personas en total"

# Pregunta 2. Cuantos llegaron por dolor?

cont_dol = 0
for d in agenda_hospital:
    if "dolor" in d:
        cont_dol +=1

print "Llegaron ",cont_dol," pacientes por dolor"

# Pregunta 3. Ordene los pacientes de mayor edad a menor edad.

# sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])
# print sorted([agenda_hospital], key=lambda x: x[3])
# sorted(agenda_hospital, key = itemgetter(3), reverse = True)

print "\nLos pacientes en orden de edad de mayor a menor: "
for x in sorted(agenda_hospital, key = itemgetter(3), reverse = True):
    print "* Paciente: %s %s Ced: %d Edad: %d Num Poliza: %d Motivo: %s" % (x)

# Pregunta 4. Cuantos pacientes son mayores de edad y cuantos menores.

mayor_edad = 0
menor_edad = 0
for x in agenda_hospital:
    if x[3] > 18:
        mayor_edad += 1
    else:
        menor_edad += 1
print "\n Hay %d pacientes mayores de edad y %d pacientes menores de edad" % (mayor_edad, menor_edad)

# Pregunta 5. Ordenar primero por dolor y luego por edad de Mayor a Menor

for x in agenda_hospital:
    if x[5] == 'dolor':
        print "Los pacientes que tienen dolor seran atendidos primero: ", x
for x in sorted(agenda_hospital, key = itemgetter(3), reverse = True):
    if x[5] != 'dolor':
        print x

# Pregunta 6. Se mueren los que tienen dolor.

for x in agenda_hospital:
    if x[5] != 'dolor':
        print x


