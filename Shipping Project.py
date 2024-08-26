"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost += shipping_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))
# The flag is: THM{IF_STATEMENT_SHOPPING}



# In shipping.py, on line 13 (when using the Code Editor's Hint), change the customer_basket_cost variable to 101 and re-run your code. 
# You will get a flag (if the total cost is correct based on your code); the flag is the answer to this question.
shipping_cost_per_kg = 1.20
customer_basket_cost = 101
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost += shipping_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))
# The flag is: THM{MY_FIRST_APP}

