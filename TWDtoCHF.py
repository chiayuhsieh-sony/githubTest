# Get the exchange rate from user input
exchange_rate = float(input("Enter the exchange rate from TWD to CHF: "))

# Get the amount in TWD to convert from user input
amount_twd = float(input("Enter the amount in TWD: "))

# Perform the conversion
amount_chf = amount_twd * exchange_rate

# Display the result
print(f"{amount_twd} TWD is equal to {amount_chf} CHF")