# Demystifying the APEX System: From Historical "Exposure Value" to Modern Light Value

> **Scope:** This framework and simulation strictly model the internal, automated in-camera metering software logic (output lightness) and are not a practical guide for raw exposure optimization (like ETTR).

This repository hosts a comprehensive article on the mathematical evolution of exposure settings.

## 📖 Use the interactive light meter simulation
To get an intuitive understanding of how the math works behind the scenes:

👉 **[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/photominion777/exposure-value-to-light-value/blob/main/Light_Meter_Simulation.ipynb)**

## 📖 Read the Full Article
The complete in-depth analysis, including all mathematical proofs, practical photographic implications, and the breakdown of linear f-stop components ($av, tv, sv$), is fully hosted in the project wiki:

👉 **[Click here to read the article in the GitHub Wiki](https://github.com/jackwelsh007-arch/exposure-value-to-light-value/wiki](https://github.com/photominion777/exposure-value-to-light-value/wiki/Demystifying-the-APEX-System%3A-The-Transition-from-Exposure-Value-to-Modern-Light-Value)**

---

### 🔍 Quick Theoretical Overview
* **The Historical Legacy:** Why the old $EV$ scale forces you to specify a fixed ISO, and how digital workflows turned ISO into a dynamic parameter.
* **The APEX Normalization:** Moving ISO speed to the camera's side of the equation to isolate ambient luminance ($L$) as the only true external variable.
* **The Additive Matrix:** How the subtractive formula $LV_{\text{cam}} = av - tv - sv$ allows instant manual exposure math across f-stops.

---

### 💻 Companion Code (Python Script Version)

If you prefer a lightweight Python script instead of the full interactive notebook, you can run the code inside `main.py` directly in your browser using an online compiler to view the exposure compensation scale (Δ LV).

#### 🚀 How to Run It Online Instantly
1. Download `light-meter.py` from this repository to your computer.
2. Go to [Online Python](https://online-python.com).
3. Click the **"Open file from Disk"** folder icon, select your downloaded `light-meter.py`, and click **"Run"**. The output will appear instantly on the screen below the code.

#### ⚠ Note on Modifying Input Values Inside the Code

You can modify default parameters directly in the configuration block of the script:

```python
# =========================================================================
#  [ PLEASE ENTER INPUT VALUES HERE ]
# =========================================================================
DEFAULT_LUMINANCE = 4096.0   # Physical Luminance in cd/m²
DEFAULT_APERTURE  = 16.0     # Aperture f-number (N)
DEFAULT_SHUTTER   = "1/125"  # Shutter speed (t) as a string
DEFAULT_ISO       = 100.0    # ISO speed rating (S)
# =========================================================================
```

* **Why quotes on `DEFAULT_SHUTTER`?** It must remain a string (`"1/125"`). Without quotes, Python evaluates it as a float (`0.008`) and bypasses the internal stop-mapping parser.

#### 🖥️ Running Locally via Terminal (Advanced)
Alternatively, pass parameters via command-line flags:
```bash
python light-meter.py --luminance 4096 --aperture 16 --shutter 1/125 --iso 100
```

## 📄 License

This project is open-source and licensed under the terms of the **MIT License**. For full academic or commercial reuse terms, please refer to the project Wiki.

