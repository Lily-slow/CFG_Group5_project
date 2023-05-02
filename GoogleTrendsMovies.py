import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# Create a pytrends object
pytrends = TrendReq()

# Set search parameters
kw_list = ["Contagion"]
timeframe = "2019-01-01 2023-04-30"

# Fetch data from Google Trends API
pytrends.build_payload(kw_list, timeframe=timeframe)
trends_data = pytrends.interest_over_time()

# Plot the trends data
plt.plot(trends_data.index, trends_data['Contagion'])
plt.title("Interest over time for 'Fast X'")
plt.xlabel("Time")
plt.ylabel("Interest")
plt.show()
