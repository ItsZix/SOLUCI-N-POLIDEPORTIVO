import data
import datetime as dt

db = data.data 
times = data.times

# Búsqueda de DNI
def search(dni):
  for user in db:
    if user['DNI'] == dni:
      print('DNI encontrado')
      return True
  return False   

# Valida formato de DNI  
def validate_dni(dni):
  if len(str(dni)) == 8:
    return search(dni)
  else:
    print('DNI inválido')
    return False

# Obtiene cancha reservada por el usuario
def reserved_gate(dni):
  for user in db:
    if user['DNI'] == dni:
      return user['gate']
  return 0  

# Verifica si tiene permiso de acceso
def has_permission(dni):
  for user in db:
    if user['DNI'] == dni:
      return True
  return False

# Obtiene fecha actual
def current_date():
  today = dt.date.today()
  return today.strftime("%d/%m/%Y")  

# Obtiene hora actual 
def current_time():
  now = dt.datetime.now()
  if now.hour > 12:
    return '{}:00pm'.format(now.hour-12)
  elif now.hour < 12:
    return '{}:00am'.format(now.hour)
  else:
    return '{}:00m'.format(now.hour)

# Verificando si la puerta está disponible  
def available_gate(day, time):

  for dated in times:
    if dated['day'] == day:
      
      for hour in dated['times']:
        if hour['time'] == time:
        
          for gate in hour['gates']:
            if gate['reserva'] == 0:
              return gate['gate']
  
  return 0 # no disponible

# Función principal
def dni_read(dni):

  print("Leyendo DNI...")
  
  if not validate_dni(dni):
    return [0,0] # DNI inválido  

  if not has_permission(dni):
    print("No tiene permiso")
    return [0,0] # No tiene permiso

  gate = reserved_gate(dni)
  if gate > 0:
    return [1, gate]  # Tiene reserva
  # No tiene reserva, revisa disponibilidad
  day = current_date()
  time = current_time()
  gate = available_gate(day, time)
  if gate > 0:
    return [1, gate] # Tiene cancha disponible
  else:
    return [0,0] # No hay cancha disponible

# Permite reservar al momento
def reservation_now():
  day = current_date()
  time = current_time()
  gate = available_gate(day, time)
  if gate > 0:
    print(f'Tiene una reserva de la cancha {gate} el día {day} a las {time}')
    return [gate, 1] # Reserva exitosa
  else:
    return [0,0] # No hay cancha disponible