from machine import Pin
import utime

entrada = Pin(4, Pin.IN, Pin.PULL_UP)
cajero = Pin(13,  Pin.IN, Pin.PULL_UP)
salida = Pin(15,  Pin.IN, Pin.PULL_UP)

ledentrada = Pin(19,Pin.OUT)
ledcajero = Pin(5,Pin.OUT)
ledsalida = Pin(18,Pin.OUT)
lednopago = Pin(21,Pin.OUT)


while True:
    utime.sleep(1)
    datosentrada = entrada.value()
    datoscajero = cajero.value()
    datossalida = salida.value()
    #print(datosentrada)
    #print(datoscajero)
    #print(datossalida)
    
    if datosentrada == 0:
        ledentrada.value(1)
        print("Puede Entrar")
    else:
        ledentrada.value(0)
        
    if datoscajero == 0:
        ledcajero.value(1)
        #print("El Valor a Pagar Es:")
        # Este es el codigo del Cajero Automatico

# Variables de Descuento

        H1D = 60  # Descuento 1 Hora
        H2D = 120  # Descuento 2 Hora
        H3D = 180  # Descuento 3 Hora
        DBD = 30   # Descuento Banco
        LPD = 15   # Libre Paso
        H = 1850   # Valor Hora
        Min = 32   # Valor Minuto
        contador = 0 # contador

# Ingrear tiempo del vehiculo
        print("Ingresa el Tiempo del Vehiculo")
        Tiempo = input()
        Tiempo = int(Tiempo)

# Cobro

        Cobro = Tiempo * Min
        print(Cobro)
        
# Aplicacion del descuento 
        
        while True:
            if Tiempo <= LPD:
                Cobro = 0
                print("Valor a Cobrar")
                print(Cobro)
                break
            else:
                print("ingrese el descuento")
                print(" 0 = No hay Descuento\n 1 = Descuento 1 Hora\n 2 = Descuento 2 Horas\n 3 = Descuento 3 Horas\n 4 = Descuento Banco\n")
                
                Descuento = input()
                Descuento = int(Descuento)
                
            
            if Descuento == 0:
                print(Cobro)
                break
            
            elif Descuento == 1:
                Tiempo = Tiempo - H1D
                Cobro = Tiempo * Min
                if Cobro < 0:
                    Cobro = 0
                print("Valor a Cobrar")
                print(Cobro)
                break
            
            elif Descuento == 2:
                Tiempo = Tiempo - H2D
                Cobro = Tiempo * Min
                if Cobro < 0:
                    Cobro = 0
                print("Valor a Cobrar")
                print(Cobro)
                break
                
            elif Descuento == 3:
                Tiempo = Tiempo - H3D
                Cobro = Tiempo * Min
                if Cobro < 0:
                    Cobro = 0
                print("Valor a Cobrar")
                print(Cobro)
                break
            
            elif Descuento == 4:
                Tiempo = Tiempo - DBD
                Cobro = Tiempo * Min
                if Cobro < 0:
                    Cobro = 0
                print("Valor a Cobrar")
                print(Cobro)
                break
            
            else:
             print("no es un numero valido")
             contador = contador + 1
             
             if contador == 3:
                print("supero los intentos")
                break
# Pago

        pago = 0
        print(Cobro)
        print("ingrese una moneda o billete para realizar el pago")


        pago = input()
        pago = int(pago)
        Cobro = int(Cobro)
        Cobro = Cobro - pago
        
        while True:
          if Cobro <= 0:
            print("Su cambio es:")
            print(-Cobro)
            print("Puede Dirigirse a la salida")
            break


          elif Cobro == 0:
            print("Puede Dirigirse a la salida")
            break
  
          else:
            print("ingrese una moneda o billete para realizar el pago")
            print(Cobro)
            pago = input()
            pago = int(pago)
            Cobro = int(Cobro)
            Cobro = Cobro - pago
            
            if Cobro <= 0:
              print("Su Cambio es:")
              print(-Cobro)
              print("Puede Dirigirse a la salida")
              break
            else:
              print("Ingrese una Moneda o Billete Para Realizar el Pago")
              print(Cobro)
    ledcajero.value(0)
        
    if datossalida == 0:
        ledsalida.value(1)
        #if Cobro <=0:
        print("Puede Salir")
        #else
            #print("Devuelvase a la Caja")
            #break
    else:
        ledsalida.value(0)
        #lednopago.value(1)
        #utime.sleep(1)
        #print("Devuelvase para pagar")
        #lednopago.value(0)
        
    
   