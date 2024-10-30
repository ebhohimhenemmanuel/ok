import pandas as pd

import seaborn as sns

weather = pd.read_csv('weather.csv')

weather.head()

weather.info()

sns.barplot(weather['wind_speed'],weather['temperature'])

sns.distplot(weather['temperature'])

sns.distplot(weather['humidity'], rug=True);

sns.jointplot(weather['humidity'],weather['temperature'])

sns.jointplot(weather['humidity'],weather['temperature'], kind="hex")

sns.jointplot(weather['humidity'],weather['temperature'], kind="kde")

sns.pairplot(weather[['humidity', 'temperature','air_pollution_index']])

sns.stripplot(weather['weather_type'], weather['temperature'])

sns.stripplot(weather['weather_type'], weather['temperature'], jitter = True)

sns.swarmplot(weather['humidity'],weather['temperature'])

sns.lmplot(x="humidity", y="temperature", data=weather)