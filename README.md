# 🐍 Python Mini Projects

> A growing collection of small, hands-on Python projects built for learning, experimenting, and having fun with code — games, tools, and everyday utilities, all in one place.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## 📖 About

This repo is a sandbox for **mini, hands-on Python projects** — each one focused on practicing a different concept: OOP, file handling, APIs, GUIs, encryption, and more. Some are practical tools, some are just for fun. 🎯

---

## 📂 Projects Included

| # | Project | Description | Key Concepts |
|---|---------|-------------|---------------|
| 📧 | **[Email Validator](Email_validation.py)** | Checks whether an entered email follows basic formatting rules (length, `@` usage, dot position, no spaces/uppercase). | String methods, validation logic |
| ⏰ | **[Alarm Clock](Alarm_clock/Alarm_clock.py)** | A countdown-based alarm clock that plays a sound once time is up. | `time` module, terminal UI, audio playback |
| 🐍 | **[Snake Game](Snake_game.py)** | The classic Snake game — eat apples, grow longer, avoid the walls! | `pygame`, OOP, game loops |
| 💱 | **[Currency Converter](Currency_convetor.py)** | Converts a base currency into multiple others using live exchange rates. | REST APIs, `requests`, JSON parsing |
| 🎲 | **[Pig Dice Game](Pig_gem.py)** | A multiplayer dice game of risk and strategy — roll to score, but don't roll a 1! | Loops, game state, randomness |
| 🏧 | **[Basic ATM](Basic_ATM.py)** | Simulates ATM functionality: create/change PIN, check balance, withdraw cash. | OOP, class-based menus |
| 🔐 | **[Password Manager](password_mannager.py)** | Securely encrypts and stores account passwords using symmetric encryption. | `cryptography` (Fernet), file I/O |
| ⌨️ | **[Typing Test](Typing_test.py)** | A terminal-based WPM (words-per-minute) typing speed test with live feedback. | `curses`, real-time input handling |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/Python_Mini_project.git
cd Python_Mini_project
```

### 2. Install dependencies
Each project uses different libraries. Install what you need:
```bash
pip install pygame playsound requests cryptography windows-curses
```
> 💡 `windows-curses` is only needed if you're running the **Typing Test** on Windows.

### 3. Run any project
```bash
python <project_name>.py
```

---

## 🎮 How to Run Each Project

| Project | Command |
|---------|---------|
| Email Validator | `python Email_validation.py` |
| Alarm Clock | `python Alarm_clock/Alarm_clock.py` |
| Snake Game | `python Snake_game.py` |
| Currency Converter | `python Currency_convetor.py` |
| Pig Dice Game | `python Pig_gem.py` |
| Basic ATM | `python Basic_ATM.py` |
| Password Manager | `python password_mannager.py` |
| Typing Test | `python Typing_test.py` |

---

## 🧰 Tech Stack

- **Language:** Python 3
- **Libraries:** `pygame`, `playsound`, `requests`, `cryptography`, `curses`
- **Concepts practiced:** OOP, file handling, APIs, encryption, game development, terminal UIs

---

## 📌 Notes & Tips

- 🖼️ The **Snake Game** and **Alarm Clock** currently use hardcoded local file paths (`G:\Python_project\...`) — update these to match your own directory structure before running.
- 🔑 The **Password Manager** relies on a local `key.key` file for encryption. For real-world use, it's best practice to keep encryption keys and any files with saved credentials (like `key.key` and `password.txt`) **out of version control** — add them to `.gitignore` rather than committing them.
- 🌐 The **Currency Converter** uses a live API key directly in the code. If you fork this project, consider moving API keys into environment variables instead of hardcoding them.

---

## 🤝 Contributing

This is a personal learning repo, but suggestions, bug reports, and improvements are always welcome! Feel free to open an issue or submit a pull request. 🙌

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ☕, 🐍, and a lot of trial-and-error debugging.</p>
