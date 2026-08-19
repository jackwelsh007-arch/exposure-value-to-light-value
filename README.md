# Demystifying the APEX System: From Historical "Exposure Value" to Modern Light Value

> **Scope:** This framework and simulation strictly model the internal, automated in-camera metering software logic (output lightness) and are not a practical guide for raw exposure optimization (like ETTR).

This repository hosts a comprehensive article on the mathematical evolution of exposure settings.

## 📖 Use the interactive light meter simulation
To get an intuitive understanding of how the math works behind the scenes:

👉 **[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/photominion777/exposure-value-to-light-value/blob/main/Light_Meter_Simulation.ipynb)**

## 📖 Read the Full Article
The complete in-depth analysis, including all mathematical proofs, practical photographic implications, and the breakdown of linear f-stop components ($av, tv, sv$), is fully hosted in the project wiki:

👉 **[Click here to read the article in the GitHub Wiki](https://github.com/jackwelsh007-arch/exposure-value-to-light-value/wiki)**

---

### 🔍 Quick Theoretical Overview
* **The Historical Legacy:** Why the old $EV$ scale forces you to specify a fixed ISO, and how digital workflows turned ISO into a dynamic parameter.
* **The APEX Normalization:** Moving ISO speed to the camera's side of the equation to isolate ambient luminance ($L$) as the only true external variable.
* **The Additive Matrix:** How the subtractive formula $LV_{\text{cam}} = av - tv - sv$ allows instant manual exposure math across f-stops.

---

### 💻 Companion Code (Optional)

For those who want to see the mathematics in practice, a standalone command-line calculator is included in `main.py` to recreate a digital exposure compensation scale (\(\Delta LV\)).

#### 🚀 How to Run It Online Instantly
1. Download `main.py` from this repository to your computer.
2. Go to [Online Python](https://online-python.com).
3. Click the **"Open file from Disk"** folder icon, select your downloaded `main.py`, and click **"Run"**.

#### ⚠️ Note on Modifying Input Values Inside the Code
When customizing the fallback configuration inside the `main.py` file, you will find a dedicated entry box:

```python
DEFAULT_SHUTTER   = "1/125"  # Must remain a string in quotation marks!
```

* **Why the quotation marks?** If you type a fraction like `1/125` without quotes, Python will instantly divide the numbers mathematically and convert it into a decimal float (`0.008`) *before* the script even boots up. This will crash the terminal's text parser and break error reporting. Keeping it in quotes guarantees that the script handles fractional formatting properly.

