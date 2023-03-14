#def present_value_of_future_cash_flows(operating_income, discount_rate, earnings_increase_yoy, duration):
#    valuation = 0
#    for d in range(duration+1):
#        valuation += (operating_income)*pow(1 + earnings_increase_yoy, d)/pow(1+discount_rate, d)
#        #print(f"d {d} value {valuation}")
#    return valuation
    

#def check_earnings_for_valuation(target_valuation, discount_rate, earnings_increase_yoy, duration):
#    operating_earnings = 250
#    while(present_value_of_future_cash_flows(operating_earnings, discount_rate, earnings_increase_yoy, duration) < #target_valuation):
#        #print(f"oe {operating_earnings} duration {duration}")
#        operating_earnings += 10
#    return operating_earnings

from util import *
    
print(f"OE 250 mill DR 0.0025 YOY 0 duration 20y networth {present_value_of_future_cash_flows(250, 0.0025, 0, 20)} mill")

print(f"OE 250 mill DR 0.0025 YOY 0 duration 30y networth {present_value_of_future_cash_flows(250, 0.0025, 0, 30)} mill")

print(f"OE 250 mill DR 0.0025 YOY 0 duration 100y networth {present_value_of_future_cash_flows(250, 0.0025, 0, 100)} mill")

print(f"OE 250 mill DR 0.0025 YOY 0.04 duration 20y networth {present_value_of_future_cash_flows(250, 0.0025, 0.04, 20)} mill")

print(f"OE 250 mill DR 0.0025 YOY 0.04 duration 30y networth {present_value_of_future_cash_flows(250, 0.0025, 0.04, 30)} mill")

print(f"OE 250 mill DR 0.0025 YOY 0.04 duration 100y networth {present_value_of_future_cash_flows(250, 0.0025, 0.04, 100)} mill")

print(f"OE 250 mill DR 0.02 YOY 0 duration 20y networth {present_value_of_future_cash_flows(250, 0.02, 0, 20)} mill")

print(f"OE 250 mill DR 0.02 YOY 0 duration 30y networth {present_value_of_future_cash_flows(250, 0.02, 0, 30)} mill")

print(f"OE 250 mill DR 0.02 YOY 0 duration 100y networth {present_value_of_future_cash_flows(250, 0.02, 0, 100)} mill")

print(f"OE 250 mill DR 0.02 YOY 0.04 duration 20y networth {present_value_of_future_cash_flows(250, 0.02, 0.04, 20)} mill")

print(f"OE 250 mill DR 0.02 YOY 0.04 duration 30y networth {present_value_of_future_cash_flows(250, 0.02, 0.04, 30)} mill")

print(f"OE 250 mill DR 0.02 YOY 0.04 duration 100y networth {present_value_of_future_cash_flows(250, 0.02, 0.04, 100)} mill")

print(f"OE 250 mill DR 0.04 YOY 0 duration 20y networth {present_value_of_future_cash_flows(250, 0.04, 0, 20)} mill")

print(f"OE 250 mill DR 0.04 YOY 0 duration 30y networth {present_value_of_future_cash_flows(250, 0.04, 0, 30)} mill")

print(f"OE 250 mill DR 0.04 YOY 0 duration 100y networth {present_value_of_future_cash_flows(250, 0.04, 0, 100)} mill")

print(f"OE 250 mill DR 0.04 YOY 0.04 duration 20y networth {present_value_of_future_cash_flows(250, 0.04, 0.04, 20)} mill")

print(f"OE 250 mill DR 0.04 YOY 0.04 duration 30y networth {present_value_of_future_cash_flows(250, 0.04, 0.04, 30)} mill")

print(f"OE 250 mill DR 0.04 YOY 0.04 duration 100y networth {present_value_of_future_cash_flows(250, 0.04, 0.04, 100)} mill")

print(f"OE 250 mill DR 0.05 YOY 0 duration 20y networth {present_value_of_future_cash_flows(250, 0.05, 0, 20)} mill")

print(f"OE 250 mill DR 0.05 YOY 0 duration 30y networth {present_value_of_future_cash_flows(250, 0.05, 0, 30)} mill")

print(f"OE 250 mill DR 0.05 YOY 0 duration 100y networth {present_value_of_future_cash_flows(250, 0.05, 0, 100)} mill")

print(f"OE 250 mill DR 0.05 YOY 0.04 duration 20y networth {present_value_of_future_cash_flows(250, 0.05, 0.04, 20)} mill")

print(f"OE 250 mill DR 0.05 YOY 0.04 duration 30y networth {present_value_of_future_cash_flows(250, 0.05, 0.04, 30)} mill")

print(f"OE 250 mill DR 0.05 YOY 0.04 duration 100y networth {present_value_of_future_cash_flows(250, 0.05, 0.04, 100)} mill")

print(f"OE 250 mill DR 0.06 YOY 0 duration 20y networth {present_value_of_future_cash_flows(250, 0.06, 0, 20)} mill")

print(f"OE 250 mill DR 0.06 YOY 0 duration 30y networth {present_value_of_future_cash_flows(250, 0.06, 0, 30)} mill")

print(f"OE 250 mill DR 0.06 YOY 0 duration 100y networth {present_value_of_future_cash_flows(250, 0.06, 0, 100)} mill")

print(f"OE 250 mill DR 0.06 YOY 0.04 duration 20y networth {present_value_of_future_cash_flows(250, 0.06, 0.04, 20)} mill")

