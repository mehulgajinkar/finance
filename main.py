import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('balance_sheets/marico_ltd_balance_sheet.csv')
df_bs = df.replace(to_replace=np.nan, value=0)
df = pd.read_csv('annual_performance/marico_ltd_annual_performance.csv')
df_is = df.replace(to_replace=np.nan, value=0)

df_bs.set_index('Heads', inplace=True) # sets required column as index instead of def number
#print(df_bs.head())
df_is.set_index('Heads', inplace=True)
# print(df_is.head())

# ARRAY CALCULATIONS
# ========================================================================================================

def calculate_averages(input_list):
    # Create a new list to store averages
    averages_list = []

    # Initialize the first element of the averages list with zero
    averages_list.append(0)

    # Calculate averages for the rest of the elements
    for i in range(1, len(input_list)):
        # Calculate the average of the current element and its previous element
        average = (input_list[i] + input_list[i - 1]) / 2.0
        averages_list.append(average)

    # Discard the first element of the averages list
    averages_list = averages_list[1:]

    return averages_list

def calculate_growth(input_list):
    # Create a new list to store growth
    growth_list = []

    # Initialize the first element of the averages list with zero
    growth_list.append(0)

    # Calculate growth for the rest of the elements
    for i in range(1, len(input_list)):
        # Calculate the growth of the current element and its previous element
        growth = ((input_list[i] / input_list[i - 1]) - 1)*100
        growth_list.append(growth)

    # Discard the first element of the growth list
    growth_list = growth_list[1:]

    return growth_list

# PLOT MODULES
# ========================================================================================================

def growth_plot():

    # plt.style.use("fivethirtyeight")
    # plt.xkcd()

    plt.plot(time_period[1:], growth_sales, label = "Sales")
    plt.plot(time_period[1:], growth_raw_material_cost, color = "#444444", linestyle = "--", marker = "o", label = "Raw Material Costs")
    plt.plot(time_period[1:], growth_total_op_cost, label = "Total Operating Costs")
    plt.xlabel("Years")
    plt.ylabel("Growth in Percentage")
    plt.title("Growth Metrics")
    plt.legend()
    # plt.grid(True)
    plt.tight_layout()
    # print(plt.style.available)
    # plt.savefig("plot_image.png")
    plt.show()

def turnover_ratio_plot():

    # plt.style.use("seaborn-darkgrid")
    # plt.xkcd()

    plt.plot(time_period[1:], total_assets_turnover_ratio, label = "Total Assets Turnover")
    plt.plot(time_period[1:], net_fixed_assets_turnover_ratio, color = "#444444", linestyle = "--", marker = "o", label = "Net Fixed Assets Turnover")
    plt.plot(time_period[1:], current_assets_turnover_ratio, label = "Current Assets Turnover")
    plt.plot(time_period[1:], inventory_turnover_ratio, label="Inventory Turnover")
    plt.plot(time_period[1:], receivables_turnover_ratio, linestyle = "--", marker = "o", label="Receivable Turnover")
    plt.plot(time_period[1:], creditors_turnover_ratio, linestyle = "--", marker = "o", label="Creditors Turnover")
    plt.xlabel("Years")
    plt.ylabel("Turnover Points")
    plt.title("Turnover Ratios")
    plt.legend()
    # plt.grid(True)
    plt.tight_layout()
    # print(plt.style.available)
    # plt.savefig("plot_image.png")
    plt.show()

# ALL REQUIRED BALANCE SHEET HEADER INITIATIONS
# ========================================================================================================

time_period = df_bs.columns.tolist()

shareholders_funds = df_bs.loc["Shareholders' funds"].tolist()
capital = df_bs.loc["Capital"].tolist()
reserves_and_surplus = df_bs.loc["Reserves and surplus"].tolist()

net_fixed_assets = df_bs.loc["Net fixed assets"].tolist()
net_preopex_pending_allocation = df_bs.loc["Net pre-operative expenses pending allocation"].tolist()
capital_wip = df_bs.loc["Capital work-in-progress"].tolist()
investments = df_bs.loc["Investments"].tolist()
other_non_curr_assets = df_bs.loc["Other non-current assets"].tolist()
curr_assets_n_loans_n_advances = df_bs.loc["Current assets & loans and advances"].tolist()
def_tax_assets = df_bs.loc["Deferred tax assets"].tolist()
misc_exp_not_written_off = df_bs.loc["Miscellaneous expenditure (not written off or adjusted)"].tolist()

curr_liab_n_provisions = df_bs.loc["Current liabilities & provisions"].tolist()

inventories = df_bs.loc["Inventories"].tolist()
cash_n_bank_bal = df_bs.loc["Cash and bank balances"].tolist()

receivables = df_bs.loc["Sundry debtors & bills receivable"].tolist()

curr_liab = df_bs.loc["Current liabilities"].tolist()

