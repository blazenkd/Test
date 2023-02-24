# 2/21/2023
# ---FreeCodeCamp---
"""
Budget App Project 3
"""
import pandas as pd
# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)
print(certificates_earned[certificates_earned > 5])

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

print(certificates_earned.iloc[2])

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

names = ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
