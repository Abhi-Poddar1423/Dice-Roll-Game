# 🎲 Dice Roll Game (Modular Python Project)

A simple, interactive, and professional menu-driven Dice Roll game built with Python. This project demonstrates **Modular Programming**, **Error Handling**, and **ANSI Color integration** in a CLI environment.

## 🚀 Features
- **Modular Architecture:** Logic is separated from the main entry point.
- **User Interaction:** Allows the user to choose their lucky number (1-6).
- **Computer AI:** Computer rolls a random dice using the `random` module.
- **Error Handling:** Uses `try-except` blocks to prevent crashes on invalid inputs.
- **Colored UI:** Uses ANSI escape codes for a visually appealing terminal experience.

## 📂 Project Structure
```text
Dice-Roll-Game/
│
├── main.py            # Entry point (Menu & Loop logic)
├── Dice_engine.py      # Core Game Logic (Calculations & Comparisons)
└── README.md          # Project Documentation
🛠️ How to Run
Ensure you have Python 3.x installed.

Clone this repository or download the files.

Open your terminal in the project folder.

Run the following command:

Bash
python main.py
🧠 Logic Explained
The game follows a simple comparison logic:

If User Score > Computer Score -> User Wins!

If Computer Score > User Score -> Computer Wins!

If both are equal -> It's a Tie!

💻 Tech Stack
Language: Python 3

Modules: random

Environment: VS Code / Terminal


---

