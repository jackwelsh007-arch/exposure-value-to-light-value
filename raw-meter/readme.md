# A Utopia for RAW Shooters: An Extension from Light Meters to Linear RAW Meters (ETTR)

**Scope:** This framework models a theoretical internal in-camera RAW-metering software logic based on linear sensor limits (ETTR Optimization) independently of standard JPEG rendering algorithms.

## 📖 Interactive Linear RAW Meter Simulation & Full Article

- **Simulation:** [Open the Interactive Simulation in Google Colab](INSERT_YOUR_COLAB_SHARE_LINK_HERE)
- **Full Article:** [Read the comprehensive analysis in the GitHub Wiki](../wiki/A-Utopia-for-RAW-Shooters:-Linear-RAW-Meters)

### 🔍 Quick Theoretical Overview
- **The Fixed Ceiling:** Tracks a constant digital saturation ceiling (\(y_{\text{sat}}\)) instead of shifting targets based on JPEG lightness.
- **Analog Gain Integration:** Shifts the sensor gain variable (\(sv_{\text{raw}}\)) to measure effective full-well capacity reduction.
- **The Decoupled Matrix:** Uses \(\Delta y_{\text{Display}} = \Delta y_{\text{ETTR}} - EC_{\text{user}}\) for viewfinder needle functionality while keeping data distribution static.

### 💻 Companion Code (Python Script Version)
Run `raw-meter.py` locally or via an online Python environment. Ensure `DEFAULT_SHUTTER` remains a string (e.g., `"1/125"`) for the stop-mapping parser.

```bash
python raw-meter.py
```

## 📄 License
Licensed under the terms of the **Proprietary Research License** (see [LICENSE](./LICENSE)).
