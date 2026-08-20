# A Utopia for RAW Shooters: An Extension from Light Meters to Linear RAW Meters (ETTR)

**Scope:** Dieses Framework und die Simulation modellieren streng eine theoretische interne In-Camera-RAW-Metering-Softwarelogik basierend auf linearen Sensorgrenzen (ETTR-Optimierung) und sind unabhängig von Standard-JPEG-Rendering-Algorithmen oder Mittelgrau-Zielen.

Dieses Verzeichnis hostet die technische Implementierung und den Begleitcode für die mathematische Evolution von Belichtungseinstellungen hin zu physikalischen Sensorgrenzen.

## 📖 Interaktive lineare RAW-Meter-Simulation

Um ein intuitives Verständnis der mathematischen Hintergründe zu erhalten:

👉 **[Interaktive Simulation in Google Colab öffnen](INSERT_YOUR_COLAB_SHARE_LINK_HERE)**

## 📖 Den vollständigen Artikel lesen

Die vollständige Tiefenanalyse inklusive aller mathematischen Beweise, unabhängiger Weißabgleichsanalysen und der Entkopplung von Sensorphysik und künstlerischem Benutzereinfluss ist vollständig im Wiki hinterlegt:

👉 **[Klicke hier, um den Artikel im GitHub Wiki zu lesen](../wiki/A-Utopia-for-RAW-Shooters:-Linear-RAW-Meters)**

### 🔍 Kurzer theoretischer Überblick

- **Die feste Obergrenze:** Warum ein echter RAW-Messer eine konstante digitale Sättigungsgrenze (\(y_{\text{sat}}\)) verfolgt, statt Ziele basierend auf einem JPEG-Bearbeitungsziel zu verschieben.
- **Die Integration der analogen Verstärkung:** Verschiebung der Sensorverstärkung (\(sv_{\text{raw}}\)) auf die Signalberechnungsseite, um die effektive Full-Well-Capacity-Reduktion direkt im Signalpfad zu messen.
- **Die entkoppelte Matrix:** Wie die Formel \(\Delta y_{\text{Display}} = \Delta y_{\text{ETTR}} - EC_{\text{user}}\) eine traditionelle Suchernadel ermöglicht, während die physikalische Datenverteilung des Histogramms statisch bleibt.

### 💻 Begleitender Code (Python-Skript-Version)

Wenn du ein leichtgewichtiges Python-Skript bevorzugst statt des interaktiven Notebooks, kannst du die Module (`raw_logic_part1.py` und `raw_ui_part2.py`) lokal oder online ausführen, um die Digitalkapazitätsauslastung einzusehen.

#### 🚀 Online ausführen

1. Lade `raw_logic_part1.py` und `raw_ui_part2.py` aus diesem Ordner herunter.
2. Gehe auf Online Python.
3. Lade beide Dateien über das Ordner-Icon hoch und führe sie aus.

#### ⚠ Hinweis zu Eingangswerten im Code

Du kannst die Standardparameter direkt im Konfigurationsblock der Skripte anpassen:

```python
# =========================================================================
# [ PLEASE ENTER INPUT VALUES HERE ]
# =========================================================================
DEFAULT_LUMINANCE = 4096.0  # Physical Luminance in cd/m²
DEFAULT_APERTURE = 16.0     # Aperture f-number (N)
DEFAULT_SHUTTER = "1/125"   # Shutter speed (t) as a string
DEFAULT_ISO = 100.0         # ISO speed rating (S)
DEFAULT_BIT_DEPTH = 14      # Sensor ADC Bit-Depth Resolution
# =========================================================================
```

- **Warum Anführungszeichen bei DEFAULT_SHUTTER?** Es muss ein String bleiben (`"1/125"`), da Python es sonst direkt als mathematischen Bruch auswertet und den internen Stop-Parser umgeht.

#### 🖥 Lokal via Terminal ausführen

Alternativ lassen sich die Module direkt über dein Terminal starten:

```bash
python raw_ui_part2.py
```

## 📄 Lizenz

Dieses Teilprojekt ist proprietär geschützt und lizenziert unter den Bedingungen der **Proprietary Research License**. Für die vollständigen akademischen oder kommerziellen Nutzungsbedingungen lies bitte die [LICENSE](./LICENSE) in diesem Verzeichnis.
