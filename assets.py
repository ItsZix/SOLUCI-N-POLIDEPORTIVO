import reads

num_gates =2  # Número de canchas
in_gate = 0  # Puerta inicialmente cerrada

def access():

  dni = input('Ingrese DNI: ')

  # Leemos DNI y obtenemos acceso y cancha
  access_data = reads.dni_read(dni)  

  if access_data == [0,0] and reads.search(dni)==False:
    print('DNI no está en base de datos')
    print('Ingrese uno válido')
    return access() # Reinicia proceso

  elif access_data == [0,0] and reads.search(dni)==True:
    action = input('Quiere reservar ahora? (s/n)')
    if action=='s':
      access_data = reads.reservation_now() # Hace reserva instantánea
      gate = access_data[0] 
      if gate == 0:
        print('No hay cancha disponible')
        return [0,0] # No abre nada
      else:
        print('Reservado')
        
    else: 
      print('Ha decidido que no va a reservar')
      print('Iniciando el programa ...')
      return access() # Reinicia proceso

  else:
    # Usuario con reserva, abre cancha correspondiente
    access_val = access_data[0]
    gate = access_data[1]
    if gate != 0:
      print(f'Abriendo cancha {gate}')

  return access_data # Devuelve datos para arduino

def save():
  print('Guardando datos')