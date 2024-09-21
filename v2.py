import random

# задание числа кандидатов
NumKandidats = random.randint(2, 10)
NameKandidats = ["Данил", "Кирилл", "Роман", "Иван", "Анжела", "Денис", "Никита", "Сергей", "Руслан", "Мария", "Дмитрий", "Павел", "Карина", "Вячеслав", "Роман", "Сергей"]
LastNameKandidats = ["Гаделия", "Варакин", "Кабирова", "Кит", "Олейник", "Никонов", "Погребняк", "Симон", "Федоров", "Шадчнев", "Панченко", "Бадрызлов", "Шляхтин"]
Kandidats = []

# создание списка всех подходящих кандидатов
for i in range(NumKandidats):
    name = random.choice(NameKandidats) + ' ' + random.choice(LastNameKandidats)
    if len(name) < 80:
        Kandidats.append(name)
    else:
        Kandidats.append(random.choice(NameKandidats) + ' ' + random.choice(LastNameKandidats))
Kandidats1 = list(set(Kandidats))

# создание бюллетеней избирателей с голосами для каждого кандидата
statements_list = []
for i in range(1, random.randint(2, 1000)):
    bulleten = list(range(1, NumKandidats + 1))
    random.shuffle(bulleten)
    statements_list.append(bulleten)

# присвоение нулевого рейтинга каждому из кандидатов перед подсчётом голосов
Kandidats_Rate = {k: 0 for k in Kandidats1}

# подсчёт голосов за каждого из кандидатов
for i in statements_list:
    score = NumKandidats
    for j in i:
        Kandidats_Rate[Kandidats1[j - 1]] += score
        score -= 1

# исключение кандидатов из предвыборной гонки в зависимости от их рейтинга
Rate_list = sum(Kandidats_Rate.values())

while max(Kandidats_Rate.values()) <= (Rate_list / 2):
    # если один из кндидатов набрал более половины голосов
    if max(Kandidats_Rate.values()) >= (Rate_list / 2):
        print(max(Kandidats_Rate, key=Kandidats_Rate.get))
    else:
        min_key = min(Kandidats_Rate, key=Kandidats_Rate.get)
        min_value = Kandidats_Rate[min_key]
        del Kandidats_Rate[min_key]
        Kandidats_Rate[min(Kandidats_Rate, key=Kandidats_Rate.get)] += min_value

print(max(Kandidats_Rate.keys()))