
# Income Tax Calculator (New Tax Regime)
# Beginner Python Project

STANDARD_DEDUCTION = 75000
CESS_RATE = 0.04

def line():
    print("=" * 60)

def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative.")
            else:
                return value
        except ValueError:
            print("Enter a valid number.")

def personal_details():
    line()
    print("PERSONAL DETAILS")
    line()
    name = input("Name: ")
    age = int(input("Age: "))
    pan = input("PAN Number: ").upper()
    return name, age, pan

def income_details():
    line()
    print("INCOME DETAILS")
    line()

    salary = get_amount("Salary Income (₹): ")
    business = get_amount("Business Income (₹): ")
    property_income = get_amount("House Property Income (₹): ")
    capital = get_amount("Capital Gains (₹): ")
    interest = get_amount("Interest Income (₹): ")
    other = get_amount("Other Income (₹): ")

    gross = (
        salary
        + business
        + property_income
        + capital
        + interest
        + other
    )

    deduction = STANDARD_DEDUCTION if salary > 0 else 0

    taxable = max(0, gross - deduction)

    return {
        "salary": salary,
        "business": business,
        "property": property_income,
        "capital": capital,
        "interest": interest,
        "other": other,
        "gross": gross,
        "deduction": deduction,
        "taxable": taxable
    }

def calculate_tax(taxable):
    tax = 0

    slabs = [
        (400000, 0.00),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float("inf"), 0.30)
    ]

    previous = 0
    breakdown = []

    for limit, rate in slabs:
        if taxable > previous:
            amount = min(taxable, limit) - previous
            slab_tax = amount * rate
            tax += slab_tax
            breakdown.append((previous + 1, limit, rate * 100, slab_tax))
            previous = limit
        else:
            break

    rebate = 0
    if taxable <= 1200000:
        rebate = tax

    tax_after_rebate = max(0, tax - rebate)
    cess = tax_after_rebate * CESS_RATE
    total = tax_after_rebate + cess

    return {
        "tax": tax,
        "rebate": rebate,
        "cess": cess,
        "total": total,
        "monthly": total / 12,
        "breakdown": breakdown
    }

def tax_slabs():
    line()
    print("NEW TAX REGIME SLABS")
    line()
    print("0 - 4,00,000       : 0%")
    print("4,00,001 - 8,00,000: 5%")
    print("8,00,001 - 12,00,000:10%")
    print("12,00,001 - 16,00,000:15%")
    print("16,00,001 - 20,00,000:20%")
    print("20,00,001 - 24,00,000:25%")
    print("Above 24,00,000    :30%")

def report(name, age, pan, income, result):
    line()
    print("INCOME TAX REPORT")
    line()

    print(f"Name                 : {name}")
    print(f"Age                  : {age}")
    print(f"PAN                  : {pan}")

    line()

    print(f"Salary Income        : ₹{income['salary']:,.2f}")
    print(f"Business Income      : ₹{income['business']:,.2f}")
    print(f"House Property       : ₹{income['property']:,.2f}")
    print(f"Capital Gains        : ₹{income['capital']:,.2f}")
    print(f"Interest Income      : ₹{income['interest']:,.2f}")
    print(f"Other Income         : ₹{income['other']:,.2f}")

    line()

    print(f"Gross Income         : ₹{income['gross']:,.2f}")
    print(f"Standard Deduction   : ₹{income['deduction']:,.2f}")
    print(f"Taxable Income       : ₹{income['taxable']:,.2f}")

    line()
    print("SLAB-WISE TAX")
    for s, e, r, t in result["breakdown"]:
        end = "Above" if e == float("inf") else f"{int(e):,}"
        print(f"{s:,} - {end:>10} @ {r:>4.0f}% : ₹{t:,.2f}")

    line()
    print(f"Income Tax           : ₹{result['tax']:,.2f}")
    print(f"87A Rebate           : ₹{result['rebate']:,.2f}")
    print(f"Cess (4%)            : ₹{result['cess']:,.2f}")
    print(f"TOTAL TAX            : ₹{result['total']:,.2f}")
    print(f"Monthly Tax          : ₹{result['monthly']:,.2f}")

    if income["gross"] > 0:
        eff = result["total"] / income["gross"] * 100
    else:
        eff = 0

    print(f"Effective Tax Rate   : {eff:.2f}%")
    line()

def main():
    while True:
        line()
        print("INCOME TAX CALCULATOR - NEW TAX REGIME")
        line()
        print("1. Calculate Tax")
        print("2. View Tax Slabs")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name, age, pan = personal_details()
            income = income_details()
            result = calculate_tax(income["taxable"])
            report(name, age, pan, income, result)

        elif choice == "2":
            tax_slabs()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
