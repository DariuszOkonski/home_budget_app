class AddCost:
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'


class ListCost:
    SHORTCUT = 'wk'
    LABEL = 'Wypisz koszty'


class AddIncome:
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychody'


class ListIncomes:
    SHORTCUT = 'wp'
    LABEL = 'Wypisz przychody'


class MainMenu:
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCost.SHORTCUT: ListCost(),
        AddIncome.SHORTCUT: AddIncome(),
        ListIncomes.SHORTCUT: ListIncomes()
    }

    def draw(self):
        print('Powiedz co chcesz zrobić?: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')

        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcję: ')

        print(MainMenu.OPTIONS[option])