borrowings = df_bs.loc["Borrowings"].tolist()

# ALL REQUIRED INCOME STATEMENT HEADER INITIATIONS
# ========================================================================================================

total_raw_materials = df_is.loc["Raw materials, etc & purch of fin gds"].tolist()
salaries = df_is.loc["Salaries and wages"].tolist()
power_n_fuel = df_is.loc["Power & fuel"].tolist()
rent_n_lease = df_is.loc["Rent & lease rent"].tolist()
freight_out = df_is.loc["Outward freight/other dist expenses"].tolist()
net_sales = df_is.loc["Net sales"].tolist()

pbdit = df_is.loc["PBDIT"].tolist()
depreciation = df_is.loc["Depreciation"].tolist()

pat = df_is.loc["Net profit (PAT)"].tolist()

interest = df_is.loc["Interest expenses"].tolist()

total_tax_provisions = df_is.loc["Total tax provision"].tolist()

total_op_cost = df_is.loc["Operating expenses"].tolist()

pbt = df_is.loc["PBT"].tolist()

# ALL REQUIRED DERIVED HEADER INITIATIONS
# ========================================================================================================

total_net_worth = (np.array(shareholders_funds)).tolist()

cogs = (np.array(total_raw_materials)
        + np.array(salaries)
        + np.array(power_n_fuel)
        + np.array(rent_n_lease)
        + np.array(freight_out)).tolist()

total_assets = (np.around(np.array(net_fixed_assets)
              + np.array(net_preopex_pending_allocation)
              + np.array(capital_wip) + np.array(investments)
              + np.array(other_non_curr_assets)
              + np.array(curr_assets_n_loans_n_advances)
              + np.array(def_tax_assets)
              + np.array(misc_exp_not_written_off),2)).tolist()

quick_assets = (np.array(curr_assets_n_loans_n_advances)
        + np.array(inventories)).tolist()

tnw = (np.array(total_net_worth)
        - np.array(misc_exp_not_written_off)).tolist()

average_tnw = calculate_averages(tnw)

pbit = (np.array(pbdit)
        - np.array(depreciation)).tolist()

# USER REQUIRED FIELDS INITIATIONS
# ========================================================================================================

number_of_shares = 1
face_value_of_shares = 1
curr_stock_price = 1
mkt_value_of_equity = 1
dividends = 1


# PROFITABILITY RATIOS
# ========================================================================================================
print("\n========PROFITABILITY RATIOS========\n")

# Gross Profit Margin: Gross Profit / Net Sales
# Note: Network Cost not included. Freight Out included

gross_profit = (np.array(net_sales) - np.array(cogs)).tolist()
gross_profit_margin = (np.around((np.array(gross_profit) / np.array(net_sales)*100),2)).tolist()
print("Gross Profit Margin:    ",gross_profit_margin)

# Operating Profit Margin: EBIT / Net Sales

ebit = (np.array(pbdit) - np.array(depreciation)).tolist()

op_profit_margin = (np.around((np.array(ebit) / np.array(net_sales)*100),2)).tolist()
print("Operating Profit Margin:",op_profit_margin)

# Net Profit Margin: PAT / Net Sales

net_profit_margin = (np.around((np.array(pat) / np.array(net_sales)*100),2)).tolist()
print("Net Profit Margin:      ",net_profit_margin)

# Cash Profit Margin: PBDIT / Net Sales

cash_profit_margin = (np.around((np.array(pbdit) / np.array(net_sales)*100),2)).tolist()
print("Cash Profit Margin:     ",cash_profit_margin)

# LIQUIDITY RATIOS
# ========================================================================================================
print("\n========LIQUIDITY RATIOS========\n")

# Current Ratio: Current Assets, Loans and Advances / Current Liabilities and Provisions

current_ratio = (np.around((np.array(curr_assets_n_loans_n_advances) / np.array(curr_liab_n_provisions)),2)).tolist()
print("Current Ratio:",current_ratio)

# Quick Ratio: (Current Assets - Inventories) / Current Liabilities and Provisions

quick_ratio = (np.around((np.array(quick_assets) / np.array(curr_liab_n_provisions)),2)).tolist()
print("Quick Ratio:  ",quick_ratio)

# Cash Ratio: Cash and Bank Balances / Current Liabilities and Provisions

cash_ratio = (np.around((np.array(cash_n_bank_bal) / np.array(curr_liab_n_provisions)),2)).tolist()
print("Cash Ratio:   ",cash_ratio)

# TURNOVER RATIOS
# ========================================================================================================
print("\n========TURNOVER RATIOS========\n")

# Total Assets Turnover Ratio: Net Sales / Average Total Assets

average_total_assets = calculate_averages(total_assets)
total_assets_turnover_ratio = (np.around((np.array(net_sales[1:]) / np.array(average_total_assets)),2)).tolist()

