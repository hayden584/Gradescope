
chosen_currency = int(input("Choose to convert to 1. EUR 2. GBP 3. CNY 4. INR:"))
USD = input("Enter dollar amount to exchange: ")

cleaned_USD = USD.replace("$", "")
amount = float(cleaned_USD)

USD_after_fee = amount * .95

if chosen_currency == 1:
    converted_amount = USD_after_fee / 1.08
    print("After fees you will receive EUR", round(converted_amount))
elif chosen_currency == 2:
    converted_amount = USD_after_fee / 1.21
    print("After fees you will receive GBP", round(converted_amount))
elif chosen_currency == 3:
    converted_amount = USD_after_fee / 0.15
    print("After fees you will receive CNY", round(converted_amount))
elif chosen_currency == 4:
    converted_amount = USD_after_fee / 0.012
    print("After fees you will receive INR", round(converted_amount))
