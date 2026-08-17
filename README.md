# exposure-value-to-light-value
A calculator explaining the transition from historical Exposure Value (EV) to modern Light Value (LV) using logarithmic APEX components.

### 1. Component & Environment Value Definitions
* **Aperture Value ($av$):** Derived from the f-number ($N$).
  $$av = \log_2(N^2)$$
* **Time Value ($tv$):** Derived from the exposure time ($t$) in seconds.
  $$tv = \log_2(t)$$
* **Speed Value ($sv$):** Derived from the sensor sensitivity ($S$, ISO).
  $$sv = \log_2\left(\frac{S}{100}\right)$$
* **External Light Value ($LV_{\text{ext}}$):** Derived from ambient luminance ($L$ in $\text{cd/m}^2$) and standard calibration constant ($K = 12.5$ in $\text{cd\cdot s/m}^2$).
  $$LV_{\text{ext}} = \log_2\left(\frac{L \cdot 100}{K}\right)$$

### 2. Camera Light Value ($LV_{\text{cam}}$)
The overall camera light value decomposes additively into the three f-stop components:
$$LV_{\text{cam}} = av - tv - sv$$

### 3. Exposure Compensation ($\Delta LV$)
The light meter measures the external ambient light value ($LV_{\text{ext}}$) and compares it with the current camera settings ($LV_{\text{cam}}$) to show the deviation:
$$\Delta LV = LV_{\text{ext}} - LV_{\text{cam}}$$
