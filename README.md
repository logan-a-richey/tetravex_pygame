# 🧩 Tetravex (Pygame)

## 📌 About

Tetravex is a logic-based puzzle game where you drag and drop numbered tiles into a grid so that adjacent edges match. This implementation is a fast, responsive desktop version built using Pygame, designed for flexibility and customization.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <your_repo_url>
cd tetravex
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Launch the game

```bash
./run_game.py <board_size>  # Example: ./run_game.py 4
```

### 4. Exit the game

* Press `ESC` or click the window close button.

---

## ✨ Features

* Procedural Tetravex puzzle generation
* Smooth tile click-and-drag with animated feedback
* Real-time validation overlay (red hologram for incorrect placements)
* End-game detection with victory message
* Responsive and intuitive user experience

---

## 🔍 Project Significance

* Personal passion project to bring a classic game to life with modern responsiveness
* Showcases event-driven programming, matrix manipulation, and custom animations
* Strong use of data structures, state management, and UI interaction logic
* Full-featured desktop puzzle experience built entirely with Python and Pygame

---

## 🛠 Planned Improvements

### 🎯 Optimizations

* [ ] Use `.blit()` exclusively for rendering (avoid `.draw()`)
* [ ] Pre-render all numbers/images and blit to screen surfaces

### 🎮 Scene Manager (Multi-screen UX)

* Title Screen: puzzle size, prefs, high scores, exit
* Level Select: 3x3, 4x4, 5x5, 6x6
* Gameplay
* Preferences
* High Score

### 🔊 Sound Effects

* [ ] Piece movement
* [ ] Piece snapping
* [ ] Error (wrong placement)
* [ ] Puzzle completion
* [ ] Menu interactions

### 💾 Persistence

* [ ] Save/load progress using local config or database
* [ ] Persist user preferences across sessions

### 🧠 Gameplay Features

* [ ] Reset button
* [ ] Hint button
* [ ] Undo/redo moves
* [ ] Row/column shift (right-click drag)
* [ ] Puzzle complete dialog popup
* [ ] Integrate C-based puzzle solver

---

## 🌐 Full Stack Roadmap

This project may evolve into a full-stack web application with:

* **Frontend:** React + Canvas API (game rendering)
* **Backend:** Python (Flask) + C integration for performance-critical logic
* **Features:** User profiles, scoreboards, mobile responsiveness, multiplayer (stretch goal)

---

## 💻 Contributing

- Please open an issue or submit a pull request. 
- Contributions and suggestions welcome.

---

## 📄 License

[MIT License](./LICENSE) — free for personal and commercial use.

