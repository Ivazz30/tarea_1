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
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]

agenda_hospital.extend(persona)
for x in agenda_hospital:
    print "* Paciente: %s %s Ced: %d Edad: %d Num Poliza: %d Motivo: %s" % (x)

