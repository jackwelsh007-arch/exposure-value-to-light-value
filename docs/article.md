# Demystifying the APEX System: The Transition from Exposure Value to Modern Light Value

---

## Camera Settings and the Exposure Triangle

For optimal exposure, modern cameras provide three adjustable parameters: the aperture f-number ($N$), the exposure time or shutter speed ($t$), and the sensor sensitivity ($S$, ISO arithmetic speed / film speed).

Using the reflected-light meter calibration constant $K$ and the luminance $L$, the equilibrium condition for optimal camera settings under a given ambient brightness $L$ and a given film speed $S$ is defined as:

$$\frac{N^2}{t} = \frac{S}{K} \cdot L \quad (1)$$

Luminance $L$ is typically measured in $\text{cd/m}^2$, and a standard industry value for the calibration constant is $K = 12.5 \ \frac{\text{cd}\cdot\text{s}}{\text{m}^2}$.

This equilibrium equation originates from an era when ambient brightness $L$ and film speed $S$ had to be accepted as fixed external parameters. Once a film was loaded into the camera, it could not be altered dynamically. Consequently, the only adjustable camera parameters were the aperture f-number and the shutter speed. 

Because light perception (much like sound perception) is processed logarithmically by the human visual system, these physical variables were transformed into a scale that is perceived linearly by humans. This yields the camera variable $EV_{\text{cam}} = \log_2\left(\frac{N^2}{t}\right)$ and the external environmental variable $EV_{\text{ext}} = \log_2\left(\frac{S}{K} \cdot L\right)$. 

The Exposure Value of the camera must match the externally determined Exposure Value, meaning the optimal exposure condition simplifies to:

$$EV_{\text{cam}} = EV_{\text{ext}}$$

However, this conventional setup represents a historical legacy. Because of it, one must always specify the corresponding Exposure Value at a fixed given ISO speed. 

In modern digital workflows, the ISO speed has transitioned into a fully dynamic, adjustable camera parameter. Therefore, it mathematically makes sense to shift this variable to the left side of our optimization equation. The only true external parameter dictated solely by the environment is the ambient luminance $L$ (brightness). Shifting the variables yields the updated condition:

$$\frac{N^2}{t} \cdot \frac{K}{S} = L \quad (2)$$

For practical application, the photographic industry normalizes this luminance value to $L_{\text{nor}}$:

$$L_{\text{nor}} = L \cdot \frac{100}{K}$$

By doing so, we can define unified variables tailored directly to human visual perception, known as Light Values ($LV$). These are expressed as $LV_{\text{cam}} = \log_2\left(\frac{N^2}{t} \cdot \frac{100}{S}\right)$ and $LV_{\text{ext}} = \log_2(L_{\text{nor}})$. 

Multiplying equation (2) by $\frac{100}{K}$ and applying a base-2 logarithm ($\log_2$) mathematically derives our modern optimal exposure balance:

$$LV_{\text{cam}} = LV_{\text{ext}}$$

---

## Additive APEX Components and Exposure Compensation

If we now explicitly define the Aperture Value ($av$), Time Value ($tv$), and Speed Value or Sensitivity Value ($sv$) as follows:

$$av = \log_2(N^2)$$
$$tv = \log_2(t)$$
$$sv = \log_2\left(\frac{S}{100}\right)$$

The overall camera light value ($LV_{\text{cam}}$) gracefully decomposes additively into three distinct f-stop components:

$$LV_{\text{cam}} = av - tv - sv$$

### Practical Implications

This linear relationship simplifies manual exposure math immensely. For example: If you increase the aperture f-number by one full f-stop from $N$ to $1.4N$, the Aperture Value increases from $av$ to $av' = av + 1$. This structural change subsequently raises the overall camera light value from $LV_{\text{cam}}$ to $LV_{\text{cam}}' = LV_{\text{cam}} + 1$. 

In practical terms, the camera is now configured for an ambient brightness environment that is one full f-stop brighter than reality. If left uncorrected, the resulting image would turn out underexposed. 

To counteract this shift and maintain a constant camera light value, you must increase either the shutter speed duration or the sensor sensitivity by exactly one full f-stop. This means adjusting time from $t$ to $2t$ or sensitivity from $S$ to $2S$. 

Doing so increases the Time Value or Speed Value accordingly by one full f-stop (from $tv$ to $tv' = tv + 1$ or from $sv$ to $sv' = sv + 1$). The absolute sum of the equation remains perfectly constant, and the exposure stays mathematically optimal. This balance can be written, e.g. as compensation via film speed (meaning tv' = tv):

$$LV' = av' - tv' - sv' = (av + 1) - tv - (sv + 1) = av - tv - sv = LV$$ 

### The Digital Light Meter

Many modern camera manufacturers have natively integrated this exact mathematical approach into their user interfaces. They display the precise deviation between light parameters as:

$$\Delta LV = LV_{\text{ext}} - LV_{\text{cam}}$$

This delta is widely known to photographers as the Exposure Compensation Scale (or exposure light meter). The camera's internal meter continuously measures the external environmental light value ($LV_{\text{ext}}$) and references it against the current internal camera parameters ($LV_{\text{cam}}$). 

If the digital exposure indicator ($\Delta LV$) shows a positive deviation from zero—for instance, a value of $+2$ f-stops—it mathematically signifies that the current configuration will yield an image that is 4 times overexposed ($2^2 = 4$). 

To re-establish an optimal balance, the photographer or the automated camera system must apply a collective reduction of 2 full f-stops. This can be achieved by:
* Increasing the aperture f-number by 2 stops (av' = $av + 2$).
* Reducing the exposure duration by 2 stops ($tv' = tv - 2$).
* Reducing the film speed sensitivity by 2 stops ($sv' = sv - 2$).
* Reducing the shutter speed and film speed by 1 stop ($tv' = tv - 1$ and $sv' = sv - 1$).

Any combination of manual adjustments that yields a net reduction of 2 f-stops across the system successfully restores mathematically optimal exposure conditions for the photograph.
