class Flower:
    def __init__(self, name, color, growing_place, blooming_season, lifespan, price):
        self.name = name
        self.color = color
        self.growing_place = growing_place
        self.blooming_season = blooming_season
        self.lifespan = lifespan
        self.price = price

    def __repr__(self):
        return f"{self.color} {self.name}"


class WildFlower(Flower):
    def __init__(self, name, color, growing_place, blooming_season, average_lifespan, price, petals):
        super().__init__(name, color, growing_place, blooming_season, average_lifespan, price)
        self.petals = petals


class GardenFlower(Flower):
    def __init__(self, name, color, growing_place, blooming_season, average_lifespan, price, bud):
        super().__init__(name, color, growing_place, blooming_season, average_lifespan, price)
        self.bud = bud


class HothouseFlower(Flower):
    def __init__(self, name, color, growing_place, blooming_season, average_lifespan, price, thorns):
        super().__init__(name, color, growing_place, blooming_season, average_lifespan, price)
        self.thorns = thorns


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.key = None
        self.found_flowers = []

    def collect_flowers(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def wilting_time(self):
        average_lifespan = sum((flower.lifespan for flower in self.flowers))
        return average_lifespan / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))
        self.key = key

    def find_flowers(self, key, param):
        self.found_flowers = []
        for flower in self.flowers:
            if getattr(flower, key) == param:
                self.found_flowers.append(flower)

    def __repr__(self):
        info = f"Букет содержит следующие цветы: " + ", ".join(repr(flower) for flower in self.flowers)
        info += f"\n Букет завянет через {self.wilting_time():.2f} дней"
        info += f"\n Полная стоимость букета: ${bouquet.total_cost()}"
        if self.key:
            info += f"\n Отсортировали по парамтру {self.key}: " + ", ".join(repr(flower) for flower in self.flowers)
        if self.found_flowers:
            info += f"\n Найденны цветы: " + ", ".join(repr(flower) for flower in self.found_flowers)
        return info



rose = HothouseFlower('poза', 'red', 'теплица', 'все сезоны', 10, 5, True)
lily = HothouseFlower('лилия', 'white', 'теплица', 'лето', 8, 10, False)
peony = GardenFlower('пион', 'rose', 'сад', 'осень', 12, 4, True)
chamomile = WildFlower('ромашка', 'white', 'поле', 'лето', 5, 1, True)
dandelion = WildFlower('одуванчик', 'yellow', 'поле', 'лето', 2,1, False)

bouquet = Bouquet()
bouquet.collect_flowers(rose)
bouquet.collect_flowers(lily)
bouquet.collect_flowers(peony)
bouquet.collect_flowers(chamomile)
bouquet.collect_flowers(dandelion)
# Пример сортировки по имени
bouquet.sort_flowers('name')
# Пример поиска по цвету
bouquet.find_flowers('color', 'white')

print(bouquet)
