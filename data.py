# Cancha 0 significa no reservada

data = [
  {'DNI': '70398195', 'USER': 'Sofia Bobadilla', 'gate': 1, 'time': '9:00pm', 'day': '11/11/2023'},
  {'DNI': '70878875', 'USER': 'Jamil Casaverde', 'gate': 0}, 
  {'DNI': '70355221', 'USER': 'Ubaldo Olazabal', 'gate': 2, 'time': '8:00pm', 'day': '10/11/2023'}
]

times = [
  {'day': '10/11/2023', 
   'times': [{'time': '8:00pm', 'gates': [{'gate': 1, 'reserved': 0}, {'gate': 2, 'reserved': 1}]},
            {'time': '9:00pm', 'gates': [{'gate': 1, 'reserved': 0}, {'gate': 2, 'reserved': 1}]}]},
             
  {'day': '11/11/2023',
   'times': [{'time': '8:00pm', 'gates': [{'gate': 1, 'reserved': 1}, {'gate': 2, 'reserved': 0}]}, 
            {'time': '9:00pm', 'gates': [{'gate': 1, 'reserved': 1}, {'gate': 2, 'reserved': 0}]}]}
]