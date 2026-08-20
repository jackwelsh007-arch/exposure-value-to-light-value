#!/usr/bin/env python3
"""
Digital Light Meter Simulator (Core Engine)
Converts human-readable camera values (rounded manufacturer steps) into mathematically 
exact 1/3 f-stop values internally for perfect APEX exposure calculations.
Uses a rock-solid, fixed monospace template layout for terminal safety.
"""

import math
import argparse
import sys

# Global option lists representing the standard manufacturer display values
N_OPTIONS = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.5, 2.8, 3.2, 3.5, 4.0, 4.5, 5.0, 5.6, 6.3, 7.1, 8.0, 9.0, 10, 11, 13, 14, 16, 18, 20, 22, 25, 29, 32]
T_OPTIONS = ["1", "1/1.3", "1/1.6", "1/2", "1/2.5", "1/3.2", "1/4", "1/5", "1/6", "1/8", "1/10", "1/13", "1/15", "1/20", "1/25", "1/30", "1/40", "1/50", "1/60", "1/80", "1/100", "1/125", "1/160", "1/200", "1/250", "1/320", "1/400", "1/500", "1/640", "1/800", "1/1000", "1/1250", "1/1600", "1/2000", "1/2500", "1/3200", "1/4000", "1/5000", "1/6400", "1/8000"]
S_OPTIONS = [100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 2500, 3200, 4000, 5000, 6400, 8000, 10000, 12800, 16000, 20000, 25600, 32000, 40000, 51200]

def get_lighting_name(lv: float) -> str:
    """Returns the descriptive environmental name based on the calculated Light Value."""
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
    # 1. MAP DISPLAY VALUES TO MATHEMATICALLY EXACT VALUES (1/3 STOPS)
    try:
        idx_N = N_OPTIONS.index(N)
        idx_t = T_OPTIONS.index(t_str)
        idx_S = S_OPTIONS.index(S)
    except ValueError as e:
        print(f"Error: Entered value is not in the standardized third-stop lists.\nDetails: {e}", file=sys.stderr)
        return

    # Aperture (N): Base f/1.0 is at index 3. Steps scale exactly by 2^(1/6)
    N_exact = 1.0 * (2**(1/6))**(idx_N - 3)
    
    # Shutter Speed (t): Base 1s is at index 0. Steps go to shorter times (2^(-1/3))
    t_exact = 1.0 * (2**(-1/3))**idx_t
    
    # ISO Speed (S): Base ISO 100 is at index 0. Steps scale by 2**(1/3)
    S_exact = 100.0 * (2**(1/3))**idx_S

    K = 12.5
    L = float(L_input)

    if L <= 0:
        print("Error: Luminance (L) must be greater than 0.", file=sys.stderr)
        return

    # 2. SYSTEM SEPARATION & APEX CALCULATIONS (Using exact values for flawless snapping)
    av = math.log2(N_exact**2)
    tv = math.log2(t_exact)
    sv = math.log2(S_exact / 100)
    LV_cam = av - tv - sv
    
    LV_ext = math.log2(L * (100 / K))
    delta_lv = LV_ext - LV_cam

    current_name = get_lighting_name(LV_ext)

    # 100% STATIC MONOSPACE TEMPLATE (From your original layout)
    scale_header = "<-5....-4....-3....-2....-1.....0....+1....+2....+3....+4....+5>"
    scale_ticks  = "  | . . | . . | . . | . . | . . | . . | . . | . . | . . | . . |  "
    
    # Calculate pointer position on the monospace layout
    if delta_lv <= -5.1:
        # Out of bounds left
        scale_pointer = "▲"
    elif delta_lv >= 5.1:
        # Out of bounds right
        scale_pointer = " " * (len(scale_ticks) - 3) + "▲"
    else:
        # Find closest third-stop tick slot (-15 to +15)
        closest_tick = round(delta_lv * 3)
        # Golden center (0) is exactly at index 32. Each third-stop deviates by 2 spaces.
        target_spaces = 32 + (closest_tick * 2)
        scale_pointer = " " * target_spaces + "▲"

    output_text = f"""
===================================================================================================
[ INTERNAL DIGITAL LIGHT METER ANALYSIS ]
===================================================================================================
Calculated Physical Luminance (L)  :  {L:.2f} cd/m² ({current_name})
Environmental Light Value (LV_ext) :  {LV_ext:.2f}
Camera Light Value (LV_cam)        :  {LV_cam:.2f}
---------------------------------------------------------------------------------------------------
Δ LV Deviation (Viewfinder Indicator) : {delta_lv:+.2f} stops
---------------------------------------------------------------------------------------------------
 {scale_header}
 {scale_ticks}
 {scale_pointer}
===================================================================================================
"""

    if abs(delta_lv) < 0.17:
        output_text += "✅ EXPOSURE BALANCE: Perfect match. Camera Light Value aligns with Environmental Light Value."
    elif delta_lv > 0:
        output_text += (
            "⚠️ OVEREXPOSURE: Camera configuration requires adjustment "
            "for a brighter scene."
        )
    else:
        output_text += (
            "⚠️ UNDEREXPOSURE: Camera configuration requires adjustment "
            "for a darker scene."
        )

    if LV_ext >= 18.5:
        output_text += (
            "\n🔥 WARNING: High intensity light source. "
            "Prolonged exposure may damage the camera sensor."
        )

    print(output_text)

def main():
    # =========================================================================
    #  [ PLEASE ENTER INPUT VALUES HERE ]
    # =========================================================================
    DEFAULT_LUMINANCE = 4096.0   # Physical Luminance in cd/m²
    DEFAULT_APERTURE  = 16.0     # Aperture f-number (N)
    DEFAULT_SHUTTER   = "1/125"  # Shutter speed (t) as a string or fraction
    DEFAULT_ISO       = 100.0    # ISO speed rating (S)
    # =========================================================================

    parser = argparse.ArgumentParser(description="Digital Light Meter Simulator")
    parser.add_argument("-L", "--luminance", type=float, default=DEFAULT_LUMINANCE)
    parser.add_argument("-N", "--aperture", type=float, default=DEFAULT_APERTURE)
    parser.add_argument("-t", "--shutter", type=str, default=DEFAULT_SHUTTER)
    parser.add_argument("-S", "--iso", type=float, default=DEFAULT_ISO)

    args = parser.parse_args()
    calculate_and_display(L_input=args.luminance, N=args.aperture,
                          t_str=args.shutter, S=args.iso)

if __name__ == "__main__":
    main()
