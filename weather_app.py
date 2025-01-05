import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x500")
        
        # Replace with your API key from OpenWeatherMap
        self.api_key = "583f87dba86bcb68058fa123777f933a"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Create and set up the main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create widgets
        self.setup_widgets()
        
    def setup_widgets(self):
        # City entry
        ttk.Label(self.main_frame, text="Enter City:").grid(row=0, column=0, pady=10)
        self.city_entry = ttk.Entry(self.main_frame, width=30)
        self.city_entry.grid(row=0, column=1, pady=10)
        
        # Search button
        ttk.Button(self.main_frame, text="Search", command=self.get_weather).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Weather info display
        self.weather_frame = ttk.LabelFrame(self.main_frame, text="Weather Information", padding="10")
        self.weather_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        # Weather labels
        self.temp_label = ttk.Label(self.weather_frame, text="Temperature: ")
        self.temp_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        
        self.feels_like_label = ttk.Label(self.weather_frame, text="Feels Like: ")
        self.feels_like_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        
        self.humidity_label = ttk.Label(self.weather_frame, text="Humidity: ")
        self.humidity_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        
        self.desc_label = ttk.Label(self.weather_frame, text="Description: ")
        self.desc_label.grid(row=3, column=0, pady=5, sticky=tk.W)
        
        self.wind_label = ttk.Label(self.weather_frame, text="Wind Speed: ")
        self.wind_label.grid(row=4, column=0, pady=5, sticky=tk.W)
        
        self.last_updated_label = ttk.Label(self.weather_frame, text="Last Updated: ")
        self.last_updated_label.grid(row=5, column=0, pady=5, sticky=tk.W)
        
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
            
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"  # For Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]
                
                # Update labels
                self.temp_label.config(text=f"Temperature: {temp}°C")
                self.feels_like_label.config(text=f"Feels Like: {feels_like}°C")
                self.humidity_label.config(text=f"Humidity: {humidity}%")
                self.desc_label.config(text=f"Description: {description.capitalize()}")
                self.wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
                self.last_updated_label.config(text=f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                messagebox.showerror("Error", f"Error: {data['message']}")
                
        except requests.RequestException:
            messagebox.showerror("Error", "Failed to fetch weather data. Please check your internet connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()