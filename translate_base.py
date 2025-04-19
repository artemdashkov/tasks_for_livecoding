from googletrans import Translator # https://pypi.org/project/translators/
from datetime import datetime

# Создаем объект Translator
translator = Translator()
start = datetime.now()
print(f"start {start}")

with open('us_eng.txt', 'r', encoding='utf-8') as file:
    for x in file.readlines():
        en_line = x.strip()
        translated = translator.translate(en_line, src='en', dest='ru')
        ru_line = translated.text
        print(ru_line)

end = datetime.now()
print(f"start {end}")
print(f"total time: {end-start}")