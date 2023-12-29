base_state = {
    'water': 400,
    'milk': 540,
    'beans': 120,
    'cups': 9,
    'money': 550
}

espresso = {
    'water': 250,
    'milk': 0,
    'beans': 16,
    'money': 4,
    'cups': 1
}
latte = {
    'water': 350,
    'milk': 75,
    'beans': 20,
    'money': 7,
    'cups': 1
}
cappuccino = {
    'water': 200,
    'milk': 100,
    'beans': 12,
    'money': 6,
    'cups': 1
}


def remaining():
    return f"""\nThe coffee machine has:
{base_state['water']} ml of water
{base_state['milk']} ml of milk
{base_state['beans']} g of coffee beans
{base_state['cups']} disposable cups
${base_state['money']} of money"""


def take():
    global base_state
    print(f"\nI gave you ${base_state['money']}")
    base_state['money'] = 0


def fill():
    global base_state
    base_state['water'] += int(input("\nWrite how many ml of water you want to add: \n"))
    base_state['milk'] += int(input("Write how many ml of milk you want to add: \n"))
    base_state['beans'] += int(input("Write how many grams of coffee beans you want to add: \n"))
    base_state['cups'] += int(input("Write how many disposable cups you want to add: \n"))


def buy(type_of_coffee):
    global base_state
    count = 0
    coffeeType = ''
    if int(type_of_coffee) == 1:
        coffeeType = espresso
    elif int(type_of_coffee) == 2:
        coffeeType = latte
    elif int(type_of_coffee) == 3:
        coffeeType = cappuccino

    for i in base_state:
        for x in coffeeType:
            if i == x:
                if base_state[i] < coffeeType[x]:
                    print(f"Sorry, not enough {i}!")
                    break
                else:
                    count += 1

    if count == 5:
        print("I have enough resources, making you a coffee!")
        base_state['water'] -= coffeeType['water']
        base_state['milk'] -= coffeeType['milk']
        base_state['beans'] -= coffeeType['beans']
        base_state['cups'] -= coffeeType['cups']
        base_state['money'] += coffeeType['money']


while True:
    action = input("\nWrite action (buy, fill, take, remaining, exit): \n")
    if action == "buy":
        type_ = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if type_ == 'back':
            continue
        else:
            buy(type_)
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print(remaining())
    elif action == "exit":
        break
