import time
if __name__ == '__main__':
    base_str = "*"

    print("[*] iniciando evaluacion de print")
    contenido = "iteracion, promedio, maximo, minimo, mediana\n"
    for idx in range (20):
    res = list()
        for i in range(200):
            full_str = base_str*(i+1)

            inicio = time.perf_counter()
            print(full_str)
            fin = time.perf_counter()

            print(f"Tiempo de ejecucion para {i+1} caracteres -> {fin-inicio} segundos")
            res.append(fin-inicio)
        promedio = sum(res) / len(res)
        maximo = max(res)
        minimo = min(res)
        res.sort()
        mediana = res[int(len(res)/2)]
        fila = f"{idx + 1},{promedio},{maximo},{minimo},{mediana}\n"
        contenido +=fila 
        print("[*] Pruebas terminadas procediendo a escribir en archivos")
    
        contenido = contenido [:-1]
    #sort() : ordena en forma ascendente


    #csv es un tipo de archivo que trata de modelar una table (filas con columnas)
    # saltos de linea 
