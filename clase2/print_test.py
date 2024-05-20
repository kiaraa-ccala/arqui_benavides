import time 

if __name__ == '__main__':
    inicio = time.perf_counter()
    print("Este es un print de prueba")
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin-inicio} segundos")

    N = 1024
    tic = time.perf_counter()
    for i in range(N):
        print("Este es un print{_} de prueba")
    toc = time.perf_counter()
    print(f"Tiempo de ejecucion {toc-tic} segundos")