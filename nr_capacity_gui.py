import tkinter as tk
from tkinter import ttk, messagebox
from nr_capacity_tool import CapacityModel, generate_summary


class NRCapacityGUI(tk.Tk):
    '''
    Class contains GUI for the NR Capacity Dimensioning Tool
    '''
    def __init__(self):
        super().__init__()
        self.title("NR Capacity Dimensioning Tool")
        self.geometry("500x600")
        self.create_widgets()

    def create_widgets(self):
        self.inputs = {}
        fields = [
            ("Area (km²)", "area_km2"),
            ("Subscriber Density (users/km²)", "subscriber_density"),
            ("Busy Hour DL Traffic (GB/sub)", "bht_gb_dl"),
            ("Busy Hour UL Traffic (GB/sub)", "bht_gb_ul"),
            ("eMBB Ratio (0–1)", "embb_ratio"),
            ("URLLC Ratio (0–1)", "urllc_ratio"),
            ("mMTC Ratio (0–1)", "mmtc_ratio"),
            ("FR1 Bandwidth (MHz)", "bandwidth_fr1"),
            ("FR2 Bandwidth (MHz)", "bandwidth_fr2"),
            ("FR1 MIMO Gain", "mimo_gain_fr1"),
            ("FR2 MIMO Gain", "mimo_gain_fr2"),
            ("FR1 Spectral Efficiency", "spectral_eff_fr1"),
            ("FR2 Spectral Efficiency", "spectral_eff_fr2")
        ]

        for label, key in fields:
            ttk.Label(self, text=label).pack()
            entry = ttk.Entry(self)
            entry.pack()
            self.inputs[key] = entry

        ttk.Button(self, text="Run Dimensioning", command=self.run_calculation).pack(pady=10)
        self.output_text = tk.Text(self, height=12, width=60)
        self.output_text.pack()

    def run_calculation(self):
        try:
            values = {k: float(self.inputs[k].get()) for k in self.inputs}
            params = CapacityModel(**values)
            results = generate_summary(params)

            self.output_text.delete(1.0, tk.END)
            for key, val in results.items():
                self.output_text.insert(tk.END, f"{key}: {val}\n")
        except Exception as e:
            messagebox.showerror("Input Error", str(e))


if __name__ == "__main__":
    app = NRCapacityGUI()
    app.mainloop()
