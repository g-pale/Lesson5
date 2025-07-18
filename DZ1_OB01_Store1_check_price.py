class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаление товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получение цены товара. Если товара нет — вернуть None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара, если он есть в ассортименте."""
        if item_name in self.items:
            self.items[item_name] = new_price

    def display_info(self):
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")
        print("Ассортимент товаров:")
        if not self.items:
            print("  (Товары отсутствуют)")
        else:
            for item, price in self.items.items():
                print(f"  - {item}: {price:.2f} руб.")

# Пример использования:

# Создание магазина
my_store = Store("Фруктовый Рай", "ул. Садовая, 15")

# Добавление товаров
my_store.add_item("яблоки", 0.5)
my_store.add_item("бананы", 0.75)

# Получение цены
print(f'Стоимость яблок: {my_store.get_price("яблоки")}')  # 0.5
print(f'Стоимость апельсинов: {my_store.get_price("апельсины")}')  # None

# Вывод информации о магазине
# my_store.display_info()