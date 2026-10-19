from orbit import orbital_period, eclipse_duration

SOLAR_CONSTANT_W_M2 = 1361 # sunlight power per m^2 above the atmosphere
CELL_EFFICIENCY = 0.30 # good space-grade solar cells
BATTERY_EFFICIENCY = 0.9 # energy you get back out of the battery compared with what you put in
BATTERY_SPECIFIC_ENERGY_WH_KG = 150 # watt-hours stored per kilogram of lithium-ion battery
TEST_CASES = [("550km", 550, 1000, 700, 0.3), ("GEO", 35786, 1000, 700, 0.7)] # name, altitude, num_gpus, gpu_power_w, depth_of_discharge

def total_power_w(num_gpus, gpu_power_w, overhead=0.3):
    """Returns the total power in watts. Overhead consists of CPUs, networking, and cooling loops."""
    return num_gpus * gpu_power_w * (1 + overhead)

def solar_array_power_w(load_w, altitude_km): # panels only work in sunlight, so in that time they need to both power the load and also recharge the battery for the next eclipse
    """Returns the solar array power in watts."""
    daylight = orbital_period(altitude_km) - eclipse_duration(altitude_km)
    return load_w * (daylight + eclipse_duration(altitude_km) / BATTERY_EFFICIENCY) / daylight

def solar_array_area_m2(array_power_w):
    """Returns the solar array area in meters squared."""
    return array_power_w / (SOLAR_CONSTANT_W_M2 * CELL_EFFICIENCY)

def battery_capacity_wh(load_w, altitude_km, depth_of_discharge): # depth of discharge is how much of the battery is drained in each cycle. 
    """Returns the battery capacity in watt-hours."""
    energy_used_per_eclipse = load_w * eclipse_duration(altitude_km) / 3600. # Divide by 3,600 to convert watt-seconds into watt-hours.
    return energy_used_per_eclipse / depth_of_discharge

def battery_mass_kg(capacity_wh):
    """Returns the mass of the battery in kilograms."""
    return capacity_wh / BATTERY_SPECIFIC_ENERGY_WH_KG

# run some tests
def main():
    print("Orbit, Altitude, Total Power, Solar Array Power, Solar Array Area, Battery Capacity, Battery Mass")
    for name, altitude, num_gpus, gpu_power_w, depth_of_discharge in TEST_CASES:
        load_w = total_power_w(num_gpus, gpu_power_w)
        array_power_w = solar_array_power_w(load_w, altitude)
        battery_cap_wh = battery_capacity_wh(load_w, altitude, depth_of_discharge)
        print(name, altitude, 'km',
        f'{load_w / 1000:.1f}', 'kilowatts',
        f'{array_power_w / 1000:.1f}', 'kilowatts',
        f'{solar_array_area_m2(array_power_w):.1f}', 'meters squared',
        f'{battery_cap_wh / 1000:.1f}', 'kilowatt-hours',
        f'{battery_mass_kg(battery_cap_wh):.1f}', 'kilograms',)

# run the program
if __name__ == "__main__":
    main()