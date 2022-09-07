import pandas as pd
import os

# Change Working Directory
os.chdir('./Section 7 - Pandas Exercises')

# Open CSV File
sal = pd.read_csv('data/Salaries.csv')

# DataFrame Info
print(sal.info())

# Average Base Pay
avg_basepay = sal['BasePay'].mean()
print(f"Average Base Pay: {avg_basepay}\n")

# Highest Overtime Pay
max_otpay = sal['OvertimePay'].max()
print(f"Maximum Overtime Pay: {max_otpay}\n")

# Job title of JOSEPH DRISCOLL
joseph_job = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print(f"Joseph Driscoll's job is - {joseph_job}\n")

# JOSEPH DRISCOLL total pay including benefits
joseph_pay = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(f"Joseph Driscoll's pay including benefits is - {joseph_pay}\n")

# Name of the highest paid person including benefits
max_pay_amt = sal['TotalPayBenefits'].max()
max_pay_filter = sal['TotalPayBenefits'] == max_pay_amt
max_pay_df = sal[max_pay_filter]
print(f"The name of the highest paid person is {max_pay_df['EmployeeName']}\n")

# Lowest paid person including benefits
min_pay_amt = sal['TotalPayBenefits'].min()
min_pay_filter = sal['TotalPayBenefits'] == min_pay_amt
min_pay_df = sal[min_pay_filter]
print(f"The name of the lowest paid person is {min_pay_df['EmployeeName']}\n")

# Average Base Pay per year from 2011 - 2014
avg_basepay_peryear = sal.groupby(by='Year',axis=0).mean()
print(avg_basepay_peryear['BasePay'])
print()

# Number of Unique Job Titles
print(f"The number of unique job titles are: {sal['JobTitle'].nunique()}\n")

# Top 5 most common jobs
joblist = sal['JobTitle'].value_counts()
print(joblist.head())
print()

# Jobs that only appeared once in 2013
sal_2013 = sal[sal['Year'] == 2013]                 # Get the data for 2013
jobs_2013 = sal_2013['JobTitle'].value_counts()     # Get the different job value counts in 2013
jobs_oneperson = jobs_2013[jobs_2013 == 1]          # Get the jobs with a job count of 1
print(jobs_oneperson)
print(f'The number of jobs held by one person only is: {len(jobs_oneperson)}\n')


# How many people have the word chief in their job title?

# Custom formula to determine if string contains chief
def isChief(name:str):
    return name.lower().find('chief') != -1

sal_copy = sal.copy()
sal_copy = sal_copy['JobTitle'].apply(isChief)
print(sal[sal_copy])
print(f"The number of jobs that have chief in the title is: {len(sal[sal_copy])}\n")

# Correlation between job title length and salary
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len','TotalPayBenefits']].corr())


