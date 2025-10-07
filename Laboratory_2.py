#Laboratory 2
#1
def format_phone_number(phone):
    cleaned = phone.replace(" ", "").replace("-", "")
    digits = ''.join(filter(str.isdigit, cleaned))
    formatted = f"({digits[:3]}){digits[3:6]}-{digits[6:]}"
    return formatted
print(format_phone_number("555-123-4567"))

#2
# item = "Book"
# price = 15.99
# quantity = 2

# print(f"{quantity} x {item} @ $ {price:.2f} ea. = ${price * quantity:.2f}")

#3
# def is_valid_username(username):
#     return username.isalnum() and 5 <= len(username) <= 12
# print(is_valid_username("user123"))
# print(is_valid_username("abc!"))
# print(is_valid_username("toolongusername123"))

#4
# def mask_credit_card(card_number):
#     digits = ''.join(filter(str.isdigit,card_number))
#     masked = '*' * (len(digits)- 4) + digits[-4:]
#     return masked
# print(mask_credit_card("1234567812345670"))