class CoffeeMachine:
    # default status of coffee machine
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.action()

    # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
    def buy_espresso(self):
        # global water, coffee_beans, cups, money
        if CoffeeMachine.water >= 250 and CoffeeMachine.coffee_beans >= 16 and CoffeeMachine.cups >= 1:
            CoffeeMachine.water -= 250
            CoffeeMachine.coffee_beans -= 16
            CoffeeMachine.cups -= 1
            CoffeeMachine.money += 4
            print('I have enough resources, making you a coffee!')
        elif CoffeeMachine.water < 250:
            print('Sorry, not enough water!')
        elif CoffeeMachine.coffee_beans < 16:
            print('Sorry, not enough coffee beans!')
        elif CoffeeMachine.cups < 1:
            print('Sorry, not enough disposable cups!')
        print()
        self.action()

    # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    def buy_latte(self):
        # global water, coffee_beans, milk, cups, money
        if CoffeeMachine.water >= 350 and CoffeeMachine.milk >= 75 and CoffeeMachine.coffee_beans >= 20 \
                and CoffeeMachine.cups >= 1:
            CoffeeMachine.water -= 350
            CoffeeMachine.milk -= 75
            CoffeeMachine.coffee_beans -= 20
            CoffeeMachine.cups -= 1
            CoffeeMachine.money += 7
            print('I have enough resources, making you a coffee!')
        elif CoffeeMachine.water < 350:
            print('Sorry, not enough water!')
        elif CoffeeMachine.milk < 75:
            print('Sorry, not enough milk!')
        elif CoffeeMachine.coffee_beans < 20:
            print('Sorry, not enough coffee beans!')
        elif CoffeeMachine.cups < 1:
            print('Sorry, not enough disposable cups!')
        print()
        self.action()

    # For a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
    def buy_cappuccino(self):
        # global water, coffee_beans, milk, cups, money
        if CoffeeMachine.water >= 200 and CoffeeMachine.milk >= 100 and CoffeeMachine.coffee_beans >= 12 \
                and CoffeeMachine.cups >= 1:
            CoffeeMachine.water -= 200
            CoffeeMachine.milk -= 100
            CoffeeMachine.coffee_beans -= 12
            CoffeeMachine.cups -= 1
            CoffeeMachine.money += 6
            print('I have enough resources, making you a coffee!')
        elif CoffeeMachine.water < 200:
            print('Sorry, not enough water!')
        elif CoffeeMachine.milk < 100:
            print('Sorry, not enough milk!')
        elif CoffeeMachine.coffee_beans < 12:
            print('Sorry, not enough coffee beans!')
        elif CoffeeMachine.cups < 1:
            print('Sorry, not enough disposable cups!')
        print()
        self.action()

    def buy_coffee(self):
        back = 'back'
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        input_buy_coffee = input()
        if input_buy_coffee.lower() == back:
            self.action()
        elif int(input_buy_coffee) == 1:
            self.buy_espresso()
        elif int(input_buy_coffee) == 2:
            self.buy_latte()
        elif int(input_buy_coffee) == 3:
            self.buy_cappuccino()

    def fill_machine(self):
        # global water, milk, coffee_beans, cups
        print()
        print('Write how many ml of water you want to add:')
        water_input = int(input())
        CoffeeMachine.water += water_input
        print('Write how many ml of milk you want to add:')
        milk_input = int(input())
        CoffeeMachine.milk += milk_input
        print('Write how many grams of coffee beans you want to add:')
        coffee_input = int(input())
        CoffeeMachine.coffee_beans += coffee_input
        print('Write how many disposable cups you want to add:')
        cups_input = int(input())
        CoffeeMachine.cups += cups_input
        print()
        self.action()

    def take_out_money(self):
        # global money
        print(f'''
    I gave you ${CoffeeMachine.money}
    ''')
        CoffeeMachine.money = 0
        self.action()

    def print_status(self):
        print(f'''
    The coffee machine has:
    {CoffeeMachine.water} ml of water
    {CoffeeMachine.milk} ml of milk
    {CoffeeMachine.coffee_beans} g of coffee beans
    {CoffeeMachine.cups} disposable cups
    ${CoffeeMachine.money} of money
    ''')
        self.action()

    def action(self):
        # operations
        buy = "buy"
        fill = "fill"
        take = "take"
        remaining = "remaining"
        input_exit = "exit"

        print('Write action (buy, fill, take, remaining, exit):')
        user_input_action = input()

        if user_input_action.lower() == buy:
            self.buy_coffee()
        elif user_input_action.lower() == fill:
            self.fill_machine()
        elif user_input_action.lower() == take:
            self.take_out_money()
        elif user_input_action.lower() == remaining:
            self.print_status()
        elif user_input_action.lower() == input_exit:
            exit()


CoffeeMachine()
