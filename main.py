#!/usr/bin/env python3
"""
Demystifying the APEX System: Companion Command-Line Calculator
Models the automated in-camera metering software logic (Δ LV deviation).
"""

import math

def calculate_delta_lv(L, N, t, S):
    """
    Computes the deviation between environmental light and camera configuration.
    L: Physical Luminance in cd/m²
    N: Aperture (f-number)
    t: Shutter Speed in seconds (float)
    S: ISO Speed
    """
    K = 12.5

    # SYSTEM SEPARATION
    # Left side: Camera settings (APEX logarithmic components)
    av = math.log2(N**2)
    tv = math.log2(t)
    sv = math.log2(S / 100)
    LV_cam = av - tv - sv

    # Right side: Environment (Physical luminance normalized to ISO 100 baseline)
    LV_ext = math.log2(L * (100 / K))
    
    # Deviation scale
    delta_lv = LV_ext - LV_cam
    return LV_cam, LV_ext, delta_lv

def render_terminal_meter(delta_lv):
    # EXACT COURIER/MONOSPACE ALIGNMENT MATRIX (95 characters wide)
    scale_header = " -5       -4       -3       -2       -1        0       +1       +2       +3       +4       +5 "

    scale_ticks = []
    for index in range(-15, 16):
        tick_value = index / 3.0

        if abs(delta_lv - tick_value) < (1.0 / 6.0) and -5.1 < delta_lv < 5.1:
            scale_ticks.append("▲")
        elif index % 3 == 0:
            scale_ticks.append("|")
        else:
            scale_ticks.append("·")

    prefix = "◀ " if delta_lv < -5.1 else "  "
    suffix = " ▶" if delta_lv > 5.1 else "  "
    scale_visual = prefix + "  ".join(scale_ticks) + suffix

    print(scale_header)
    print(scale_visual)

def main():
    print("===============================================================================================")
    print("[ INTERNAL DIGITAL LIGHT METER ANALYSIS ]")
    print("===============================================================================================")
    
    # Standard demo scenario (Matches your Colab initial states)
    L = 128.0      # Scene Luminance (cd/m²)
    N = 2.8        # Aperture
    t = 1 / 125.0  # Shutter speed (using exact mathematical fraction)
    S = 400        # ISO
    
    LV_cam, LV_ext, delta_lv = calculate_delta_lv(L, N, t, S)
    
    print(f"Calculated Physical Luminance (L)  :  {L:.2f} cd/m²")
    print(f"Camera Light Value (LV_cam)        :  {LV_cam:.2f}")
    print(f"Environmental Light Value (LV_ext) :  {LV_ext:.2f}") 
    print("-----------------------------------------------------------------------------------------------")
    print(f"Δ LV Deviation (Viewfinder Indicator) : {delta_lv:+.2f} stops")
    print("-----------------------------------------------------------------------------------------------")
    
    render_terminal_meter(delta_lv)
    print("===============================================================================================")

    # Your original, corrected exposure logic
    if abs(delta_lv) < 0.17:
        print("✅ EXPOSURE BALANCE: Perfectly matched. Light values are optimal.")
    elif delta_lv > 0:
        print("⚠️ OVEREXPOSURE: Camera configuration requires adjustment for a brighter scene.")
    else:
        print("⚠️ UNDEREXPOSURE: Camera configuration requires adjustment for a darker scene.")

if __name__ == "__main__":
    main()
