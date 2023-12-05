import pyowm.owm
import rumps


class WeatherApp(rumps.App):
    """Получить ключ можно на сайте
    https://openweathermap.org/api
    API_KEY ваш ключ
    DEFAULT_CITY ваш город
    """
    API_KEY = YOUR_KEY
    DEFAULT_CITY = YOUR_CITY

    def __init__(self):
        super(WeatherApp, self).__init__("Weather Widget", 'Loading...')
        self.weather_manager = pyowm.OWM(self.API_KEY).weather_manager()

    @rumps.timer(1200)
    def update_weather(self, _):
        observation = self.weather_manager.weather_at_place(self.DEFAULT_CITY)
        weather = observation.weather
        icon = f'img/{weather.weather_icon_name[:-1]}.png'
        temperature = round(weather.temperature('celsius')['temp'])
        self.title = f"{temperature}°C"
        self.icon = icon

    @rumps.clicked("Refresh data")
    def refresh_data(self, _):
        self.update_weather()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
