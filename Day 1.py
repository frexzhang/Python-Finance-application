# Author: Frex
# -*- coding = utf-8 -*-
# @Time:  18/12/2024 16:07
# @Author:Olivier Frex
# @File:  Day 1.py
# @Software: PyCharm
import numpy_financial as np

import numpy


salary = 60000
savings_rate = 0.25
investment_rate= 0.05
desired_cash =1500000
annual_cash = salary*savings_rate

years_to_retirement=np.nper(investment_rate,-annual_cash,0,desired_cash)
print(f'Martha has {years_to_retirement:,.1f} years to retirement.')

investment_rates = [0.05,0.06,0.07]
for i_rate in investment_rates:
    years_to_retirement = np.nper(i_rate, -annual_cash, 0, desired_cash)
    print(f'Martha has {years_to_retirement:,.1f} years to retirement if she earns a {i_rate:.1%} return.')

