import assets

def main():
  print('main') 
  print('iniciando')
  
  # Llamamos a la función access en assets que gestiona el acceso
  access_data = assets.access()  
  
  # access_data contiene [access_val, gate]
  # access_val: 0 si no tiene acceso, 1 si tiene acceso
  # gate: 0 si no se abre nada, o el número de cancha si se abre
  
  # Enviamos el número de cancha a abrir al Arduino
  #send_to_arduino(access_data[1])

  # Guardamos datos
  assets.save()

if __name__=='__main__':
  main()