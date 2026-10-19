import math # needed for pi, sqrt, asin

EARTH_RADIUS_KM = 6371 # in kilometers
EARTH_GRAVITATIONAL_PARAMETER_KM3_S2 = 398600.4418 # in km^3 / s^2
ORBITS = [("ISS", 420), ("Starlink", 550), ("GEO", 35786)]

def orbit_radius(altitude_km):
    """Returns the orbit radius in kilometers."""
    return EARTH_RADIUS_KM + altitude_km

def orbital_period(altitude_km):
    """Returns the orbital period in seconds."""
    return 2 * math.pi * math.sqrt((orbit_radius(altitude_km) ** 3) / EARTH_GRAVITATIONAL_PARAMETER_KM3_S2)

def eclipse_duration(altitude_km):
    """Returns the worst-case time spent in Earth's shadow, in seconds."""
    fraction_in_shadow = math.asin(EARTH_RADIUS_KM / orbit_radius(altitude_km)) / math.pi
    return fraction_in_shadow * orbital_period(altitude_km)

# test some altitudes
def main():
    print("Orbit, Altitude, Period, Eclipse")
    for name, altitude in orbits:
        print(name, altitude, 'km',
        f'{orbital_period(altitude) / 60:.1f}', 'min',
        f'{eclipse_duration(altitude) / 60:.1f}', 'min')

# run the program
if __name__ == "__main__":
    main()