import pyowm.owm
import rumps


class WeatherApp(rumps.App):
    API_KEY = 'YOUR_API_KEY'
    DEFAULT_CITY = 'Roma,IT'

    def __init__(self):
        super().__init__(name="Weather Widget", title='Loading...')
        self.weather_manager = pyowm.OWM(self.API_KEY).weather_manager()
        self.city = self.DEFAULT_CITY

    @property
    def observation(self):
        return self.weather_manager.weather_at_place(self.city)

    @property
    def current_weather(self):
        return self.observation.weather

    @property
    def temperature(self):
        return self.current_weather.temperature('celsius')['temp']

    @property
    def description(self):
        return self.current_weather.detailed_status.capitalize()

    def update_weather(self):
        self.title = f"{round(self.temperature)}°C {self.description}"

    @rumps.timer(600)
    def update_weather_periodically(self, _):
        self.update_weather()

    @rumps.clicked("Refresh data")
    def refresh_data(self, _):
        self.update_weather()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
