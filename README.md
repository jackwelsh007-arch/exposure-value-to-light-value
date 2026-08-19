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
For those who want to see the mathematics in practice, a small companion command-line calculator is included in `main.py` to recreate a digital exposure compensation scale ($\Delta LV$). Setup and execution details can be found directly in the code comments. Download main.py onto your computer and go to

👉 **[Online Python](https://www.online-python.com/)**

On that webpage, click on "Open file from Disk" symbol (a folder icon), choose the main.py from your pc and click run.
