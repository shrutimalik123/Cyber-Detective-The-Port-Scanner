# 🖥️ Cyber-Detective: Port Scanner - Logic Sim

A deduction-based security simulation where you play as a network analyst identifying an open port on a secured server. By scanning specific ranges, you narrow down the location of the target port. This project simulates the tension of a system breach while teaching the fundamental principles of search algorithms and data validation.

This project focuses on teaching:
* **Binary Search Principles:** Strategy-based narrowing of data ranges to find a target efficiently.
* **Error Handling:** Using `try/except` blocks to prevent crashes from malformed user input.
* **Complex String Parsing:** Handling multiple input formats (ranges vs. integers) in a single field.
* **Conditional Range Checking:** Using comparison operators to determine if a value exists within a specific set.

---

## ✨ Features

* **Dual-Mode Scanning:** Switch between "Range Scans" (to narrow down the field) and "Direct Connection" attempts (to win the game).
* **Input Validation:** Built-in protection against non-numeric characters and formatting errors.
* **Tension Mechanics:** A limited "Firewall Lockdown" timer that creates a sense of urgency.
* **Dynamic Target Generation:** The target port is randomized every game, ensuring infinite replayability.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `port_scanner.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python port_scanner.py
    ```

### 3. Gameplay Instructions
1.  **Scan a Range:** Type `1-50` to see if the port is in the lower half of the network.
2.  **Analyze the Signal:** If a signal is found, scan a smaller range (e.g., `1-25`).
3.  **Breach the System:** Once you are confident, type the exact port number (e.g., `22`) to gain access.
4.  **Beat the Lockdown:** You only have 7 attempts before the Firewall resets.



---

## 🧠 Code Structure Highlights

### Robust Input Handling
This is the most "production-ready" part of the code. By using a `try` block, we ensure that if a user types something like "scan me" instead of "1-10", the game simply warns them instead of crashing.

```python
try:
    # Code that might fail (like converting string to int)
    guess = int(user_input)
except ValueError:
    # Code that runs if an error occurs
    print("Invalid input!")

