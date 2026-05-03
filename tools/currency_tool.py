# def currency_converter(amount, rate=83):
#     converted = amount * rate
#     return f"{amount} USD is approximately {converted} INR"

def currency_converter(amount, rate=83, from_curr="USD", to_curr="INR"):
    converted = amount * rate
    return f"{amount} {from_curr} ≈ {converted} {to_curr}"