import matplotlib.pyplot as plt
import orbit, power, thermal

GPU_POWER_W = 700
LEO_ALTITUDE_KM = 550
LEO_DOD = 0.3
GEO_ALTITUDE_KM = 35786
GEO_DOD = 0.7

def main():
    gpu_counts = []
    leo_array_areas = []
    geo_array_areas = []
    radiator_areas = []

    for gpu_count in range(100, 10001, 100):
        load = power.total_power_w(gpu_count, GPU_POWER_W)
        leo_area = power.solar_array_area_m2(power.solar_array_power_w(load, LEO_ALTITUDE_KM))
        geo_area = power.solar_array_area_m2(power.solar_array_power_w(load, GEO_ALTITUDE_KM))
        radiator = thermal.radiator_area_m2(load)

        gpu_counts.append(gpu_count)
        leo_array_areas.append(leo_area)
        geo_array_areas.append(geo_area)
        radiator_areas.append(radiator)

    plt.plot(gpu_counts, leo_array_areas, label="Solar array (LEO, 550 km)")
    plt.plot(gpu_counts, geo_array_areas, label="Solar array (GEO)")
    plt.plot(gpu_counts, radiator_areas, label="Radiator (300 K)")
    plt.xlabel('Number of GPUs')
    plt.ylabel('Area (m²)')
    plt.title('Orbital data centre: required area vs. GPU count')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("results.png", dpi=150)       
    print("Saved results.png")

# run the program
if __name__ == "__main__":
    main()