from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(28341124)
condition = lookup.condition
forecasts = lookup.forecast
print(forecasts[0].date)
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)

print(condition.text)