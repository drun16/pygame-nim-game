Here is your content rewritten and **properly formatted as a clean, professional `README.md`** using standard Markdown. I fixed heading levels, code blocks, spacing, and consistency, but **did not change your meaning or content**.

---

# 🎮 Pygame-Based Nim Game with AI Opponent

## 1. Introduction

This project implements a **two-row Nim game** using **Python and the Pygame library**, where a human player competes against an AI-controlled opponent.

**Nim** is a classic impartial combinatorial game with strong mathematical foundations. The objective is simple: players take turns removing objects from rows, and the player who removes the **final object wins**. Despite its simplicity, Nim demonstrates optimal play through mathematical reasoning using the **Nim-sum**.

This project demonstrates:

* Game loop design using Pygame
* Event-driven programming
* Implementation of game-theory-based AI
* Use of virtual environments for dependency management

---

## 2. Game Description and Rules

* The game consists of **two rows of balls**
* Players alternate turns
* On each turn, a player may remove **1–3 balls**
* Balls may be removed from a single row or split across rows, depending on the selected move
* The player who removes the **last remaining ball wins**
* The human player always takes the first turn

---

## 3. Nim-Sum Theory and AI Strategy

### 3.1 What Is Nim-Sum?

The **Nim-sum** is calculated using the **bitwise XOR (`^`)** operation on the number of remaining objects in each row.

**Example:**

```python
nim_sum = row_1_count ^ row_2_count
```

---

### 3.2 Game-Theoretic Interpretation

* **Nim-sum = 0**
  The current position is mathematically losing if the opponent plays optimally.

* **Nim-sum ≠ 0**
  The current player can force a winning outcome by making a move that reduces the Nim-sum to zero.

---

### 3.3 AI Decision Logic

* The AI calculates the Nim-sum on its turn
* If the Nim-sum is **non-zero**, the AI removes balls strategically to force a zero Nim-sum
* If the Nim-sum is **zero**, the AI performs a valid random move
* A timed delay is added to simulate realistic thinking behavior

This approach ensures **near-optimal play** by the AI.

---

## 4. Technologies Used

* Python 3
* Pygame
* Virtual Environment (`venv`)

---

## 5. Installation and Environment Setup

### 5.1 Install Python

Ensure **Python 3.9 or higher** is installed.

Check your Python version:

```bash
python --version
```

Download Python if required:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 5.2 Create and Activate a Virtual Environment (Recommended)

Using a virtual environment ensures project dependencies do not interfere with system-wide Python packages.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

When activated, your terminal prompt should show `(venv)`.

---

### 5.3 Install Dependencies

With the virtual environment activated:

```bash
pip install pygame
```

```bash
pip install random
```

(Optional) Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## 6. Project Setup and Execution

### 6.1 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pygame-nim-game.git
cd pygame-nim-game
```

---

### 6.2 Project Structure

```text
pygame-nim-game/
│
├── main.py
├── Nimaiball(7).png
├── README.md
└── venv/   (not tracked by Git)
```

⚠️ Ensure the image path in the code matches:

```python
pygame.image.load("Nimaiball(7).png")
```

---

### 6.3 Run the Application

```bash
python main.py
```

---

## 7. User Interaction

* Players interact via **on-screen buttons**
* Disabled buttons indicate **invalid moves**
* Turn indicators show whether it is the **Human** or **AI’s** turn
* The game ends automatically when no balls remain

---

## 8. End Condition

* The game concludes when **all balls are removed**
* The winner is displayed on screen
* No manual restart is required (can be added as an enhancement)

---

## 9. Potential Enhancements

* Restart and quit buttons
* Difficulty levels (suboptimal AI)
* Additional rows of balls
* Sound effects and animations
* Multiplayer mode

---

## 10. Academic Relevance

This project demonstrates:

* Practical application of game theory
* Event-driven programming
* AI decision-making using mathematical models
* Software structuring and dependency isolation using virtual environments

It is suitable for coursework in:

* Computer Science
* Game Development
* Artificial Intelligence
* Discrete Mathematics

---


---

## 11. License

This project is provided for **educational use**.
You are free to modify and extend it for learning and academic purposes.

---
