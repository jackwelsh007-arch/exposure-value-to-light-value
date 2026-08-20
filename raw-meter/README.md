# A Utopia for RAW Shooters: An Extension from Light Meters to Linear RAW Meters (ETTR)

**Scope:** Models an internal in-camera RAW-metering software logic based on linear sensor limits independently of standard JPEG rendering.

## 📖 Interactive Linear RAW Meter Simulation & Full Article

*   **Simulation:** [Open in Google Colab](INSERT_YOUR_COLAB_SHARE_LINK_HERE)
*   **Full Article:** [Read the GitHub Wiki](https://github.com/photominion777/exposure-value-to-light-value/wiki/A-Utopia-for-RAW-Shooters%3A-An-Extension-from-Light-Meters-to-Linear-RAW-Meters-%28ETTR%29)

### 🔍 Quick Theoretical Overview

*   **Additive RAW-APEX Transformation:** Converts the multiplicative physical chain into an additive log-2 system ($y_c = e_c - av + tv + sv_{\text{raw}}$).
*   **The ISO Gain Paradox Resolved:** Shows $y_{\text{sat}}$ is an absolute hardware constant while $sv_{\text{raw}}$ shifts the peak signal toward clipping.
*   **Decoupled Dual-Feedback Mechanism:** Separates static sensor limits from the dynamic user viewfinder override ($\Delta y_{\text{Display}} = \Delta y_{\text{ETTR}} - EC_{\text{user}}$).

### 💻 Companion Code

Run `raw-meter.py` locally:
```bash
python raw-meter.py
```

## 📄 License
Licensed under the **Proprietary Research License** (see [LICENSE](./LICENSE)).
