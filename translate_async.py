import asyncio  
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Пул потоков для выполнения синхронной функции в фоновом режиме
executor = ThreadPoolExecutor()

def sync_translate(text, target_language):
    result = GoogleTranslator(target=target_language).translate(text)
    return result

async def async_translate(text, target_language):
    loop = asyncio.get_event_loop()
    # Используем executor для выполнения синхронного вызова
    result = await loop.run_in_executor(executor, sync_translate, text, target_language)
    return result

async def main():
    start = datetime.now()
    print(f"start {start}")

    with open('us_eng.txt', 'r', encoding='utf-8') as file:
        texts = file.readlines()
        tasks = [async_translate(text, 'ru') for text in texts]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    end = datetime.now()
    print(f"start {end}")
    print(f"total time: {end-start}")


# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(main())