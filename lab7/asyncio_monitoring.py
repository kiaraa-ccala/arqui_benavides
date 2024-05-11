# En base al programa asyncio_monitoring.py crear un programa que, 
# además de monitorear los recursos, pueda ser pausado y reanudado 
# en cualquier momento.
import asyncio
import psutil


async def monitorizar_recursos():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()

        print(f"Uso de CPU: {cpu_percent}% | Uso de Memoria: {mem_info.percent}%")

        await asyncio.sleep(1)

async def main():
    print("Monitorización de Recursos del Sistema")
    print("Presiona Ctrl+C para detener la monitorización.")
    await asyncio.sleep(3) 
    try:
        await monitorizar_recursos()
    except KeyboardInterrupt:
        print("Monitorización detenida.")

if __name__ == "__main__":
    asyncio.run(main())
