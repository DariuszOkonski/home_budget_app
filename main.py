from views import MainMenu

class Application:
    @staticmethod
    def main():
        menu = MainMenu();
        menu.draw()

        screen = menu.get_screen()
        screen.set_repository('category', category_repository)
        screen.set_repository('entry', entry_repository)
        screen.draw()


if __name__ == "__main__":
    Application.main()