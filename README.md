# pandas-mint-taxes

Ever wanted to use Python and basic data analysis skills to help do your taxes?

I'll show you how it's possible using a few features of the popular personal finance service Mint.com, in conjunction with your favorite data analysis package.
Mint is a service that syncs with your financial statements from various credit cards and banks, and allows you to view your transactions from across multiple accounts in one unified dashboard.

For the purposes of this tutorial, I will use the Python programming language and Pandas data manipulation library, but great alternatives could be R or Excel if you are more familiar with those. This projects assumes you will obtain a Mint transactions csv export, with example code snippets in `.py`, and `.ipython/juptyer` form.

### DISCLAIMER: 
### THIS DEMO IS DISTRIBUTED FOR EDUCATIONAL PURPOSES ONLY. IT IS NOT TAX-RELATED ADVICE OR FILING SOFTWARE. 
### FOR ALL TAX-RELATED QUESTIONS AND CONCERNS PLEASE ASK A CERTIFIED ACCOUNTANT


Before We Start
--------
You will need to set up a [Mint.com](https://www.mint.com/how-mint-works) account, and connect any bank/credit-card accounts that you'd like to analyze.
If you do not have an account yet, you will need to set one up if you wish to play along with your own data.

This tutorial's syntax assumes you're using Python 2.7 version. 

You will need the following Python Packages installed: `pandas`. This can be done in one fell swoop using the `requirements.txt` file provided, by running the command `pip install -r requirements.txt`.

Exporting Mint Transactions
--------
Go to your Mint `Transactions`, it should look something like this:
![Navigating to Mint Transactions Tab](/tutorial_images/MintTransactionScreen.png?raw=true "Mint Transactions Tab")

Next, to export your transaction history, scroll to the bottom of the tab, and click the export link, which will prompt your browser to download a `transactions.csv` file. Move it to your workspace / working directory.
![Mint Export Transactions](/tutorial_images/MintExportTransactions.png?raw=true "Mint Export Transactions")

Run Python Scripts
---------
Jupyter: run `jupyter notebook` in your working directory (the project directory with these scripts) which should allow you to initiate the `review_transactions.ipynb` in your browser window to begin exploring your transactions log.

Python: run `python review_transactions.py`

Quick Overview of Pandas and DataFrames
------------
Pandas is a data manipulation library which allows for the creation of in-memory DataFrame objects.

DataFrames allow for quick access to views of your original Data Frame with various query predicates (aka attribute filtering) applied. In this example, the transactions are the rows, with Dates, Descriptions, Amounts, etc as attributes.

This allows for statistical manipulations on different data attribute types (integers, floats, strings).
In this tutorial, you will specifically see some string attribute searches, and numeric summations in action.

![Pandas Year Date Range Filter 2016](/tutorial_images/YearDateRangeFilterExample.png?raw=true "Pandas Year Date Range Filter 2016")

![Taxi Transport Example](/tutorial_images/TaxiTransportExample.png?raw=true "Taxi Transport View")

![Public Transit Example](/tutorial_images/PublicTransitExample.png?raw=true "Public Transit Example")
