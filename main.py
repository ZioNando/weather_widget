import pyowm.owm
import rumps


class WeatherApp(rumps.App):
    """You can get the key on the website
    https://openweathermap.org/api
    API_KEY your key
    DEFAULT_CITY your city
    """
    API_KEY = HERE_API_KEY
    DEFAULT_CITY = 'CITY, COUNTRY_ABBR'

    def __init__(self):
        super(WeatherApp, self).__init__("Weather Widget", 'Loading...')
        self.weather_manager = pyowm.OWM(self.API_KEY).weather_manager()

    @rumps.timer(1200)
    def update_weather(self, _):
        observation = self.weather_manager.weather_at_place(self.DEFAULT_CITY)
        temperature = round(observation.weather.temperature('celsius')['temp'])
        self.icon = f'img/{observation.weather.weather_icon_name[:-1]}.png'
        self.title = f"{temperature}°C"

    @rumps.clicked("Refresh data")
    def refresh_data(self, _):
        self.update_weather()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
