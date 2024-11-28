"""
Проверить, что число одновременно делится на 5 и на 3.
Если делится, то True; если не делится - то False
"""


class CheckNumber:

    def divided_on_fife_and_three(self, number):
        return number % 3 == 0 and number % 5 == 0


object_1 = CheckNumber()
result_of_divide = object_1.divided_on_fife_and_three(15)
print(result_of_divide)