print(f"OE 250 mill DR 0.06 YOY 0.04 duration 30y networth {present_value_of_future_cash_flows(250, 0.06, 0.04, 30)} mill")

print(f"OE 250 mill DR 0.06 YOY 0.04 duration 100y networth {present_value_of_future_cash_flows(250, 0.06, 0.04, 100)} mill")

print(f"OE 11,500 mill DR 0.04 YOY 0 duration 5y networth {present_value_of_future_cash_flows(11500, 0.04, 0, 5)} mill")
print(f"OE 11,500 mill DR 0.04 YOY 0.04 duration 5y networth {present_value_of_future_cash_flows(11500, 0.04, 0.04, 5)} mill")
print(f"OE 11,500 mill DR 0.04 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(11500, 0.04, 0.05, 5)} mill")
print(f"OE 11,500 mill DR 0.04 YOY 0.08 duration 5y networth {present_value_of_future_cash_flows(11500, 0.04, 0.08, 5)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0 duration 5y networth {present_value_of_future_cash_flows(11500, 0.05, 0, 5)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0 duration 10y networth {present_value_of_future_cash_flows(11500, 0.05, 0, 10)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0 duration 30y networth {present_value_of_future_cash_flows(11500, 0.05, 0, 30)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0 duration 100y networth {present_value_of_future_cash_flows(11500, 0.05, 0, 100)} mill")

print(f"OE 14541 mill DR 0.0094 YOY 0.59 duration 10y networth {present_value_of_future_cash_flows(14541, 0.0094, 0.59, 10)} mill")

print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 5)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 10y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 10)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 30y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 30)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 100y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 100)} mill")

print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 5)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 10y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 10)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 30y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 30)} mill")
print(f"OE 11,500 mill DR 0.05 YOY 0.05 duration 100y networth {present_value_of_future_cash_flows(11500, 0.05, 0.05, 100)} mill")


print(f"OE 33364 mill DR 0.04 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(33364, 0.04, 0.05, 5)} mill")
print(f"OE 33364 mill DR 0.04 YOY 0.83 duration 5y networth {present_value_of_future_cash_flows(33364, 0.04, 0.83, 5)} mill")
print(f"OE 33364 mill DR 0.04 YOY 0.05 duration 10y networth {present_value_of_future_cash_flows(33364, 0.04, 0.05, 10)} mill")
print(f"OE 33364 mill DR 0.04 YOY 0.05 duration 30y networth {present_value_of_future_cash_flows(33364, 0.04, 0.05, 30)} mill")
print(f"OE 33364 mill DR 0.04 YOY 0.05 duration 100y networth {present_value_of_future_cash_flows(33364, 0.04, 0.05, 100)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(33364, 0.05, 0.05, 5)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.83 duration 5y networth {present_value_of_future_cash_flows(33364, 0.05, 0.83, 5)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.05 duration 10y networth {present_value_of_future_cash_flows(33364, 0.05, 0.05, 10)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.05 duration 30y networth {present_value_of_future_cash_flows(33364, 0.05, 0.05, 30)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.05 duration 100y networth {present_value_of_future_cash_flows(33364, 0.05, 0.05, 100)} mill")

print(f"OE 33364 mill DR 0.05 YOY 0.08 duration 5y networth {present_value_of_future_cash_flows(33364, 0.05, 0.08, 5)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.08 duration 10y networth {present_value_of_future_cash_flows(33364, 0.05, 0.08, 10)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.08 duration 30y networth {present_value_of_future_cash_flows(33364, 0.05, 0.08, 30)} mill")
print(f"OE 33364 mill DR 0.0356 YOY 0.065 duration 5y networth {present_value_of_future_cash_flows(33364, 0.0356, 0.05, 5)} mill")
print(f"OE 33364 mill DR 0.05 YOY 0.08 duration 100y networth {present_value_of_future_cash_flows(33364, 0.05, 0.08, 100)} mill")
print(f"OE 33364 mill DR 0.0356 YOY 0.05 duration 5y networth {present_value_of_future_cash_flows(33364, 0.0356, 0.05, 5)} mill")
print(f"OE 33364 mill DR 0.0356 YOY 0.83 duration 5y networth {present_value_of_future_cash_flows(33364, 0.0356, 0.83, 5)} mill")
print(f"OE 33364 mill DR 0.0348 YOY 0.05 duration 10y networth {present_value_of_future_cash_flows(33364, 0.0348, 0.5, 10)} mill")
print(f"OE 33364 mill DR 0.0366 YOY 0.05 duration 30y networth {present_value_of_future_cash_flows(33364, 0.0366, 0.05, 30)} mill")



print(f"duration 30 growth 0%: {check_earnings_for_valuation(20000, 0.05, 0, 30)} mill")
print(f"duration 30 growth 2%: {check_earnings_for_valuation(20000, 0.05, 0.02, 30)} mill")
print(f"duration 30 growth 4%: {check_earnings_for_valuation(20000, 0.05, 0.04, 30)} mill")
print(f"duration 30 growth 6%: {check_earnings_for_valuation(20000, 0.05, 0.06, 30)} mill")
print(f"duration 30 growth 8%: {check_earnings_for_valuation(20000, 0.05, 0.08, 30)} mill")
print(f"duration 30 growth 10%: {check_earnings_for_valuation(20000, 0.05, 0.10, 30)} mill")

#print(f"OE 250 mill DR 0.05 YOY 10 duration 2y networth {present_value_of_future_cash_flows(250, 0.05, 0.02, 2)} mill")







