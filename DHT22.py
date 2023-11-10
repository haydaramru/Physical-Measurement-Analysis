import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

time = np.arange(0, 3600, 60)  

humidity_mean = 50  
humidity_variation = 5  

humidity = humidity_mean + humidity_variation * np.random.randn(len(time))
humidity = np.clip(humidity, 0, 100) 

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, humidity, marker='o', linestyle='-', color='b')
plt.title('DHT22 Humidity Sensor Dummy Data')
plt.xlabel('Time (s)')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()

