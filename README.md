# ❌⭕ Tic-Tac-Toe – Human vs Computer (Decision Tree)

## 📌 Overview
This project implements a **Human vs Computer Tic-Tac-Toe game** powered by a **Decision Tree model**.

Unlike traditional rule-based implementations, the AI is trained using an existing dataset that already contains the **best possible move** for each board state. The work in this project focuses on **training a model** and using it to play against a human player.

---

## 🧠 Approach
1. A pre-existing dataset (`tictac_single.txt`) contains board states with the corresponding optimal move.
2. A Decision Tree model is trained on this data to learn the best move selection strategy.
3. During gameplay, the trained model:
   - Evaluates the current board state
   - Predicts the best possible move
4. A human player competes against the AI in a full Tic-Tac-Toe game.

---

## 🌳 Why Decision Tree?
A Decision Tree model was chosen for this project because:

- Tic-Tac-Toe has a **small and discrete state space**, making it well-suited for tree-based models.
- Decision Trees can **directly model game rules and conditional logic** without requiring complex feature engineering.
- The model is **interpretable**, allowing easy inspection of how board states map to move decisions.
- Training and inference are **fast**, making it practical for real-time gameplay.
- The dataset already contains optimal moves, aligning well with **supervised classification**.

---

## 📂 Files in This Repository

- **`tictac_single.txt`**  
  Dataset containing board states and their corresponding best moves.

- **`DT_Tic_Tac_Train.ipynb`**  
  Jupyter Notebook used to train the Decision Tree model on the Tic-Tac-Toe dataset.

- **`DT_Tic_Tac_Toe_Class.py`**  
  Python implementation of the Decision Tree model used for move prediction.

- **`DT_Tic_Tac_Toe_HvsC.py`**  
  Python implementation of the Human vs AI Tic-Tac-Toe game.

---

## 🎯 Key Outcome
This project demonstrates how a **Decision Tree model**, trained on an optimal-move dataset, can be used to build an effective and interpretable AI opponent for a classic game.
