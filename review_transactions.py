### DISCLAIMER:
### THIS DEMO IS DISTRIBUTED FOR EDUCATIONAL PURPOSES ONLY. IT IS NOT TAX-RELATED ADVICE OR FILING SOFTWARE.
### FOR ALL TAX-RELATED QUESTIONS AND CONCERNS PLEASE ASK A CERTIFIED ACCOUNTANT

import pandas as pd

# TODO: move your MINT.com transactions.csv into this project directory
# / the directory where you are running jupyter notebook
PATH_TO_YOUR_TRANSACTIONS = "transactions.csv"

df = pd.DataFrame.from_csv(PATH_TO_YOUR_TRANSACTIONS)



## Create a Dataframe view for only 2016 year transactions
# the leftmost column of the ingested csv file, by default is assumed as your 'index' of the DataFrame
# here we filter for all records w. dates less than Jan 1, 2017 and greater than Dec 31, 2015
# what is returned: a new view of the DataFrame only with records in this restricted date range
y16 = df[(df.index < '2017-01-01') & ( df.index > '2015-12-31' )]

# Using the Mint 'Rental Car & Taxi' category label
# it's possible to create a view for all 2016 rental/taxi expenditure
rentalcar = y16[y16.Category == "Rental Car & Taxi"]


## A way to sum-up train/metro/public-transit expenditures
# Substitute your public transit specific search strings e.g. "MBTA", "MTA", "BART", "SUBWAY"
#
# Side Note:
# If you eat a lot at Subway and if your public transit code contains SUBWAY,
# you may be counting sandwiches too in this view :-)
MBTA = y16[y16['Original Description'].str.contains("MBTA")]


## Example of how to quickly sum up the 'Amount' columns for several different views.
transport_sum = MBTA.Amount.sum() + rentalcar.Amount.sum()

## What if we want to figure out travel expenses for a business trip to San Francisco
sf_transport = y16[(y16.index > '2016-06-24') & (y16.index < '2016-07-05')]
sf_transport_sum = sf_transport.Amount.sum()
