import csv

with open("TestForm.csv", "r", encoding="utf8") as file:
    # словарь из данных с файла
    reader = csv.DictReader(file)

    hobbys = []

    counter = []
    sum = 0

    #словарь: фильм/еда - кол-во выбора
    series = {}
    food = {}


    for row in reader:

        hobbys.append(row["Hobby"])

        # посчитать сумму оценок
        counter.append(row["Summer"])
        sum += int(row["Summer"])

    #счетчик выбора сериалов
        favorite = row["Series"] #favorite - название сериала из таблицы
        if favorite in series: series[favorite] += 1 #если такой сериал уже в словаре - добавить к кол-во раз +1
        else: series[favorite] = 1 #если сериал еще не в словаре - добавить его

        choose = row["Food"]
        if choose in food: food[choose] += 1
        else: food[choose] = 1


    #посчитать среднее арифметическое + вывод
    arMean = sum//len(counter)
    print(f"Средняя оценка лета 0-10: {arMean}! \n")

    #вывести количество выборов сериалов через перебор ключей
    for key in sorted(series, key=series.get, reverse=True):
        print(f"{key} выбрали - {series[key]} - раз")
    for key in sorted(food, key=food.get, reverse=True):
        print(f"\n{key} выбрали - {food[key]} - раз")

    print(f"Все собранные хобби: {hobbys}")