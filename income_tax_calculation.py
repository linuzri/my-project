tax_payable = 0
# income = 45000
income = int(input("Your Income : "))

if income <= 10000:
    tax_payable = 0

elif income <= 20000:
    # 1st 10000 is 0%
    tax_payable =0

    # next 10000 is 10%
    x = income - 10000
    tax_payable += (x * 10) / 100

else:
    # first 10000 is 0%
    tax_payable = 0

    # next 10000 is 10%
    tax_payable += (10000 * 10) / 100

    # remaining is 20%
    tax_payable += (income - 20000) * 20 / 100

print(f"Your Tax : {tax_payable}")
