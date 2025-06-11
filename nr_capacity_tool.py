import math

class CapacityModel:
    '''
        Stores all input values
    ''' 
    def __init__(self, area_km2, subscriber_density, bht_gb_dl, bht_gb_ul, 
                 embb_ratio, urllc_ratio, mmtc_ratio, 
                 bandwidth_fr1, bandwidth_fr2, 
                 mimo_gain_fr1, mimo_gain_fr2, 
                 spectral_eff_fr1, spectral_eff_fr2,
                 cells_per_site=3):
        self.area_km2 = area_km2
        self.subscriber_density = subscriber_density
        self.bht_dl = bht_gb_dl * 8000 / 3600  # Mbps per user
        self.bht_ul = bht_gb_ul * 8000 / 3600
        self.embb_ratio = embb_ratio
        self.urllc_ratio = urllc_ratio
        self.mmtc_ratio = mmtc_ratio
        self.bandwidth_fr1 = bandwidth_fr1
        self.bandwidth_fr2 = bandwidth_fr2
        self.mimo_gain_fr1 = mimo_gain_fr1
        self.mimo_gain_fr2 = mimo_gain_fr2
        self.spectral_eff_fr1 = spectral_eff_fr1
        self.spectral_eff_fr2 = spectral_eff_fr2
        self.cells_per_site = cells_per_site


'''
Calculates the total expected network traffic (in Mbps) based on the area,
user density and service profile ratios provided in the parameters.
'''
def calculate_total_traffic(params: CapacityModel) -> float:
    total_users = params.area_km2 * params.subscriber_density
    total_traffic = total_users * (
        params.bht_dl * params.embb_ratio +
        0.1 * params.urllc_ratio +  # URLLC estimation
        0.001 * params.mmtc_ratio   # mMTC estimation
    )
    return total_traffic  # in Mbps


'''
Computes the maximum data throughput of a single cell (in Mbps) using
channel bandwidth, spectral efficiency, and MIMO gain.
'''
def calculate_cell_throughput(bw_mhz, se_bps_hz, mimo_gain) -> float:
    return bw_mhz * se_bps_hz * mimo_gain


'''
Estimates the required number of cells and base station sites needed to handle 
the calculated total traffic, given the cell capacities and sectorization.
'''
def estimate_site_requirements(total_traffic, fr1_throughput, fr2_throughput, utilization=0.7, cells_per_site=3):
    total_capacity = lambda x: x * utilization
    fr1_cells = math.ceil(total_traffic / total_capacity(fr1_throughput))
    fr2_cells = math.ceil(total_traffic / total_capacity(fr2_throughput))
    total_cells = min(fr1_cells, fr2_cells)
    total_sites = math.ceil(total_cells / cells_per_site)
    return total_cells, total_sites


'''
Aggregates all calculations and returns a summary dictionary with 
total traffic, single cell capacities, and required cells/sites for the given scenario.
'''
def generate_summary(params: CapacityModel):
    traffic = calculate_total_traffic(params)

    fr1_capacity = calculate_cell_throughput(params.bandwidth_fr1, params.spectral_eff_fr1, params.mimo_gain_fr1)
    fr2_capacity = calculate_cell_throughput(params.bandwidth_fr2, params.spectral_eff_fr2, params.mimo_gain_fr2)

    cells, sites = estimate_site_requirements(traffic, fr1_capacity, fr2_capacity, cells_per_site=params.cells_per_site)

    return {
        "Total Traffic (Mbps)": round(traffic, 2),
        "FR1 Cell Throughput (Mbps)": round(fr1_capacity, 2),
        "FR2 Cell Throughput (Mbps)": round(fr2_capacity, 2),
        "Estimated Cells Required": cells,
        "Estimated Sites Required": sites
    }

'''
The example
'''
if __name__ == "__main__":
    scenario = CapacityModel(
        area_km2=10,
        subscriber_density=5000,
        l=2,
        bht_gb_ul=0.5,
        embb_ratio=0.6,
        urllc_ratio=0.3,
        mmtc_ratio=0.1,
        bandwidth_fr1=100,
        bandwidth_fr2=400,
        mimo_gain_fr1=4,
        mimo_gain_fr2=6,
        spectral_eff_fr1=4.2,
        spectral_eff_fr2=6.8
    )

    summary = generate_summary(scenario)
    for k, v in summary.items():
        print(f"{k}: {v}")
