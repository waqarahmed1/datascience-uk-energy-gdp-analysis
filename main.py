
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# Download source 'Indicators.csv' file from here:
# https://www.kaggle.com/datasets/kaggle/world-development-indicators?select=Indicators.csv
DATA_SOURCE_FILE = "/YOUR_LOCAL_PATH/Indicators.csv"

def main():

    ##################################### LINE GRAPH FOR ENERGY IMPORTS #####################################
    data = pd.read_csv(DATA_SOURCE_FILE)
    print(data.shape)
    countries = data['CountryName'].unique().tolist()
    country_code = data['CountryCode'].unique().tolist()
    indicators = data['IndicatorName'].unique().tolist()
    years = data['Year'].unique().tolist()

    print(f'Number of indicators: {len(indicators)}')
    print(f'Number of countries: {len(countries)} and no of country code: {len(country_code)}')
    print(f'Years data from {min(years)} till {max(years)}, over {len(years)} years')

    indicator_name = 'Energy imports'
    sample_country_code = 'GBR'

    mask1 = data['IndicatorName'].str.contains(indicator_name)
    mask2 = data['CountryCode'].str.contains(sample_country_code)
    stage = data[mask1 & mask2]

    years   = stage['Year'].values
    energy  = stage['Value'].values
    plt.plot(years,energy)
    plt.xlabel('Years')
    plt.ylabel(stage['IndicatorName'].iloc[0])

    years = stage['Year'].values
    energy = stage['Value'].values
    plt.plot(years,energy)
    plt.xlabel('Years')
    plt.ylabel(stage['IndicatorName'].iloc[0])

    ax = plt.gca()
    ax.spines['bottom'].set_position(("data",0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()

    ##################################### HISTOGRAM FOR ENERGY IMPORTS #####################################

    plt.hist(energy,10,density=False,facecolor='green')
    plt.xlabel(stage['IndicatorName'].iloc[0])
    plt.ylabel('# of Years')
    plt.title('Energy Import distribution (UK)')
    plt.show()

    ##################################### GDP for UK #####################################

    gdp_indicator = 'GDP per capita \(constant 2005'
    mask_gdp      = data['IndicatorName'].str.contains(gdp_indicator)
    gdp_stage     = data[mask_gdp & mask2]

    plt.plot(gdp_stage['Year'].values, gdp_stage['Value'].values)
    plt.xlabel('Year')
    plt.ylabel(gdp_stage['IndicatorName'].iloc[0])
    plt.title('GDP per Capita UK')

    plt.axis([1955,2020,0,45000])
    plt.show()

    ##################################### CORRELATION ENERGY IMPORTS V GDP FOR UK #####################################

    print(gdp_stage)
    print('GDP Min Year = ', gdp_stage['Year'].min(),"max: ", gdp_stage['Year'].max())
    print('Energy imports Min Year = ', stage['Year'].min(), "max: ",stage['Year'].max())

    gdp_stage_trunc = gdp_stage[gdp_stage['Year'] < 2014]

    fig, axis = plt.subplots()
    axis.yaxis.grid(True)
    axis.set_title('Energy imports Vs. GDP (per capita)',fontsize=10)
    axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[0],fontsize=10)
    axis.set_ylabel(stage['IndicatorName'].iloc[0],fontsize=10)

    X = gdp_stage_trunc['Value']
    Y = stage['Value']

    axis.scatter(X, Y)
    plt.show()
    print(np.corrcoef(gdp_stage_trunc['Value'], stage['Value']))
    
if __name__ == "__main__":
    main()
    
