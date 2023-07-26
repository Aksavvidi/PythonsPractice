from functools import reduce

quarters = ["A", "B", "C", "D"]
prices = [1000, 2000, 1800, 1500]

sales = (dict(zip(quarters, prices)))

# print(sales)    #{'A': 1000, 'B': 2000, 'C': 1800, 'D': 1500}

# Traverse a dictionary
for key, value in sales.items():
    print(key, ":", value)
"""
Print (key, ":", value)
A : 1000
B : 2000
C : 1800
D : 1500
"""
filtered_sales = dict(filter(lambda quarter_tuple: quarter_tuple[1] >= 1500, sales.items()))

print("Filtered sales: ", filtered_sales)  #Filtered sales:  {'B': 2000, 'C': 1800, 'D': 1500}

quarters_tax = {key : value *0.2 for key, value in sales.items()}

print("Quarters tax: ", quarters_tax) # Quarters tax:  {'A': 200.0, 'B': 400.0, 'C': 360.0, 'D': 300.0}

total_years_sale = reduce(lambda x,y : x + y, sales.values())
print("Total years sales:", total_years_sale)  # Total years sales: 6300