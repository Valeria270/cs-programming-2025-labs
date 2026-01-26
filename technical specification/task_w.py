import json, datetime, os

FUEL_TYPES = ["АИ-92", "АИ-95", "АИ-98", "ДТ"]
FUEL_PRICES = {"АИ-92": 48.50, "АИ-95": 58.30, "АИ-98": 66.80, "ДТ": 56.20}
DATA_FILE = "azs_data.json"


class Cistern:
    def __init__(self, id, fuel_type, max_volume, current_volume, min_level=1000, is_active=True):
        self.id, self.fuel_type, self.max_volume, self.current_volume = id, fuel_type, max_volume, current_volume
        self.min_level, self.is_active, self.is_emergency_blocked = min_level, is_active, False

    def can_dispense(self, amount):
        return (self.is_active and not self.is_emergency_blocked and
                self.current_volume >= amount and self.current_volume - amount >= self.min_level)

    def dispense(self, amount):
        if self.can_dispense(amount):
            self.current_volume -= amount
            if self.current_volume < self.min_level:
                self.is_active = False
            return True
        return False

    def refuel(self, amount):
        if self.current_volume + amount <= self.max_volume:
            self.current_volume += amount
            return True
        return False

class Column:
    def __init__(self, column_id, pumps_config):
        self.column_id = column_id
        self.pumps = []
        for i, (fuel_type, cistern_id) in enumerate(pumps_config, 1):
            self.pumps.append(
                {"pump_id": f"P{column_id}-{i}", "fuel_type": fuel_type, "connected_cistern_id": cistern_id})