print("Total Assets Turnover Ratio:                          ",total_assets_turnover_ratio)

# Net Fixed Assets Turnover Ratio: Net Sales / Average Net Fixed Assets

average_net_fixed_assets = calculate_averages(net_fixed_assets)
net_fixed_assets_turnover_ratio = (np.around((np.array(net_sales[1:]) / np.array(average_net_fixed_assets)),2)).tolist()

print("Net Fixed Assets Turnover Ratio:                      ",net_fixed_assets_turnover_ratio)

# Current Assets Turnover Ratio: Net Sales / Average Current Assets

average_current_assets = calculate_averages(curr_assets_n_loans_n_advances)
current_assets_turnover_ratio = (np.around((np.array(net_sales[1:]) / np.array(average_current_assets)),2)).tolist()

print("Current Assets Turnover Ratio:                        ",current_assets_turnover_ratio)

# Inventory Turnover Ratio: COGS / Average Inventories

average_inventories = calculate_averages(inventories)
inventory_turnover_ratio = (np.around((np.array(cogs[1:]) / np.array(average_inventories)),2)).tolist()

print("Inventory Turnover Ratio:                             ",inventory_turnover_ratio)

# Receivable Turnover Ratio: Net Sales / Average Receivables

average_receivables = calculate_averages(receivables)
receivables_turnover_ratio = (np.around((np.array(net_sales[1:]) / np.array(average_receivables)),2)).tolist()

print("Receivable Turnover Ratio:                            ",receivables_turnover_ratio)

# Creditors Turnover Ratio: Raw Material Costs / Average Trade Creditors (CAUTION: Available here: Current liabilities)

average_curr_liab = calculate_averages(curr_liab)
creditors_turnover_ratio = (np.around((np.array(total_raw_materials[1:]) / np.array(average_curr_liab)),2)).tolist()

print("Creditors Turnover Ratio (CAUTION: Check Parameters): ",creditors_turnover_ratio)

# SOLVENCY RATIOS
# ========================================================================================================
print("\n========SOLVENCY RATIOS========\n")

# Debt To Equity: Long Term Borrowings / (Net worth - Misc Exp Not Written Off)

debt_to_equity = (np.around(np.array(borrowings) / ((np.array(total_net_worth) - np.array(misc_exp_not_written_off))),4)).tolist()
print("Debt to Equity Ratio:                                   ",debt_to_equity)

# Total Debt to Equity: (Long Term Borrowings + Short Term Borrowings [CAUTION: Available here: Current Liabilities) / (Net worth - Misc Exp Not Written Off)

total_debt_to_equity = (np.around((np.array(borrowings) + np.array(curr_liab)) / ((np.array(total_net_worth) - np.array(misc_exp_not_written_off))),2)).tolist()
print("Total Debt to Equity Ratio (CAUTION: Check Parameters): ",total_debt_to_equity)

# TOL/TNW: (Total Assets - Net worth) / (Net worth - Misc Exp Not Written Off)

tol_tnw_ratio = (np.around((np.array(total_assets) - np.array(total_net_worth)) / ((np.array(total_net_worth) - np.array(misc_exp_not_written_off))),2)).tolist()
print("TOL/TNW Ratio:                                          ",tol_tnw_ratio)

# Interest Cover Ratio: (EBIT - Tax) / Interest

interest_cover_ratio = (np.around((np.array(pbdit) - np.array(depreciation) - np.array(total_tax_provisions)) / ((np.array(interest))),2)).tolist()
print("Interest Coverage Ratio:                                ", interest_cover_ratio)

# HOLDING PERIODS (DAYS)
# ========================================================================================================
print("\n========HOLDING PERIODS (DAYS)========\n")

# Inventory Period: (Average Inventory) / (COGS / 365)

h_inventory_period = (np.around((np.array(average_inventories)) / ((np.array(cogs[1:]))/365),0)).tolist()
print("Holding Inventory Period:                             ", h_inventory_period)

# Receivables Period: (Average Receivables) / (Net Sales / 365)

h_receivables_period = (np.around((np.array(average_receivables)) / ((np.array(net_sales[1:]))/365),0)).tolist()
print("Holding Receivables Period:                           ", h_receivables_period)

# Creditors Period : (Average Trade Creditors [CAUTION: Available here: Average Current Liabilities] ) / (Raw Material Cost / 365)

h_creditors_period = (np.around((np.array(average_curr_liab)) / ((np.array(total_raw_materials[1:]))/365),0)).tolist()
print("Holding Creditors Period (CAUTION: Check Parameters): ", h_creditors_period)

# OPERATING CYCLE (DAYS)
# ========================================================================================================
print("\n========OPERATING CYCLE (DAYS)========\n")

