# exposure-value-to-light-value
A mathematically precise utility explaining the transition from the historical Exposure Value ($EV$) to the modern Light Value ($LV$). This project demonstrates how modern cameras utilize the APEX system for perfect exposure calculation and compensation.

## 🚀 Key Features

* **Historical EV vs. Modern LV:** Demonstrates how $LV$ normalizes exposure based on sensor sensitivity.
* **Additive APEX Calculation:** Splits exposure variables into additive f-stop components ($av$, $tv$, $sv$).
* **Exposure Balance Indicator:** Recreates the digital "Exposure Compensation Scale" ($\Delta LV$).
* **Reciprocity Correction:** Calculates alternative exposure combinations automatically.

---

## 📐 The Mathematics

### Variable Definitions
* **$N$**: Aperture (f-number)
* **$t$**: Shutter speed / exposure time (in seconds)
* **$S$**: Sensor sensitivity (ISO arithmetic speed)
* **$L$**: Ambient luminance (in $\text{cd/m}^2$)
* **$K$**: Standard calibration constant ($= 12.5 \ \text{cd}\cdot\text{s/m}^2$)

### 1. Component Definitions

* **Aperture Value ($av$):**
  $$av = \log_2(N^2)$$

* **Time Value ($tv$):**
  $$tv = \log_2(t)$$

* **Speed Value ($sv$):**
  $$sv = \log_2\left(\frac{S}{100}\right)$$

* **External Light Value ($LV_{\text{ext}}$):**
  $$LV_{\text{ext}} = \log_2\left(\frac{L \cdot 100}{K}\right)$$

### 2. Camera Light Value & Compensation

* **Camera Light Value ($LV_{\text{cam}}$):**
  $$LV_{\text{cam}} = av - tv - sv$$

* **Exposure Compensation ($\Delta LV$):**
  $$\Delta LV = LV_{\text{ext}} - LV_{\text{cam}}$$

---

## 🛠️ Installation & Quick Start

```bash
git clone https://github.com
cd exposure-value-to-light-value
pip install -r requirements.txt
python main.py --aperture 1.4 --time 1 --iso 100 --luminance 350
```

## 🤝 Contributing
Contributions and issues are welcome!
