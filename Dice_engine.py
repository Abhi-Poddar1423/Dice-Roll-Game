import random
import time

def roll_dice_game():
    # Colors defined inside or imported
    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    BLUE= "\033[94m"
    BOLD = "\033[1m"

    print(f"\n{CYAN}=============================={RESET}")
    print(f"{CYAN}🎲   DICE DUEL STARTING   🎲{RESET}")
    print(f"{CYAN}=============================={RESET}")

    try:
        user_score = int(input(f"\n{YELLOW}👉 Choose your lucky number (1-6): {RESET}"))

        if user_score < 1 or user_score > 6:
            print(f"{RED}[!] Error: Invalid dice score!{RESET}")
            return
    except ValueError:
        print(f"{RED}[!] Error: Please enter a number only.{RESET}")
        return

    print(f"\n{BLUE}🤖 Computer is rolling...{RESET}")
    time.sleep(1)
    
    computer_score = random.randint(1, 6)
    
    print(f"\n{BOLD}--- RESULTS ---{RESET}")
    print(f"👤 Your Roll:     {CYAN}{user_score}{RESET}")
    print(f"🤖 Computer Roll: {YELLOW}{computer_score}{RESET}")
    print("-" * 15)

    if user_score > computer_score:
        print(f"{GREEN}🏆 RESULT: YOU WIN!😍🎊{RESET}")
    elif computer_score > user_score:
        print(f"{RED}💀 RESULT: COMPUTER WINS!😂{RESET}")
    else:
        print(f"{YELLOW}🤝 RESULT: IT'S A TIE!{RESET}")