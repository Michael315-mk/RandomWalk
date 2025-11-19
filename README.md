# RandomWalk
> "The fruits of pseudo randomness." A generative art project simulating mathematical random walks using Python.

# 🎲 Random Walk Visualization

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Viz-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)

## 🖼️ Gallery

![Random Walk Demo](assets/outpu1.png)


## 📖 About the Project

This project explores the concept of **Random Walks** — a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps.

The goal was to create a script that not only generates the data points but visualizes the **chaos and order** within the movement. By mapping the order of point generation to a color gradient (using `cmap`), we can visualize the "time" dimension in a 2D static image.

### Key Features
* **Object-Oriented Design:** Logic encapsulated in a `RandomWalk` class.
* **Customizable:** Adjustable number of points and step directions.
* **Data Visualization:** Uses `matplotlib` with colormaps (e.g., `magma`, `plasma`, `viridis`) to show trajectory evolution.
* **Styling:** Implements `dark_background` for high-contrast aesthetics.

## 🛠️ How it Works

The algorithm starts at point `(0,0)`. For each step, it decides:
1.  **Direction:** Positive or Negative (X and Y).
2.  **Distance:** A random choice from a predefined list (e.g., 1 to 5).
3.  **Accumulation:** The new position is the sum of the previous position + the step.

This mimics **Brownian Motion** logic, creating organic, cloud-like structures.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Matplotlib

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Michael315-mk/random-walk-viz.git](https://github.com/Michael315-mk/random-walk-viz.git)
    ```
2.  Install dependencies:
    ```bash
    sudo apt install python3
    sudo apt install python3-matplotlib
    ```

### Usage

Run the main script to generate a new walk:

```bash
python3 rw_visual.py
