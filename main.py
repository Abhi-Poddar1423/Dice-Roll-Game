from Dice_engine import roll_dice_game

def main():

    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"

    while True:
        print(f"\n{MAGENTA}╔═════════════════════════╗{RESET}")
        print(f"{MAGENTA}║      DICE ARENA HUB     ║ {RESET}")
        print(f"{MAGENTA}╚═════════════════════════╝{RESET}")
        print(f" {CYAN}[1]{RESET} Enter Battle")
        print(f" {CYAN}[2]{RESET} Quit Game")
        
        choice = input(f"\n{RESET}Selection > ").strip()

        if choice == '1':
            roll_dice_game()
        elif choice == '2':
            print(f"\n{MAGENTA}Goodbye! Thanks You for playing. 👋{RESET}\n")
            break
        else:
            print(f"\033[31m⚠️  Invalid Choice! Try again.{RESET}")

if __name__ == "__main__":
    main()