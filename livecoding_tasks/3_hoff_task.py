"""Пройти по списку и :
вывести в консоли full name (firstName + lastName)
посчитать и вывести в консоли итоговую зарплату
вывести имена, где в фамилия = Rose
посчитать и вывести количество уникальных фамилий
"""
users = [
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 200
    },
    {
        "firstName": "Margo",
        "lastName": "Rose",
        "gender": "male",
        "salary": 150
    },
    {
        "firstName": "Lisa",
        "lastName": "Barcley",
        "gender": "male",
        "salary": 1600
    },
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 2600
    },
]


# 1. вывести в консоли full name (firstName + lastName)
list_users = [f"{user["firstName"]} {user["lastName"]}" for user in users]
print(f"full name: \t{list_users}")
# 2. посчитать и вывести в консоли итоговую зарплату
list_of_salary = [user["salary"] for user in users]
total_salary = sum(list_of_salary)
print(f"Итоговая зарплата: \t{total_salary}")

# 3. вывести имена, где в фамилия = Rose
list_first_name = [user["firstName"] for user in users if user["lastName"] == "Rose"]
print(f"имена, где в фамилия = Rose: {list_first_name}")

# 4. посчитать и вывести количество уникальных фамилий
set_unique_lastname = {user["lastName"] for user in users}
print(set_unique_lastname)