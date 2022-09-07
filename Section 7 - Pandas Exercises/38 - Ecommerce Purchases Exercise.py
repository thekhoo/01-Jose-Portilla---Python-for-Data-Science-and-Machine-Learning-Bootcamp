import pandas as pd
import os

# Change Working Directory
os.chdir('./Section 7 - Pandas Exercises')

# Reading in the CSV File
ecom = pd.read_csv('data/Ecommerce Purchases.csv')
print(ecom.head())

# Getting Data on the DataFrame
print(f"Rows: {ecom.shape[0]} Columns: {ecom.shape[1]}\n")

# Average Purchase Price
avg_purchase_price = ecom['Purchase Price'].mean()
print(f"Average Purchase Price: {avg_purchase_price}")

# Highest and Lowest Purchase Price
max_price = ecom['Purchase Price'].max()
min_price = ecom['Purchase Price'].min()
print(f"Highest Price: {max_price}\nLowest Price: {min_price}\n")

# How many people have english as their language of choice?
eng_ecom = ecom[ecom['Language'] == 'en']
print(f"{len(eng_ecom)} have selected 'en' as their language of choice.\n")

# Job Title Lawyer
lawyer_ecom = ecom[ecom['Job'] == 'Lawyer']
print(f"Lawyers: {len(lawyer_ecom)}\n")

# How many morning and evening purchases
print(ecom['AM or PM'].value_counts())
print()

# 5 Most Common Job Titles
print(ecom['Job'].value_counts().head())
print()

# Purchase Price from Lot 90 WT
lot_filter = ecom['Lot'] == '90 WT'
lot_df = ecom[lot_filter]
print(lot_df['Purchase Price'])
print()

# Email of the person with the following credit card number
credit_card_no = 4926535242672853
print(ecom[ecom['Credit Card'] == credit_card_no]['Email'])
print()

# How many people have American Express as their Credit Card Provider and made a purchase over $95
purchase_filter = ecom['Purchase Price'] > 95
cc_provider_filter = ecom['CC Provider'] == 'American Express'
amex_df = ecom[purchase_filter & cc_provider_filter]
print(f"Number of AMEX Cards with purchases over $95: {len(amex_df)}")
print()

# Credit Card that expires in 2025
def get_expiry(date:str):
    return date.split('/')[1]

expiry_year_series = ecom['CC Exp Date'].apply(get_expiry)
expire_2025 = expiry_year_series[expiry_year_series == '25']
print(f"Number of Credit Cards Expiring in 2025: {len(expire_2025)}")
print()

# 5 most popilar email providers
def get_provider(email:str):
    return email.split('@')[1]

email_provider_series = ecom['Email'].apply(get_provider)
print(email_provider_series.value_counts().head())
