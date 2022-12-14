# density in kg/L
# 1028.19 kg/l a los −2 °C, 1028.11 a los 0 °C, 1.027.78 a los 4°C
def calculate_density(temperature):
    density = -2000

    if temperature == -2:
        density = 1028.19
    elif temperature == 0:
        density = 1028.11
    elif temperature == 4:
        density = 1027.78
    elif temperature < 0:
        density = -0.04*temperature + 1028.11
    elif temperature > 0:
        density = -0.165*temperature + 1028.11

    return round(density, 2)
