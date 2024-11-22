age = 18
def age_func(age):
    if age > 15:
        return "Это правда"
    else:
        return "Это ложь"

result = age_func(18)
print(result)

result_2 = "Это правда" if age > 15 else "Это ложь"

print(result_2)