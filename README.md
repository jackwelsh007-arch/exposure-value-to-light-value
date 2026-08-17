# exposure-value-to-light-value

A utility explaining the transition from historical Exposure Value ($EV$) to modern Light Value ($LV$) using the APEX system.

## 🚀 Key Features
* Historical EV vs. Modern LV comparison
* Additive APEX Calculation ($av$, $tv$, $sv$)
* Exposure Balance Indicator ($\Delta LV$)
* Reciprocity Correction

---

## 📐 The Mathematics

### Variable Definitions
* **$N$**: Aperture | **$t$**: Shutter speed | **$S$**: ISO | **$L$**: Luminance | **$K$**: Constant ($12.5$)

### Formulas
* **$av = \log_2(N^2)$** | **$tv = \log_2(t)$** | **$sv = \log_2(S/100)$**
* **$LV_{\text{cam}} = av - tv - sv$** | **$\Delta LV = LV_{\text{ext}} - LV_{\text{cam}}$**

---

## 🛠️ Installation & Quick Start

```bash
git clone https://github.com
cd exposure-value-to-light-value
pip install -r requirements.txt
python main.py --aperture 1.4 --time 1 --iso 100 --luminance 350
```

---

## 🤝 Contributing
Contributions and issues are welcome!

