from pulp import *
import pulp

class Toy:
    def __init__(self, name, profit, prod_limit, packages):
        self.name = name
        self.profit = profit
        self.prod_limit = prod_limit
        self.packages = packages
        self.prod_count = LpVariable(f"Toy_Prod_Count_{name}", lowBound=0, upBound= prod_limit ,cat='Integer')

class Package:
    def __init__(self, products, profit):
        self.products = products
        min_prod_limit = min(product.prod_limit for product in products);
        self.profit = profit
        self.prod_count = LpVariable(f"Package_Prod_Count_{id(self)}", lowBound=0, upBound= min_prod_limit, cat='Integer')

def read_input():
    num_toys, num_packages, max_daily_production = map(int, input().split())

    products = []
    packages = []
  
    # Reads toys data
    for i in range(1, num_toys + 1):
        profit, capacity = input().split()
        toy = Toy(i, int(profit), int(capacity), [])
        products.append(toy)
        
    # Reads packages data
    for j in range(1, num_packages + 1):
        line = input().split()

        package_toys = list(map(int, line[:-1]))
        package_profit = int(line[-1])

        products_in_package = [products[idx - 1] for idx in package_toys]
        package = Package(products_in_package, package_profit)
        
        for toy in package_toys:
            products[toy-1].packages.append(package) 
        
        packages.append(package)

    return max_daily_production, products, packages

max_daily_production, products, packages = read_input()

prob = LpProblem("Ubiquity", LpMaximize)

total_production = 0
toy_production_profit = 0

# Toy production limit constraint
for toy in products:
    toy_production_profit += toy.profit * toy.prod_count 
    toy_p_prod_count = lpSum(package.prod_count for package in toy.packages)
    prob += toy.prod_count + toy_p_prod_count <= toy.prod_limit, f"Toy_Prod_Limit_{toy.name}"
    total_production += toy.prod_count + toy_p_prod_count
        
# Constraint to ensure that the total production does not exceed the daily limit
prob += total_production <= max_daily_production, "Daily_Production_Limit"

# Objective function
prob += toy_production_profit + lpSum(package.profit * package.prod_count for package in packages), "Total_Profit"

prob.solve(pulp.PULP_CBC_CMD(msg=0,timeLimit=0.04))

print(int(value(prob.objective)))

