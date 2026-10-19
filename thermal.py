from power import total_power_w

EMISSIVITY = 0.9
STEFAN_BOLTZMANN = 5.670374419e-8
TEST_CASES = (250, 300, 350) # kelvin

def radiator_area_m2(heat_w, temperature_k=300, sides=2):
    """Returns the radiator area in square metres needed to reject heat_w watts."""
    return heat_w / (sides * EMISSIVITY * STEFAN_BOLTZMANN * temperature_k ** 4)

# run some tests
def main():
    load_w = total_power_w(1000, 700)
    print("Radiator Area for", load_w / 1000, "kW")
    for temp in TEST_CASES:
        print(temp, 'K',
        f'{radiator_area_m2(load_w, temp):.1f}', 'meters squared')

# run the program
if __name__ == "__main__":
    main()