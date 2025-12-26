def calculate_due_amount(total_bill, amount_paid):
    """
    Calculates the remaining due amount.
    Handles cases where payment exceeds the total bill (returning 0).
    """
    if amount_paid >= total_bill:
        return 0.0
    else:
        return total_bill - amount_paid

# --- Example Usage ---
initial_bill = 150.75
payment = 100.00

due = calculate_due_amount(initial_bill, payment)

print(f"Total Bill Amount: ${initial_bill:.2f}")
print(f"Amount Paid: ${payment:.2f}")
print(f"Remaining Due Amount: ${due:.2f}")

# Another example where payment covers the bill
initial_bill_2 = 50.00
payment_2 = 60.00 # Overpayment
due_2 = calculate_due_amount(initial_bill_2, payment_2)
print(f"\nTotal Bill Amount: ${initial_bill_2:.2f}, Amount Paid: ${payment_2:.2f}, Remaining Due: ${due_2:.2f}")