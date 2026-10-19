import pytest
from orbit import orbital_period, eclipse_duration
from power import total_power_w, solar_array_power_w, battery_capacity_wh
from thermal import radiator_area_m2


def test_iss_period():
    # ISS at 420 km should take about 92.8 minutes per orbit
    assert orbital_period(420) / 60 == pytest.approx(92.8, abs=0.1)


def test_geo_eclipse():
    assert eclipse_duration(35786) / 60 == pytest.approx(69.3, abs=0.1)


def test_radiator_area():
    assert radiator_area_m2(910000) == pytest.approx(1100.7, abs=0.1)


def test_leo_needs_bigger_array():
    load = total_power_w(1000, 700)
    leo = solar_array_power_w(load, 550)
    geo = solar_array_power_w(load, 35786)
    assert leo > geo


def test_battery_scales_linearly():
    load = total_power_w(1000, 700)
    single = battery_capacity_wh(load, 550, 0.3)
    double = battery_capacity_wh(2 * load, 550, 0.3)
    assert double == pytest.approx(single * 2)