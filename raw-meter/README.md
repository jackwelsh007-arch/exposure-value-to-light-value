# A Utopia for RAW Shooters: An Extension from Light Meters to Linear RAW Meters (ETTR)

**Scope:** Models an internal in-camera RAW-metering software logic based on linear sensor limits independently of standard JPEG rendering.

## 📖 Interactive Linear RAW Meter Simulation & Full Article

*   **Simulation:** [Open in Google Colab](https://colab.research.google.com/github/photominion777/exposure-value-to-light-value/blob/main/raw-meter/RAW_Meter_Simulation.ipynb)
*   **Full Article:** [Read the GitHub Wiki](https://github.com/photominion777/exposure-value-to-light-value/wiki/A-Utopia-for-RAW-Shooters%3A-An-Extension-from-Light-Meters-to-Linear-RAW-Meters-%28ETTR%29)

## 🔍 The Core Essence

> [!NOTE]
> **Key Takeaway:** A true RAW exposure meter computes the RAW signal deviation to measure the exact linear distance between the sensor's saturation limit and the peak signal of the brightest color channel.

* **Input-Driven Physics:** Evaluates raw data strictly at the sensor level based on physical capacity rather than arbitrary mid-gray outputs.
* **Effective Headroom Tracking:** Accounts for the fixed hardware saturation ceiling and how increased analog gain reduces effective headroom.
* **SNR Maximization:** Maximizes the signal-to-noise ratio while protecting highlights from clipping.
* **The Seamless Workflow:** Bridges hardware optimization and in-camera metering through an adjustable artistic bias.



### 💻 Companion Code

Run `raw-meter.py` locally:
```bash
python raw-meter.py
```

## 📄 License
Licensed under the **Proprietary Research License** (see [LICENSE](./LICENSE)).
