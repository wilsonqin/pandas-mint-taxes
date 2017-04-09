# pandas-mint-taxes

Ever wanted to use Python and basic data analysis skills to help do your taxes?

I'll show you how it's possible using a few features of the popular personal finance service Mint.com, in conjunction with your favorite data analysis package.
Mint is a service that syncs with your financial statements from various credit cards and banks, and allows you to view your transactions from across multiple accounts in one unified dashboard.

For the purposes of this tutorial, I will use the Python programming language and Pandas data manipulation library, but great alternatives could be R or Excel if you are more familiar with those. This project provides a sample dummy Mint transactions csv export, with example code snippets in `.py`, `.ipython/juptyer` and in markdown form.

### DISCLAIMER: 
### THIS DEMO IS DISTRIBUTED FOR EDUCATIONAL PURPOSES ONLY. IT IS NOT TAX-RELATED ADVICE OR FILING SOFTWARE. 
### FOR ALL TAX-RELATED QUESTIONS AND CONCERNS PLEASE ASK A CERTIFIED ACCOUNTANT


Before We Start
--------
You will need to set up a [Mint.com](https://www.mint.com/how-mint-works) account, and connect any bank/credit-card accounts that you'd like to analyze for your taxes. 
If you do not have an account yet, you will need to set one up if you wish to play along with your own data.

This tutorial's syntax assumes you're using Python 2.7 version. 

You will need the following Python Packages installed: `pandas`. This can be done in one fell swoop using the `requirements.txt` file provided, by running the command `pip install -r requirements.txt`.

