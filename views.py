from abc import ABC, abstractmethod


class AbstractView(ABC):
    @abstractmethod
    def draw(self):
        pass


class AddCost(AbstractView):
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'

    def draw(self):
        print(AddCost.LABEL)


class ListCost(AbstractView):
    SHORTCUT = 'wk'
    LABEL = 'Wypisz koszty'

    def draw(self):
        print(ListCost.LABEL)


class AddIncome(AbstractView):
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychody'

    def draw(self):
        print(AddIncome.LABEL)


class ListIncomes(AbstractView):
    SHORTCUT = 'wp'
    LABEL = 'Wypisz przychody'

    def draw(self):
        print(ListIncomes.LABEL)


class MainMenu(AbstractView):
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCost.SHORTCUT: ListCost(),
        AddIncome.SHORTCUT: AddIncome(),
        ListIncomes.SHORTCUT: ListIncomes()
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcję: ')

        return MainMenu.OPTIONS[option]

    def draw(self):
        print('Powiedz co chcesz zrobić?: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')