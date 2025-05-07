import pandas as pd
import matplotlib.pyplot as plt

# Define month order explicitly for sorting
MONTH_ORDER = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

def load_temperature_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Ensure MONTH column is in title case and ordered properly
        df['PERIOD'] = df['PERIOD'].str.strip().str.title()
        df['PERIOD'] = pd.Categorical(df['PERIOD'], categories=MONTH_ORDER, ordered=True)

        df = df[df['YEAR'] == 2024]  # Filter year if needed
        df = df.sort_values(by='PERIOD')  # Sort by month order
        return df['PERIOD'].tolist(), df['STATS_VALUE'].tolist()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return [], []

def plot_temperature_comparison(months, akl_temps, chch_temps):
    plt.figure(figsize=(12, 6))
    plt.plot(months, akl_temps, marker='o', label='Auckland', color='red')
    plt.plot(months, chch_temps, marker='s', label='Christchurch', color='blue')

    plt.title("Monthly Average Temperatures in 2024: Auckland vs Christchurch")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    akl_file = 'Auckland_monthly_temp.csv'
    chch_file = 'Christchurch_monthly_temp.csv'

    months_akl, akl_temps = load_temperature_data(akl_file)
    months_chch, chch_temps = load_temperature_data(chch_file)

    if months_akl != months_chch:
        print("Mismatch in months between files. Ensure both cities have the same months.")
        return

    plot_temperature_comparison(months_akl, akl_temps, chch_temps)

if __name__ == "__main__":
    main()
