if __name__ == '__main__': 
    a = 1
    b = '2'
#    c = a + b 
#    print(f"El resultado de la operacion es {c}")

    #saldria error ya que estamos operando un int + str, por lo que python no lo soporta
    # para arreglar esto usaremos try para atrapar el error 
    try : 
        c = a+b
        print(f"El resultado de la operacion es {c}")    
    except TypeError:
        print("ocurrio un error")
        if not isinstance(a, int):
            a = int(a)

        if not isinstance(b , int):
            b = int(b)

        c = a + b
    finally: 
        print(f"El resultado de la operacion es {c}")