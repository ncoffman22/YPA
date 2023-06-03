#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data.xlsx')

less_than_2_data = data[data['Range End'] < 3]
less_than_2_hours = less_than_2_data.groupby('Year')['Audience %'].sum()

greater_than_equal_2_data = data[data['Range End'] >= 3]
greater_than_equal_2_hours = greater_than_equal_2_data.groupby('Year')['Audience %'].sum()

fig, ax = plt.subplots()

ax.plot(less_than_2_hours.index, less_than_2_hours, label='Less than 2 hours')
ax.plot(greater_than_equal_2_hours.index, greater_than_equal_2_hours, label='Greater than or equal to 2 hours')

ax.set_xticks(data['Year'].unique())
ax.set_xticklabels(data['Year'].unique(), rotation=45)
ax.set_ylabel('Percentage')
# ax.set_title('Social Media Usage of Youths Aged 16-19 from 2012-2022')
ax.legend(title='Key')

# plt.figtext(0.5, 0.01, 'Based on yearly Q4 surveys from GlobalWebIndex 2023', ha='center', fontsize=6, va='center')
plt.show()
