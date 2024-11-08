def access_control(user_role, department):
    match user_role, department:
        case 'Admin', _:
            return "Full access to all departments"
        case 'Manager', 'Sales':
            return "Access to sales data only"
        case 'Manager', 'HR':
            return "Access to HR data only"
        case 'Employee', _:
            return "Limited access to own data only"
        case _:
            return "No access granted"

# Example usage
print(access_control('Manager', 'Sales'))  # Output: Access to sales data only


def process_payment(method, country):
    match method, country:
        case 'Credit Card', 'US':
            return "Processing via US credit gateway"
        case 'Credit Card', 'EU':
            return "Processing via EU credit gateway"
        case 'PayPal', _:
            return "Processing via PayPal"
        case 'Bank Transfer', 'US':
            return "Processing via US bank network"
        case 'Bank Transfer', 'EU':
            return "Processing via EU bank network"
        case _:
            return "Payment method not supported"

# Example usage
print(process_payment('Credit Card', 'US'))  # Output: Processing via US credit gateway


