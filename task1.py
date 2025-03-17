import requests

API_KEY = "1b426be26aa84acba20b9cde4b80a225"  # Replace with the API key you copied
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()



# Extract and print weather details
temperature = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['description']

print(f"City: {CITY}")  
print(f"Temperature: {temperature}°C")  
print(f"Humidity: {humidity}%")  
print(f"Weather: {weather}")  

print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Weather: {weather}")

import matplotlib.pyplot as plt
import seaborn as sns

cities = ["Mumbai", "Delhi", "New York", "London", "Tokyo"]
temps = []

for city in cities:
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL).json()
    temps.append(response['main']['temp'])

# Create a bar plot
sns.barplot(x=cities, y=temps)
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Comparison Across Cities")
plt.show()
