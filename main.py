import math
import argparse

def calculate_apex(aperture, shutter_speed, iso, luminance, k=12.5):
    # Mathematisch korrekte APEX-Komponenten nach deinem Fachartikel
    av = math.log2(aperture ** 2)
    tv = math.log2(1.0 / shutter_speed)  # log2(1/t) für korrekte Zeitwerte
    sv = math.log2(iso / 100)
    
    # Die Kamera-Belichtungsbalance (Subtraktiv basierend auf APEX-Richtlinien)
    lv_cam = av + tv - sv
    
    # Externer Lichtwert aus der Umgebungsluminanz
    l_nor = luminance * (100 / k)
    lv_ext = math.log2(l_nor) if l_nor > 0 else 0
    
    # Abweichung (Belichtungswaage)
    delta_lv = lv_ext - lv_cam
    return av, tv, sv, lv_cam, lv_ext, delta_lv

def draw_light_meter(delta_lv):
    # Generiert eine visuelle Belichtungsskala von -3 bis +3 Stufen
    meter_range = range(-3, 4)
    pointer_pos = round(delta_lv)
    
    # Begrenzt den Zeiger auf die Skala, falls der Wert extrem ist
    pointer_pos = max(-3, min(3, pointer_pos))
    
    scale_chars = ["▲" if x == pointer_pos else "┃" if x == 0 else "·" for x in meter_range]
    labels = "-3 . -2 . -1 .  0 . +1 . +2 . +3"
    return f"{labels}\n" + "  ".join(scale_chars)

def main():
    parser = argparse.ArgumentParser(description="APEX Exposure & Light Value Calculator")
    parser.add_argument("--aperture", type=float, required=True, help="Aperture f-number (N)")
    parser.add_argument("--time", type=float, required=True, help="Shutter speed in seconds (t)")
    parser.add_argument("--iso", type=float, required=True, help="Sensor sensitivity (S)")
    parser.add_argument("--luminance", type=float, required=True, help="Ambient luminance in cd/m² (L)")
    args = parser.parse_args()
    
    av, tv, sv, lv_cam, lv_ext, delta_lv = calculate_apex(
        args.aperture, args.time, args.iso, args.luminance
    )
    
    # Ausgabe eines professionellen Berichts im Terminal
    print("\n" + "="*45)
    print("      APEX LIGHT VALUE CALCULATOR REPORT      ")
    print("="*45)
    print(f" INPUTS: N=f/{args.aperture} | t={args.time}s | ISO={args.iso} | L={args.luminance} cd/m²")
    print("-"*45)
    print(f" Aperture Value (av) : {av:6.2f} (f-stops)")
    print(f" Time Value (tv)     : {tv:6.2f} (f-stops)")
    print(f" Speed Value (sv)    : {sv:6.2f} (f-stops)")
    print("-"*45)
    print(f" Camera Light Value  (LV_cam): {lv_cam:6.2f}")
    print(f" External Light Value (LV_ext): {lv_ext:6.2f}")
    print(f" Exposure Deviation   (ΔLV)   : {delta_lv:+6.2f} f-stops")
    print("="*45)
    print(" DIGITAL EXPOSURE METER SCALE:")
    print(draw_light_meter(delta_lv))
    print("="*45)
    
    if abs(delta_lv) < 0.25:
        print(" Status: Mathematically Optimal Exposure! 🎉")
    elif delta_lv > 0:
        print(f" Status: OVEREXPOSED! Reduce system by {abs(delta_lv):.1f} stops.")
    else:
        print(f" Status: UNDEREXPOSED! Increase system by {abs(delta_lv):.1f} stops.")
    print("="*45 + "\n")

if __name__ == "__main__":
    main()
