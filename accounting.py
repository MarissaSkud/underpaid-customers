#Sets melon cost as constant global variable

MELON_COST = 1.00

def check_customer_payment(file_path):

  """Checks data file to see which customers have underpaid.

  Opens file of sales data, calculates expected payment & compares it to actual payment
  for each customer, prints statement if there is a discrepancy.
  """

  #open data file
  data_file = open(file_path)

  #strip out whitespace from file and tokenize each line
  for line in data_file:
    line = line.rstrip()
    data = line.split('|')

    #set the relevant tokenized strings to variables and convert to int or float if needed
    name = data[1]
    melons = int(data[2])
    paid = float(data[3])

    #calculate the expected price based on number of melons sold & melon cost
    customer_expected = melons * MELON_COST

    #compare expected price to actual payment and, if discrepancy, print statement
    #of actual vs expected payment.

    if customer_expected != paid:
      if customer_expected > paid:
        payment_problem = "UNDERPAYMENT"
      elif customer_expected < paid:
        payment_problem = "OVERPAYMENT"

      print(f"{payment_problem}! {name} paid ${paid:.2f},", 
      f"expected ${customer_expected:.2f}")

  data_file.close()

check_customer_payment("customer-orders.txt")

#Note: solution suggests further tokenizing name into first name & last name, but I think this
#is unnecessary/impractical: there are multiple "Pamela"s in the list, for instance, so
#it is no good to get back "Pamela paid $1.46, expected $5.00"; much better to have 
#"Pamela Mills paid $1.46, expected $5.00"

#lots of underpayments & no overpayments! BAD SIGN FOR UBERMELON.

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
