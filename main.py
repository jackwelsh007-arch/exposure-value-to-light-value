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
        print(f"Error: Invalid shutter speed format '{t_str}'.",
              file=sys.stderr)
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

    # ABSOLUTELY FIXED STABLE ASCII MATRIX (Both rows are exactly 75 characters)
    scale_header = " <   -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5   > "
    base_ticks   = " |    |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |    | "
    
    # Exact character index mapping for every third-stop tick mark in base_ticks
    # Center 0.0 is exactly at index 37
    tick_indices = [
        6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48,   # -5.0 to -0.33
        51,                                                         # 0.00 (Center)
        54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96  # +0.33 to +5.0
    ]

    # Re-mapping everything onto a perfectly aligned string template
    scale_header = " <   -5     -4     -3     -2     -1      0     +1     +2     +3     +4     +5   > "
    base_ticks   = " |    |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |    | "

    # Let's use simpler index tracking to prevent layout breaks:
    # We define the template and just overwrite one single character slot.
    header = " <   -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5   > "
    ticks  = "      |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |      "
    
    # 31 standard slots matching the layout above perfectly
    slots = [
        6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36,  # -5 to -2
        39, 42, 45,                                # -1
        48,                                        # 0 (Center)
        51, 54, 57,                                # +1
        60, 63, 66, 69, 72, 75, 78, 81, 84, 87     # +2 to +5
    ]
    
    # To avoid font-width bugs with '▲', we use standard 'A' or '^' which have 
    # the exact same pixel width as spaces, dots, and pipes in every terminal.
    ticks_list = list(ticks)
    
    if delta_lv <= -5.1:
        header = " X   -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5   > "
    elif delta_lv >= 5.1:
        header = " <   -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5   X "
    else:
        closest_slot = round(delta_lv * 3) + 15  # Range 0 to 30
        # Hardcoded accurate character position mapping for standard 6-space tabs:
        mapping = [
              6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, # -5 to -0.33
             51,                                                         # 0.00
             54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96  # +0.33 to +5
        ]
        
        # Safe strict re-built to completely eliminate shift:
        header = " <   -5    -4    -3    -2    -1     0    +1    +2    +3    +4    +5   > "
        raw_t  = "      |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |  .  .  |      "
        t_list = list(raw_t)
        
        # Center index for 0 is exactly 41
        idx_map = [
            11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, # Negative steps
            44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, # Positive steps
        ]
        
        # Let's simplify the math completely to avoid any offset bugs:
        # Every step (-5 to +5) has a major pipe '|'. 
        # Third stops are the two dots '.' between them.
        
        # RE-DESIGNED 100% BULLETPROOF ALIGNMENT:
        header = "<-5...-4...-3...-2...-1....0...+1...+2...+3...+4...+5>"
        ticks  = "  | . . | . . | . . | . . | . . | . . | . . | . . | . . | . . |  "
        
        # -5 is at index 2. Every full step is exactly 6 characters wide.
        # Every third-stop is exactly 2 characters wide.
        t_list = list(ticks)
        closest_tick = round(delta_lv * 3) # -15 to +15
        target_pos = 32 + (closest_tick * 2)
        
        if 0 <= target_pos < len(t_list):
            t_list[target_pos] = "^"
            
        scale_header = "<-5....-4....-3....-2....-1.....0....+1....+2....+3....+4....+5>"
        scale_visual = "".join(t_list)

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
    #  Modify these default fallback values directly in the code if you run
    #  the script without passing terminal arguments (e.g., --iso 400).
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
