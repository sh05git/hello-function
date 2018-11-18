# テーブル毎に割り勘
# Table1：1500円で3人

amount1 = 1500
number_of_people1 = 3

print(f"1人あたり: {amount1 // number_of_people1}円, 端数: {amount1 % number_of_people1}円")

# Table2：2000円で3人
amount2 = 2000
number_of_people2 = 3

print(f"1人あたり: {amount2 // number_of_people2}円, 端数: {amount2 % number_of_people2}円")

# Table3：3647円で4人
amount3 = 3647
number_of_people3 = 4

print(f"1人あたり: {amount3 // number_of_people3}円, 端数: {amount3 % number_of_people3}円")

amount = 1500
number_of_people = 3

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")


# Table1: 1500円で3人
# Table2: 2000円で3人
# Table3: 3647円で4人


def warikan(amount, number_of_people):
    return amount // number_of_people, amount % number_of_people


result = warikan(amount, number_of_people)
print(f"1人あたり: {result[0]}円, 端数: {result[1]}円")
