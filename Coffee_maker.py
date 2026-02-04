class CoffeeMachine:
    def __init__(self, brand, water_level=0, temperature=90, coffee_amount=0):
        self.brand = brand
        self.__water_level = water_level
        self.__temperature = temperature
        self.__coffee_amount = coffee_amount

    def brew(self):
        if self.__water_level >= 200 and self.__coffee_amount >= 10 and 85 <= self.__temperature <= 100:
            self.__water_level -= 200
            self.__coffee_amount -= 10
            print(f"{self.brand} brewed a cup of coffee.")
        else:
            print("Cannot brew: Check water level, coffee amount, or temperature.")

    def get_water_level(self):
        return self.__water_level

    def get_temperature(self):
        return self.__temperature

    def get_coffee_amount(self):
        return self.__coffee_amount

    def set_water_level(self, new_level):
        if new_level >= 0:
            self.__water_level = new_level
        else:
            print("Invalid water level. Must be non-negative.")

    def set_temperature(self, new_temp):
        if 60 <= new_temp <= 100:
            self.__temperature = new_temp
        else:
            print("Invalid temperature. Must be between 60°C and 100°C.")

    def set_coffee_amount(self, new_amount):
        if new_amount >= 0:
            self.__coffee_amount = new_amount
        else:
            print("Invalid coffee amount. Must be non-negative.")

    def display_details(self):
        print(f"Brand: {self.brand}, Water Level: {self.__water_level}ml, Temperature: {self.__temperature}°C, Coffee Amount: {self.__coffee_amount}g")

    def cups_available(self):
        cups_by_water = self.__water_level // 200
        cups_by_coffee = self.__coffee_amount // 10
        return min(cups_by_water, cups_by_coffee)

machines = [
    CoffeeMachine("BrewMaster", 500, 90, 20),
    CoffeeMachine("CaféPro", 300, 95, 15),
    CoffeeMachine("QuickCup", 250, 88, 10)
]

while True:
    print("\nSMART COFFEE MACHINE SYSTEM")
    print("1. Add Coffee Machine")
    print("2. View All Machines")
    print("3. Update Machine Settings")
    print("4. Delete Machine")
    print("5. Brew Coffee")
    print("6. Add Water")
    print("7. Add Coffee")
    print("8. How Many Coffees Can Be Brewed")
    print("9. Exit")

    choice = input("Choose an option (1-9): ").strip()

    if choice == "1":
        brand = input("Enter machine brand: ")
        water = int(input("Enter initial water level (ml): "))
        temp = int(input("Enter initial temperature (°C): "))
        coffee = int(input("Enter initial coffee amount (g): "))

        if water < 0 or temp < 0 or coffee < 0:
            print("Error: All values must be non-negative.")
        else:
            machine = CoffeeMachine(brand, water, temp, coffee)
            machines.append(machine)
            print(f"'{brand}' added to system.")

    elif choice == "2":
        print("\nMachine List:")
        if not machines:
            print("No machines available.")
        else:
            for i, machine in enumerate(machines, start=1):
                print(f"{i}. ", end="")
                machine.display_details()

            print("\nEncapsulation Test:")
            for machine in machines:
                try:
                    print(machine.__water_level)
                except AttributeError:
                    print(f"{machine.brand}: Cannot access __water_level directly (encapsulation works).")
                try:
                    print(machine.__coffee_amount)
                except AttributeError:
                    print(f"{machine.brand}: Cannot access __coffee_amount directly (encapsulation works).")
                try:
                    print(machine.__temperature)
                except AttributeError:
                    print(f"{machine.brand}: Cannot access __temperature directly (encapsulation works).")

                print(f"{machine.brand} - Water: {machine.get_water_level()}ml, Coffee: {machine.get_coffee_amount()}g, Temp: {machine.get_temperature()}°C")

    elif choice == "3":
        update_brand = input("Enter machine brand to update: ")
        found = False
        for machine in machines:
            if machine.brand.lower() == update_brand.lower():
                new_water = int(input("Enter new water level (ml): "))
                new_temp = int(input("Enter new temperature (°C): "))
                new_coffee = int(input("Enter new coffee amount (g): "))

                if new_water < 0 or new_temp < 0 or new_coffee < 0:
                    print("Error: All values must be non-negative.")
                else:
                    machine.set_water_level(new_water)
                    machine.set_temperature(new_temp)
                    machine.set_coffee_amount(new_coffee)
                    print(f"'{machine.brand}' updated.")
                found = True
                break
        if not found:
            print("Machine not found.")

    elif choice == "4":
        delete_brand = input("Enter machine brand to delete: ")
        for machine in machines:
            if machine.brand.lower() == delete_brand.lower():
                machines.remove(machine)
                print(f"'{delete_brand}' removed from system.")
                break
        else:
            print("Machine not found.")

    elif choice == "5":
        print("\nSelect a machine to brew:")
        for i, machine in enumerate(machines, start=1):
            print(f"{i}. {machine.brand}")
        index = int(input("Enter machine number: ")) - 1
        if 0 <= index < len(machines):
            machines[index].brew()
        else:
            print("Invalid selection.")

    elif choice == "6":
        brand = input("Enter machine brand to add water: ")
        for machine in machines:
            if machine.brand.lower() == brand.lower():
                amount = int(input("Enter water amount to add (ml): "))
                current = machine.get_water_level()
                machine.set_water_level(current + amount)
                print(f"{amount}ml water added to '{machine.brand}'.")
                break
        else:
            print("Machine not found.")

    elif choice == "7":
        brand = input("Enter machine brand to add coffee: ")
        for machine in machines:
            if machine.brand.lower() == brand.lower():
                amount = int(input("Enter coffee amount to add (g): "))
                current = machine.get_coffee_amount()
                machine.set_coffee_amount(current + amount)
                print(f"{amount}g coffee added to '{machine.brand}'.")
                break
        else:
            print("Machine not found.")

    elif choice == "8":
        print("\nAvailable Cups per Machine:")
        for machine in machines:
            cups = machine.cups_available()
            print(f"{machine.brand} can brew {cups} cup(s) of coffee.")

    elif choice == "9":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please select from 1 to 9.")