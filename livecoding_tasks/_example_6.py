import matplotlib.pyplot as plt

# Данные
models = ['BART-base', 'T5-base', 'GPT-2 medium']
scores = [0.726, 0.714, 0.692]
colors = ['#4A90E2', '#50E3C2', '#F5A623']  # более приятные и разнообразные цвета

# Построение графика
plt.bar(models, scores, color=colors)
plt.xlabel('Модель')
plt.ylabel('BERTScore')
plt.title('Сравнение моделей по BERTScore')
plt.ylim(0, 1)  # диапазон 0-1 для метрики
plt.show()