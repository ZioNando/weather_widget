import pyowm.owm
import rumps


class WeatherApp(rumps.App):
    API_KEY = 'YOUR_KEY'
    DEFAULT_CITY = 'CITY,COUNTRY_ABBR'

    def __init__(self):
        super(WeatherApp, self).__init__("Weather Widget", 'Loading...')
        self.weather_manager = pyowm.OWM(self.API_KEY).weather_manager()

    @property
    def observation(self):
        return self.weather_manager.weather_at_place(self.DEFAULT_CITY)

    @property
    def current_weather(self):
        return self.observation.weather

    @property
    def temperature(self):
        return self.current_weather.temperature('celsius')['temp']

    @property
    def description(self):
        return self.current_weather.detailed_status.capitalize()

    @rumps.timer(1200)
    def update_weather(self, _):
        self.title = f"{round(self.temperature)}°C {self.description}"

    @rumps.clicked("Refresh data")
    def refresh_data(self, _):
        self.update_weather()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
