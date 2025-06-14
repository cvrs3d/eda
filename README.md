# 📊 Mean‑Variance‑Standard Deviation Calculator

Learn the fundamentals of **NumPy** through this project by calculating statistical measures on a 3×3 matrix.

---

## 🎯 Project Goal

Implement a function `calculate()` in **mean_var_std.py** that:

1. Expects a list of **9 numbers**.
2. Converts it into a **3×3 NumPy array**.
3. Returns a dictionary with these statistics:
   - **mean**, **variance**, **standard deviation**, **max**, **min**, **sum**
   - Calculated along:
     - **axis 0** (columns)
     - **axis 1** (rows)
     - The **flattened array**

Example usage:

```python
from mean_var_std import calculate

calculate([0,1,2,3,4,5,6,7,8])

