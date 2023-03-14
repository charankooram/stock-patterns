def present_value_of_future_cash_flows(net_income, discount_rate, earnings_increase_yoy, duration):
    valuation = 0
    for d in range(duration+1):
        valuation += (net_income)*pow(1 + earnings_increase_yoy, d)/pow(1+discount_rate, d)
        #print(f"d {d} value {valuation}")
    return valuation
    

def check_earnings_for_valuation(target_valuation, discount_rate, earnings_increase_yoy, duration):
    net_earnings = 250
    while(present_value_of_future_cash_flows(net_earnings, discount_rate, earnings_increase_yoy, duration) < target_valuation):
        #print(f"ne {operating_earnings} duration {duration}")
        operating_earnings += 10
    return net_earnings