# Operating Inventory Period: (Average Inventory) / (Net Sales / 365)
op_inventory_period = (np.around((np.array(average_inventories)) / ((np.array(net_sales[1:]))/365),0)).tolist()
print("Operating Inventory Period:                             ", op_inventory_period)

# Operating Receivables Period: (Average Receivables) / (Net Sales / 365)
op_receivables_period = (np.around((np.array(average_receivables)) / ((np.array(net_sales[1:]))/365),0)).tolist()
print("Operating Receivables Period:                           ", op_receivables_period)

# Creditors Period : (Average Trade Creditors [CAUTION: Available here: Average Current Liabilities] ) / (Net Sales / 365)

op_creditors_period = (np.around((np.array(average_curr_liab)) / ((np.array(net_sales[1:]))/365),0)).tolist()
print("Operating Creditors Period (CAUTION: Check Parameters): ", op_creditors_period)

# Operating Cycle: Inventory Period + Recievables Period

operating_cycle = (np.around((np.array(op_inventory_period)) + (np.array(op_receivables_period)),0)).tolist()
print("Operating Cycle:                                        ", operating_cycle)

# Net Operating Cycle: Inventory Period + Recievables Period - Creditors Period

net_operating_cycle = (np.around((np.array(op_inventory_period)) + (np.array(op_receivables_period)) - (np.array(op_creditors_period)),0)).tolist()
print("Net Operating Cycle:                                    ", net_operating_cycle)

# OTHER RATIOS
# ========================================================================================================
print("\n========OTHER RATIOS========\n")

# ROA : EBIT / Average Total Assets

roa = (np.around((((np.array(ebit[1:])) / (np.array(average_total_assets)))*100),2)).tolist()
print("ROA: ", roa)

# ROE : PAT / Average Tangible Net Worth

roe = (np.around((((np.array(pat[1:])) / (np.array(average_tnw)))*100),2)).tolist()
print("ROE: ", roe)

# GROWTH
# ========================================================================================================
print("\n========GROWTH========\n")

# GROWTH : (Current Element / Previous Element) - 1

growth_sales = (np.around((calculate_growth(net_sales)),2)).tolist()
print("Sales (YoY):                ", growth_sales)

growth_raw_material_cost = (np.around((calculate_growth(total_raw_materials)),2)).tolist()
print("Raw Material Costs (YoY):   ", growth_raw_material_cost)

growth_total_op_cost = (np.around((calculate_growth(total_op_cost)),2)).tolist()
print("Total Operating Costs (YoY): ", growth_total_op_cost)

# DuPont Analysis
# ========================================================================================================
print("\n========DuPont Analysis========\n")

pat_by_pbt = (np.around((((np.array(pat[1:])) / (np.array(pbt[1:])))*1),2)).tolist()
print("PAT/PBT:                                ", pat_by_pbt)

pbt_by_pbit = (np.around((((np.array(pbt[1:])) / (np.array(pbit[1:])))*1),2)).tolist()
print("PBT/PBIT:                               ", pbt_by_pbit)

pbit_by_net_sales = (np.around((((np.array(pbit[1:])) / (np.array(net_sales[1:])))*1),2)).tolist()
print("PBIT/Net Sales:                         ", pbit_by_net_sales)

net_sales_by_avg_total_assets = (np.around((((np.array(net_sales[1:])) / (np.array(average_total_assets)))*1),2)).tolist()
print("Net Sales/Average Total Assets:         ", net_sales_by_avg_total_assets)

avg_total_assets_by_avg_net_worth = (np.around((((np.array(average_total_assets)) / (np.array(average_tnw)))*1),2)).tolist()
print("Average Total Assets/Average Net Worth: ", avg_total_assets_by_avg_net_worth)

roe_dupont = (np.around((np.array(pat_by_pbt)
              * np.array(pbt_by_pbit)
              * np.array(pbit_by_net_sales)
              * np.array(net_sales_by_avg_total_assets)
              * np.array(avg_total_assets_by_avg_net_worth)*100),2)).tolist()

print("ROE DuPont:                             ", roe_dupont)


"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--WORK IN PROGRESS--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# EQUITY RATIOS
# ========================================================================================================

# EPS: PAT / Number of Shares

eps = (np.divide(pat,number_of_shares)).tolist()
print("EPS:",eps)

# DPS: Dividends / Number of Shares

dps = dividends / number_of_shares
print("DPS:",dps)

# Book Value Per Share: (Net Worth - Misc Exp Not Written Off) / Number of Shares

book_val_per_share = (np.divide(np.around((np.array(total_net_worth) - np.array(misc_exp_not_written_off)),2),number_of_shares)).tolist()
print("Book Value Per Share:",book_val_per_share)

# Payout Ratio: DPS / EPS

payout_ratio = (np.divide(dps,eps)).tolist()
print("Payout Ratio:",payout_ratio)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

#Plots

growth_plot()
turnover_ratio_plot()