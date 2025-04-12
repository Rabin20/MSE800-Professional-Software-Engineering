import numpy as np


temperature_in_degree = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])


average_temp = np.mean(temperature_in_degree)
print(f"Average temperature: {average_temp:.2f}°C")


max_temp = np.max(temperature_in_degree)
min_temp = np.min(temperature_in_degree)
print(f"Highest temperature: {max_temp}°C")
print(f"Lowest temperature: {min_temp}°C")


temperatures_fahrenheit = (temperature_in_degree * 9/5) + 32
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)


above_20_indices = np.where(temperature_in_degree > 20)[0]
print("Days with temperature above 20°C (by index):", above_20_indices)
