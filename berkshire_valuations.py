from util import present_value_of_future_cash_flows

print("\n")

no_of_shares_outstanding = 1232245

print("per 1996 annual report growing @ 18% (past 3 years earning growth without including geico acquisition!)")

print(f"bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 10)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183, 10)}")
print(f"per share bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 10)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183, 10)/no_of_shares_outstanding}")

print(f"berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 20)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183, 20)}")
print(f"per share berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 20)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183, 20)/no_of_shares_outstanding}")

print(f"berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 100)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183, 100)}")
print(f"per share berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 100)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065,0.183, 100)/no_of_shares_outstanding}")

print(f"berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 200)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183 , 200)}")
print(f"per share berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.183, 200)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.183 , 200)/no_of_shares_outstanding}")


print("\n")
print("per 1996 annual report growing @ 5% (conservative)")

print(f"bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 10)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05, 10)}")
print(f"per share bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 10)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05, 10)/no_of_shares_outstanding}")

print(f"berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 20)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05, 20)}")
print(f"per share berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 20)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05, 20)/no_of_shares_outstanding}")

print(f"berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 100)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05, 100)}")
print(f"per share berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 100)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065,0.05, 100)/no_of_shares_outstanding}")

print(f"berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 200)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05 , 200)}")
print(f"per share berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0.05, 200)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.065, 0.05 , 200)/no_of_shares_outstanding}")
