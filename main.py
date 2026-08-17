import math
import argparse

def calculate_apex(aperture, shutter_speed, iso, luminance, k=12.5):
    # Berechnung der APEX-Werte (av, tv, sv) sowie Lichtwerte (LV_cam, LV_ext) und Belichtungsdifferenz (Delta LV)
    av = math.log2(aperture ** 2)
    tv = math.log2(shutter_speed)
    sv = math.log2(iso / 100)
    lv_cam = av - tv - sv
    l_nor = luminance * (100 / k)
    lv_ext = math.log2(l_nor) if l_nor > 0 else 0
    delta_lv = lv_ext - lv_cam
    return av, tv, sv, lv_cam, lv_ext, delta_lv

def draw_light_meter(delta_lv):
    # Generiert eine visuelle Belichtungsskala von -3 bis +3 Stufen
    meter_range = range(-3, 4)
    pointer_pos = round(delta_lv)
    scale_chars = ["▲" if x == pointer_pos else "┃" if x == 0 else "·" for x in meter_range]
    return f"-3 . -2 . -1 .  0 . +1 . +2 . +3\n" + "  ".join(scale_chars)

def main():
    parser = argparse.ArgumentParser(description="APEX Exposure & Light Value Calculator")
    parser.add_argument("--aperture", type=float, required=True)
    parser.add_argument("--time", type=float, required=True)
    parser.add_argument("--iso", type=float, required=True)
    parser.add_argument("--luminance", type=float, required=True)
    args = parser.parse_args()
    
    av, tv, sv, lv_cam, lv_ext, delta_lv = calculate_apex(args.aperture, args.time, args.iso, args.luminance)
    print(f"Delta LV: {delta_lv:+6.2f}")

if __name__ == "__main__":
    main()
