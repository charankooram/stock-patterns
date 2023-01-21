def present_value_of_future_cash_flows(operating_income, discount_rate, earnings_increase_yoy, duration):
    valuation = 0
    for d in range(duration+1):
        valuation += (operating_income)*pow(1 + earnings_increase_yoy, d)/pow(1+discount_rate, d)
        #print(f"d {d} value {valuation}")
    return valuation
    
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





