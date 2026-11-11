def mask_card_number(number):
    if not isinstance(number, str):
        return "Invalid card number"
    digits = number.replace(' ', '').replace('-', '')
    if len(digits) < 4:
        return "Invalid card number"
    return '*' * (len(digits) - 4) + digits[-4:]

def parse_transaction(line):
    if not isinstance(line, str):
        return ("Invalid transaction", 0)
    parts = line.split(',')
    if len(parts) != 3:
        return ("Invalid transaction", 0)
    category = parts[1].strip()
    amount = parts[2].strip()
    if not category or not amount:
        return ("Invalid transaction", 0)
    try:
        amount = int(amount)
    except ValueError:
        return ("Invalid transaction", 0)
    return category.lower(), amount

def parse_statement_total(text):
    if not isinstance(text, str) or ':' not in text:
        return 0
    amount = text.split(':', 1)[1].strip()
    try:
        return int(amount.replace(',', ''))
    except ValueError:
        return 0

def main():
    print("==== Running mask_card_number ====")
    value = input("Enter a card number (e.g. 4111 1111 1111 1234): ")
    print("Masked card number:", mask_card_number(value))

    print("\n==== Running parse_transaction ====")
    value = input("Enter a transaction as DATE,CATEGORY,AMOUNT (e.g. 2026-11-05,dining,1550): ")
    print("Category and amount:", parse_transaction(value))

    print("\n==== Running parse_statement_total ====")
    value = input("Enter the statement total line (e.g. Total: 12,500): ")
    print("Statement total:", parse_statement_total(value))

if __name__ == "__main__":
    main()
