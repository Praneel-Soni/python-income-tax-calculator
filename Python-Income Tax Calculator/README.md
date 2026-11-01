# Income Tax Calculator – New Tax Regime

A beginner-friendly Python command-line project that estimates income tax using the tax-slab logic implemented in this program.

## Project Overview

This application collects basic personal details and different categories of income, calculates gross and taxable income, applies the configured tax slabs, and displays an income tax report with a slab-wise breakdown.

## Features

- Collects name, age and PAN number.
- Accepts salary, business, house-property, capital-gains, interest and other income.
- Prevents negative income amounts and asks again when a non-numeric amount is entered.
- Applies a standard deduction of ₹75,000 when salary income is greater than zero.
- Calculates tax using the slab rates configured in the program.
- Applies the program's 87A rebate logic for taxable income up to ₹12,00,000.
- Calculates 4% cess and displays total and monthly estimated tax.
- Provides an option to view the configured tax slabs.

## Tax Slabs Configured in the Program

| Taxable income slab | Rate |
|---|---:|
| Up to ₹4,00,000 | 0% |
| ₹4,00,001 – ₹8,00,000 | 5% |
| ₹8,00,001 – ₹12,00,000 | 10% |
| ₹12,00,001 – ₹16,00,000 | 15% |
| ₹16,00,001 – ₹20,00,000 | 20% |
| ₹20,00,001 – ₹24,00,000 | 25% |
| Above ₹24,00,000 | 30% |

## Technologies and Python Concepts Used

- Python 3
- Variables and constants
- Functions
- `while` and `for` loops
- Conditional statements (`if`, `elif`, `else`)
- Lists and tuples
- Dictionaries
- User input and output
- Exception handling (`try` / `except`)
- Formatted strings

## Project Structure

```text
income-tax-calculator/
├── income_tax_calculator_new_regime.py
└── README.md
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python income_tax_calculator_new_regime.py
```

On some systems, use:

```bash
python3 income_tax_calculator_new_regime.py
```

## How to Use

1. Choose **1. Calculate Tax** to enter personal and income details.
2. Enter the requested income amounts.
3. Review the generated income tax report.
4. Choose **2. View Tax Slabs** to see the rates configured in the program.
5. Choose **3. Exit** to close the application.

## Academic Project

Developed as a Diploma academic project to practise Python programming, functions, conditional logic, loops, input validation and basic calculations.

## Important Note

This is an educational project. The tax slabs, deduction, rebate and calculation approach are hard-coded examples in the program and may not reflect the tax law applicable to a particular financial year or every taxpayer's circumstances. The program applies the same slab calculation to the income categories it collects and does not separately handle special tax rates or all tax-law rules. Do not use its output for actual tax filing or financial decisions. Verify current rules with official tax resources or a qualified tax professional.
