from util import present_value_of_future_cash_flows

print("\n")
print(f"palantir net worth 10y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 10)} - {present_value_of_future_cash_flows(1000000000, 0.065, 0, 10)}")

print(f"palantir net worth 30y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 20)} - {present_value_of_future_cash_flows(1000000000, 0.065, 0, 20)}")

print(f"palantir net worth 100y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 100)} - {present_value_of_future_cash_flows(1000000000, 0.065,0, 100)}")

print(f"palantir net worth 200y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 200)} - {present_value_of_future_cash_flows(1000000000, 0.065, 0 , 200)}")


print("\n")
print(f"palantir per share 10y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 10)/1980000000} - {present_value_of_future_cash_flows(1000000000, 0.065, 0, 10)/1980000000}")

print(f"palantir per share 30y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 20)/1980000000} - {present_value_of_future_cash_flows(1000000000, 0.065, 0, 20)/1980000000}")

print(f"palantir per share 100y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 100)/1980000000} - {present_value_of_future_cash_flows(1000000000, 0.065,0, 100)/1980000000}")

print(f"palantir per share 200y duration: {present_value_of_future_cash_flows(1000000000, 0.045, 0, 200)/1980000000} - {present_value_of_future_cash_flows(1000000000, 0.065, 0 , 200)/1980000000}")





