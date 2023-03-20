from util import present_value_of_future_cash_flows

print("\n")

no_of_shares_outstanding = 1232245

print("per 1996 annual report")

print(f"bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 10)} - {present_value_of_future_cash_flows(2448600000, 0.075, 0, 10)}")
print(f"per share bershire net worth 10y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 10)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.075, 0, 10)/no_of_shares_outstanding}")

print(f"berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 20)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0, 20)}")
print(f"per share berkshire net worth 30y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 20)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.075, 0, 20)/no_of_shares_outstanding}")

print(f"berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 100)} - {present_value_of_future_cash_flows(2448600000, 0.065,0, 100)}")
print(f"per share berkshire net worth 100y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 100)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.075,0, 100)/no_of_shares_outstanding}")

print(f"berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 200)} - {present_value_of_future_cash_flows(2448600000, 0.065, 0 , 200)}")
print(f"per share berkshire net worth 200y duration: {present_value_of_future_cash_flows(2448600000, 0.045, 0, 200)/no_of_shares_outstanding} - {present_value_of_future_cash_flows(2448600000, 0.075, 0 , 200)/no_of_shares_outstanding}")


