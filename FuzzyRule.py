# execution methods for a FuzzyClause that contains a FuzzyVariable; _variable and a FuzzySet; _set
from membership_functions import salinidad, temperatura, corrientes, altura_laminal, viscodidad, densidad,\
    profundidad, profundidad_colocacion, turbinas
from skfuzzy import control


#   optima -> todo verde
r1 = control.Rule((salinidad['Alta'] or salinidad['Media'] or salinidad['Baja']) and temperatura['Media']
                  and (corrientes['Muy Alta'] or corrientes['Alta']) and (altura_laminal['Muy Alta'] or altura_laminal['Alta'])
                  and (viscodidad['Alta'] or viscodidad['Media']) and (densidad['Alta'] or densidad['Media'])
                  and (profundidad['Alta'] or profundidad['Media']) and (profundidad_colocacion['Alta'] or profundidad_colocacion['Media']),
                  turbinas['Optima'])

#   descartada por (al menos 1) rojo
r2 = control.Rule((salinidad['Muy Alta'] or salinidad['Muy Baja']) or (temperatura['Muy Alta'] or temperatura['Muy Baja'])
                  or corrientes['Muy Baja'] or altura_laminal['Muy Baja'] or viscodidad['Muy Alta']
                  or (densidad['Muy Alta'] or densidad['Muy Baja']) or (profundidad['Muy Alta'] or profundidad['Muy Baja'])
                  or (profundidad_colocacion['Muy Alta'] or profundidad_colocacion['Muy Baja']),
                  turbinas['Descartada'])

#   descartada por (al menos 2) naranjas
r3 = control.Rule((corrientes['Baja'] and altura_laminal['Baja'] and viscodidad['Muy Baja'] and profundidad_colocacion['Baja']) or
                  (corrientes['Baja'] and altura_laminal['Baja'] or viscodidad['Muy Baja'] or profundidad_colocacion['Baja']) or
                  (corrientes['Baja'] or altura_laminal['Baja'] or viscodidad['Muy Baja'] and profundidad_colocacion['Baja']) or
                  (corrientes['Baja'] or altura_laminal['Baja'] and viscodidad['Muy Baja'] or profundidad_colocacion['Baja']),
                  turbinas['Descartada'])

#   no recomendable por 1 naranja
r4 = control.Rule((corrientes['Baja'] and ~altura_laminal['Baja'] and ~viscodidad['Muy Baja'] and ~profundidad_colocacion['Baja']) or
                  (~corrientes['Baja'] and altura_laminal['Baja'] and ~viscodidad['Muy Baja'] and ~profundidad_colocacion['Baja']) or
                  (~corrientes['Baja'] and ~altura_laminal['Baja'] and viscodidad['Muy Baja'] and ~profundidad_colocacion['Baja']) or
                  (~corrientes['Baja'] and ~altura_laminal['Baja'] and ~viscodidad['Muy Baja'] and profundidad_colocacion['Baja']) and
                  (~salinidad['Muy Baja'] and ~salinidad['Muy Alta'] and ~temperatura['Muy Baja'] and ~temperatura['Muy Alta'] and
                   ~densidad['Muy Baja'] and ~densidad['Muy Alta'] and ~profundidad['Muy Baja'] and ~profundidad['Muy Alta']),
                  turbinas['No Recomendable'])

#   no recomendable por 3 amarillos
r5 = control.Rule(((temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and altura_laminal['Media'] or
                  viscodidad['Baja'] or densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] or altura_laminal['Media'] and
                  viscodidad['Baja'] or densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] or altura_laminal['Media'] or
                  viscodidad['Baja'] and densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] or altura_laminal['Media'] or
                  viscodidad['Baja'] or densidad['Baja'] and profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] and altura_laminal['Media'] and
                  viscodidad['Baja'] or densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] and altura_laminal['Media'] or
                  viscodidad['Baja'] and densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] and altura_laminal['Media'] or
                  viscodidad['Baja'] or densidad['Baja'] and profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] or altura_laminal['Media'] and
                  viscodidad['Baja'] and densidad['Baja'] or profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] or altura_laminal['Media'] and
                  viscodidad['Baja'] or densidad['Baja'] and profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) or corrientes['Media'] or altura_laminal['Media'] or
                  viscodidad['Baja'] and densidad['Baja'] and profundidad['Baja']),
                  turbinas['Descartada'])

#   buena por 2 amarillos
r6 = control.Rule(((temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and densidad['Baja'] and ~profundidad['Baja']) or
                  ((temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and ~altura_laminal['Media']
                   and viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and altura_laminal['Media']
                   and viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and altura_laminal['Media']
                   and ~viscodidad['Baja'] and densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and altura_laminal['Media']
                   and ~viscodidad['Baja'] and ~densidad['Baja'] and profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and viscodidad['Baja'] and densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and viscodidad['Baja'] and ~densidad['Baja'] and profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media']
                   and ~viscodidad['Baja'] and densidad['Baja'] and profundidad['Baja']),
                  turbinas['Buena'])

#  muy buena por 1 amarillo
r7 = control.Rule(((temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media'] and not
                  viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and corrientes['Media'] and ~altura_laminal['Media'] and not
                  viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and altura_laminal['Media'] and not
                  viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media'] and
                  viscodidad['Baja'] and ~densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media'] and not
                  viscodidad['Baja'] and densidad['Baja'] and ~profundidad['Baja']) or
                  (~(temperatura['Alta'] or temperatura['Baja']) and ~corrientes['Media'] and ~altura_laminal['Media'] and not
                  viscodidad['Baja'] and ~densidad['Baja'] and profundidad['Baja']),
                  turbinas['Muy Buena'])


'''# contar num de naranjas
num_naranjas = 0
if corrientes['Baja']:
    num_naranjas += 1
if altura_laminal['Baja']:
    num_naranjas += 1
if viscodidad['Muy Baja']:
    num_naranjas += 1
if profundidad_colocacion['Baja']:
    num_naranjas += 1

# contar num de amarillos
num_amarillos = 0
if temperatura['Baja'] or temperatura['Alta']:
    num_amarillos += 1
if corrientes['Media']:
    num_amarillos += 1
if altura_laminal['Media']:
    num_amarillos += 1
if viscodidad['Baja']:
    num_amarillos += 1
if densidad['Baja']:
    num_amarillos += 1
if profundidad['Baja']:
    num_amarillos += 1

# No recomendable
r3 = control.Rule(num_naranjas >= 1 or num_amarillos >= 3,
                  turbinas['No recomendable'])

# Buena
r4 = control.Rule(num_naranjas == 0 and num_amarillos == 2,
                  turbinas['Buena'])

# Muy Buena
r4 = control.Rule(num_naranjas == 0 and num_amarillos == 1,
                  turbinas['Buena'])'''