class AZSManager:
    def __init__(self):
        self.cisterns, self.columns, self.transactions, self.operations = {}, [], [], []
        self.statistics = {"total_cars": 0, "total_income": 0.0, "fuel_sold": {ft: 0.0 for ft in FUEL_TYPES},
                           "fuel_income": {ft: 0.0 for ft in FUEL_TYPES}}
        self.is_emergency, self.next_ids = False, {"transaction": 1, "operation": 1}
        self._init_data()
        self.load_data()

    def _init_data(self):
        cisterns_data = [("АИ-92 №1", "АИ-92", 20000, 12400), ("АИ-95 №1", "АИ-95", 20000, 9800),
                         ("АИ-95 №2", "АИ-95", 20000, 1200), ("АИ-98 №1", "АИ-98", 15000, 10000),
                         ("ДТ №1", "ДТ", 25000, 15600)]
        for cid, ft, mv, cv in cisterns_data:
            self.cisterns[cid] = Cistern(cid, ft, mv, cv, 500)
            if self.cisterns[cid].current_volume < 500:
                self.cisterns[cid].is_active = False

        column_config = {1: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №1")],
                         2: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №1")],
                         3: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №1"), ("АИ-98", "АИ-98 №1"), ("ДТ", "ДТ №1")],
                         4: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №1"), ("АИ-98", "АИ-98 №1")],
                         5: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №2"), ("АИ-98", "АИ-98 №1"), ("ДТ", "ДТ №1")],
                         6: [("АИ-92", "АИ-92 №1"), ("АИ-95", "АИ-95 №2"), ("АИ-98", "АИ-98 №1"), ("ДТ", "ДТ №1")],
                         7: [("АИ-95", "АИ-95 №2"), ("ДТ", "ДТ №1")], 8: [("АИ-95", "АИ-95 №2"), ("ДТ", "ДТ №1")]}
        for col_id, config in column_config.items():
            self.columns.append(Column(col_id, config))

    def save_data(self):
        data = {"cisterns": [{**c.__dict__} for c in self.cisterns.values()],
                "transactions": self.transactions, "operations": self.operations,
                "statistics": self.statistics, "is_emergency": self.is_emergency,
                "next_ids": self.next_ids}
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        if not os.path.exists(DATA_FILE): return
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.cisterns = {c['id']: Cistern(**c) for c in data.get("cisterns", [])}
        self.transactions, self.operations = data.get("transactions", []), data.get("operations", [])
        self.statistics, self.is_emergency = data.get("statistics", self.statistics), data.get("is_emergency", False)
        self.next_ids = data.get("next_ids", self.next_ids)

    def _add_op(self, op_type, details):
        self.operations.append(
            {"id": self.next_ids["operation"], "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "operation_type": op_type, "details": details})
        self.next_ids["operation"] += 1

    def serve_customer(self):
        if self.is_emergency: return print(" Аварийный режим!")
        print("\n=== ОБСЛУЖИВАНИЕ КЛИЕНТА ===")
        avail_cols = [c for c in self.columns if any(p["fuel_type"] in FUEL_TYPES for p in c.pumps)]
        if not avail_cols: return print("Нет доступных колонок")

        for i, col in enumerate(avail_cols, 1):
            print(f"{i}) Колонка {col.column_id}")
        try:
            col_choice = int(input("Выберите колонку: ")) - 1
            col = avail_cols[col_choice]

            avail_fuels = [p for p in col.pumps if self.cisterns[p["connected_cistern_id"]].is_active]
            for i, p in enumerate(avail_fuels, 1):
                print(f"{i}) {p['fuel_type']} ({FUEL_PRICES[p['fuel_type']]} ₽/л)")

            fuel_choice = int(input("Выберите топливо: ")) - 1
            pump = avail_fuels[fuel_choice]
            cistern = self.cisterns[pump["connected_cistern_id"]]

            liters = float(input(f"Литры (до {cistern.current_volume} л): "))
            if liters > cistern.current_volume: return print("Недостаточно топлива")

            total = liters * FUEL_PRICES[pump["fuel_type"]]
            print(f"{liters} л × {FUEL_PRICES[pump['fuel_type']]} ₽ = {total:.2f} ₽")

            if input("Подтвердить? (y/n): ").lower() == 'y':
                if cistern.dispense(liters):
                    self.transactions.append({"id": self.next_ids["transaction"],
                                              "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                              "column_id": col.column_id, "fuel_type": pump["fuel_type"],
                                              "liters": liters,
                                              "total_price": total, "cistern_id": cistern.id})
                    self.statistics["total_cars"] += 1
                    self.statistics["total_income"] += total
                    self.statistics["fuel_sold"][pump["fuel_type"]] += liters
                    self.statistics["fuel_income"][pump["fuel_type"]] += total
                    self.next_ids["transaction"] += 1
                    self._add_op("sale", f"Продажа {liters} л {pump['fuel_type']} за {total:.2f} ₽")
                    print("Успешно")
                else:
                    print("Ошибка")
        except:
            print("Ошибка ввода")
        input("Нажмите Enter...")

    def check_cisterns(self):
        print("\n=== СОСТОЯНИЕ ЦИСТЕРН ===")
        for c in self.cisterns.values():
            status = "ВКЛ" if c.is_active else "ВЫКЛ"
            if c.is_emergency_blocked: status = "БЛОК"
            print(f"{c.id} | {c.fuel_type} | {c.current_volume}/{c.max_volume} л | {status}")
        input("Нажмите Enter...")

    def refuel_cistern(self):
        if self.is_emergency: return print("Аварийный режим!")
        print("\n=== ПОПОЛНЕНИЕ ===")
        for i, ft in enumerate(FUEL_TYPES, 1):
            print(f"{i}) {ft}")
        try:
            fuel_choice = int(input("Выберите топливо: ")) - 1
            ft = FUEL_TYPES[fuel_choice]
            cisterns = [c for c in self.cisterns.values() if c.fuel_type == ft]
            for i, c in enumerate(cisterns, 1):
                print(f"{i}) {c.id}: {c.current_volume}/{c.max_volume} л")

            c_choice = int(input("Выберите цистерну: ")) - 1
            c = cisterns[c_choice]
            liters = float(input(f"Литры (макс {c.max_volume - c.current_volume}): "))

            if c.refuel(liters):
                self._add_op("refuel", f"Пополнение {c.id} на {liters} л")
                print("Успешно")
            else:
                print("Ошибка")
        except:
            print("Ошибка ввода")
        input("Нажмите Enter...")

    def show_stats(self):
        print("\n=== СТАТИСТИКА ===")
        print(f"Автомобилей: {self.statistics['total_cars']}")
        print(f"Доход: {self.statistics['total_income']:.2f} ₽")
        for ft in FUEL_TYPES:
            liters = self.statistics['fuel_sold'][ft]
            income = self.statistics['fuel_income'][ft]
            if liters > 0:
                print(f"{ft}: {liters:.1f} л, {income:.2f} ₽")
        input("Нажмите Enter...")

    def emergency_mode(self):
        print("\n АВАРИЙНЫЙ РЕЖИМ")
        confirm = input("АКТИВИРОВАТЬ? (y/n): ").lower()
        if confirm == 'y':
            self.is_emergency = True
            for c in self.cisterns.values():
                c.is_emergency_blocked = True
            self._add_op("emergency", "Активация аварийного режима")
            print(" Аварийный режим активирован")
        else:
            self.is_emergency = False
            for c in self.cisterns.values():
                c.is_emergency_blocked = False
            self._add_op("emergency", "Отключение аварийного режима")
            print(" Аварийный режим отключен")
        input("Нажмите Enter...")

def main():
    azs = AZSManager()
    while True:
        print("\n" + "=" * 50)
        print("АЗС УПРАВЛЕНИЕ")
        print("=" * 50)
        print("1) Обслужить клиента")
        print("2) Проверить цистерны")
        print("3) Пополнить цистерну")
        print("4) Статистика")
        print("9) Аварийный режим")
        print("0) Выход")

        try:
            choice = int(input("Выбор: "))
            if choice == 0:
                azs.save_data()
                break
            elif choice == 1:
                azs.serve_customer()
            elif choice == 2:
                azs.check_cisterns()
            elif choice == 3:
                azs.refuel_cistern()
            elif choice == 4:
                azs.show_stats()
            elif choice == 9:
                azs.emergency_mode()
        except:
            print("Ошибка")

if __name__ == "__main__":
    main()