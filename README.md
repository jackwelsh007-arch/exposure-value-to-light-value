# Demystifying the APEX System: From Historical "Exposure Value" to Modern Light Value

This repository hosts a comprehensive article on the mathematical evolution of exposure settings in photography, exposing the historical legacy of the traditional Exposure Value ($EV$) and showcasing why modern digital sensors rely on Light Values ($LV$).

## 📖 Use the interactive light meter simulation
To get an intuitive understanding of how the math works behind the scenes:

👉 **[![Open In Colab](https://github.com/photominion777/exposure-value-to-light-value/blob/main/Light_Meter_Simulation.ipynb)]([https://google.com](https://colab.research.google.com/))**

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
For those who want to see the mathematics in practice, a small companion command-line calculator is included in `main.py` to recreate a digital exposure compensation scale ($\Delta LV$). Setup and execution details can be found directly in the code comments.
