import pyowm.owm
import rumps


class WeatherApp(rumps.App):
    def __init__(self):
        super().__init__(name="Weather Widget", title='Loading...')
        owm = pyowm.OWM('API_KEY')
        self.weather_manager = owm.weather_manager()
        self.city = 'Roma,IT'
        self.update_weather()

    @rumps.timer(600)
    def update_weather(self, _=None):
        observation = self.weather_manager.weather_at_place(self.city)
        w = observation.weather
        # wind = w.wind()['speed']  # speed of wind
        temperature = w.temperature('celsius')['temp']
        description = w.detailed_status  # or w.status

        self.title = f"{round(temperature):}°C {description.capitalize()}"

    @rumps.clicked("Refresh data")
    def update_menu(self, _):
        self.update_weather()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
