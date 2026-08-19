#!/usr/bin/env python3
import math
import argparse
import sys

def get_lighting_name(lv: float) -> str:
    ranges = [
        (19.5, 22.5, "Industrial Laser / Lab Light"),
        (18.5, 19.5, "Arc Welding / High-Power LED"),
        (17.0, 18.5, "Studio Flash / Searchlight"),
        (15.5, 17.0, "Extreme Sun (Snow/Sand)"),
        (14.5, 15.5, "Sunny"),
        (13.5, 14.5, "Hazy Sun"),
        (12.5, 13.5, "Bright Overcast"),
        (11.5, 12.5, "Overcast / Cloudy"),
        (10.5, 11.5, "Deep Shade"),
        (9.5, 10.5, "Sunset / Sunrise"),
        (8.5, 9.5, "Very Dynamic Twilight"),
        (7.5, 8.5, "Bright Street Lighting"),
        (6.5, 7.5, "Blue Hour / City Night"),
        (5.5, 6.5, "Bright Indoor"),
        (4.5, 5.5, "Standard Indoor"),
        (3.5, 4.5, "Living Room (Evening)"),
        (2.5, 3.5, "Dim Indoor"),
        (1.5, 2.5, "Distant Building Lights"),
        (0.5, 1.5, "Very Dim Interior"),
        (-0.5, 0.5, "Night Sky / City Skyline"),
        (-1.5, -0.5, "Dim Night Street"),
        (-2.5, -1.5, "Full Moon (Snow)"),
        (-3.5, -2.5, "Full Moon (Landscape)"),
        (-4.5, -3.5, "Quarter Moon"),
        (-5.5, -4.5, "Crescent Moon"),
        (-7.5, -5.5, "Starlight Night"),
    ]
    for low, high, name in ranges:
        if low <= lv < high:
            return name
    return "Transition / Mixed Light"

def calculate_and_display(L_input: float, N: float, t_str: str, S: float):
    try:
        if "/" in str(t_str):
            num, denom = map(float, t_str.split("/"))
            t = num / denom
        else:
            t = float(t_str)
    except ValueError:
        print(f"Error: Invalid shutter speed format '{t_str}'.", file=sys.stderr)
        return

    K = 12.5
    L = float(L_input)

    if L <= 0:
        print("Error: Luminance (L) must be greater than 0.", file=sys.stderr)
        return

    # Calculate light values
    av = math.log2(N**2)
    tv = math.log2(t)
    sv = math.log2(S / 100)
    LV_cam = av - tv - sv
    LV_ext = math.log2(L * (100 / K))
    delta_lv = LV_ext - LV_cam

    current_name = get_lighting_name(LV_ext)

    # Fixed scale alignment matrix
    scale_header = "    -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5"
    
    ticks_chars = []
    for idx in range(-15, 16):
        tick_val = idx / 3.0
        if abs(delta_lv - tick_val) < (1.0 / 6.0) and -5.1 < delta_lv < 5.1:
            ticks_chars.append("▲")
        elif idx % 3 == 0:
            ticks_chars.append("|")
        else:
            ticks_chars.append("·")

    prefix = "◀  " if delta_lv <= -5.1 else "   "
    suffix = "  ▶" if delta_lv >= 5.1 else "   "
    
    scale_visual = prefix + "   ".join(ticks_chars) + suffix

    output_text = f"""
===================================================================================================
[ INTERNAL DIGITAL LIGHT METER ANALYSIS ]
===================================================================================================
Calculated Physical Luminance (L)  :  {L:.2f} cd/m² ({current_name})
Camera Light Value (LV_cam)        :  {LV_cam:.2f}
Environmental Light Value (LV_ext) :  {LV_ext:.2f}
---------------------------------------------------------------------------------------------------
Δ LV Deviation (Viewfinder Indicator) : {delta_lv:+.2f} stops
---------------------------------------------------------------------------------------------------
{scale_header}
{scale_visual}
===================================================================================================
"""

    if abs(delta_lv) < 0.17:
        output_text += "✅ EXPOSURE BALANCE: Perfectly matched. Light values are optimal."
    elif delta_lv > 0:
        output_text += "⚠️ OVEREXPOSURE: Camera configuration requires adjustment for a brighter scene."
    else:
        output_text += "⚠️ UNDEREXPOSURE: Camera configuration requires adjustment for a darker scene."

    if LV_ext >= 18.5:
        output_text += "\n🔥 WARNING: High intensity light source. Prolonged exposure may damage the camera sensor."

    print(output_text)

def main():
    # =========================================================================
    #  [ PLEASE ENTER INPUT VALUES HERE ]
    #  Modify these default fallback values directly in the code if you run
    #  the script without passing terminal arguments (e.g., --iso 400).
    # =========================================================================
    DEFAULT_LUMINANCE = 4096.0   # Physical Luminance in cd/m²
    DEFAULT_APERTURE  = 2.8      # Aperture f-number (N)
    DEFAULT_SHUTTER   = "1/125"  # Shutter speed (t) as a string or fraction
    DEFAULT_ISO       = 400.0    # ISO speed rating (S)
    # =========================================================================

    parser = argparse.ArgumentParser(description="Digital Light Meter Simulator")
    parser.add_argument("-L", "--luminance", type=float, default=DEFAULT_LUMINANCE)
    parser.add_argument("-N", "--aperture", type=float, default=DEFAULT_APERTURE)
    parser.add_argument("-t", "--shutter", type=str, default=DEFAULT_SHUTTER)
    parser.add_argument("-S", "--iso", type=float, default=DEFAULT_ISO)

    args = parser.parse_args()
    calculate_and_display(L_input=args.luminance, N=args.aperture, t_str=args.shutter, S=args.iso)

if __name__ == "__main__":
    main()
