# En base al programa asyncio_monitoring.py crear un programa que, 
# además de monitorear los recursos, pueda ser pausado y reanudado 
# en cualquier momento.
import asyncio
import psutil


async def monitorizar_recursos():
    while True:
        if not switch:
            cpu_percent = psutil.cpu_percent(interval=1)
            mem_info = psutil.virtual_memory()

            print(f"Uso de CPU: {cpu_percent}% | Uso de Memoria: {mem_info.percent}%")

            await asyncio.sleep(1)


async def main():
    print("Monitorización de Recursos del Sistema")
    print("Presiona Ctrl+C para detener la monitorización.")
    try:
        await asyncio.gather(monitorizar_recursos(),pausar_reanudar())
    except KeyboardInterrupt:
        print("Monitorización detenida.")


switch = False # boton para pausar el programa, se inicializa en falso
async def pausar_reanudar():
    global switch 
    print("\n-- Pulsar 'k' + Enter para pausar o reanudar--") #ya que la entrada bloquea al bucle principal se hace uso de el comando to_thread, el cual redirige la entrada del usuario a otro hilo, 
    # esto es muy util porque mas abajo se hará uso de funciones sincronas como print
    while True:
        pasos = await asyncio.to_thread(input)
        if pasos=='k':
            if switch: 
                switch = False
                print('Reanudado')
            else:
                switch = True
                print('\n Pausado')
            print("\n-- Presionar 'k' + Enter para pausar o reanudar--")
        
if __name__ == "__main__":
    asyncio.run(main())
