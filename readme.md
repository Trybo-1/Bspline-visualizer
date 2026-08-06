# B-Spline Visualizer

A simple Python project that generates and visualizes a **2D B-Spline curve** from a set of control points using NumPy and Matplotlib.

The project was built as a learning exercise to understand the mathematics behind B-Splines before using them in more advanced applications such as **Kolmogorov-Arnold Networks (KANs)**.

---

## Features

* Generate a smooth B-Spline from a set of control points
* Modular implementation of B-Spline basis functions
* Visualize the resulting curve using Matplotlib
* Clean project structure separating mathematics from visualization

---

## Preview

> *(Screenshots coming soon.)*

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Trybo-1/Bspline-visualizer.git
cd Bspline-visualizer
```

Install the required dependencies:

```bash
pip install numpy matplotlib
```

Run the project:

```bash
python main.py
```

---

## Project Structure

```text
Bspline-visualizer/
│
├── bspline/
│   ├── basis.py        # B-Spline basis function implementation
│   └── spline.py       # B-Spline curve generation
│
├── visualization/
│   └── plot.py         # Matplotlib visualization
│
└── main.py             # Example usage
```

---

## How It Works

1. A set of 2D control points is defined in `main.py`.
2. A `BSpline` object is created from those control points.
3. The curve is sampled to produce points along the spline.
4. Matplotlib plots:

   * the control points
   * the generated B-Spline curve

The current example uses seven predefined control points to demonstrate the generated curve.

---

## Technologies

* Python
* NumPy
* Matplotlib

---

## Purpose

The goal of this project is to build an understanding of:

* B-Spline basis functions
* Parametric curve generation
* Scientific visualization in Python
* The mathematical concepts that underpin spline-based machine learning models

---

## Future Improvements

Possible future additions include:

* Interactive control point editing
* Adjustable spline degree
* Knot vector visualization
* Basis function plotting
* Real-time curve updates
* Exporting generated curves

---

## License

This project is available for educational purposes.

---

## Author

**Trybo-1**

If you found this project useful or interesting, consider giving it a ⭐.
