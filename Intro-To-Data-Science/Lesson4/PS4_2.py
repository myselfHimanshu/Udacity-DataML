from pandas import *
from ggplot import *
from datetime import *
from numpy import mean

def plot_weather_data(turnstile_weather, csv=False):
    '''
    plots a histogram of entries by day of week
    '''
    pandas.options.mode.chained_assignment = None
    if csv:
        df = read_csv(turnstile_weather)
    else:
        df = turnstile_weather

    df['Day'] = df['DATEn'].map(lambda x:datetime.strptime(x, '%Y-%m-%d').strftime('%w'))
    
    agg = df.groupby(['Day'], as_index=False).aggregate(mean)

    plot = ggplot(agg, aes(x='Day', y='ENTRIESn_hourly')) + geom_line() +geom_point()
           
    return plot
