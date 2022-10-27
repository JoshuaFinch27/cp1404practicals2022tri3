"""
CP1404 - Practical 5
Program that: Stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.
"""


def main():
    """Create dictionary that stores users emails and names"""
    email_details = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name_from_email(email)
        confirm_name = input(f"Is your name {full_name}? (Y/N) ")
        if confirm_name.upper() != "Y" and confirm_name != "":
            full_name = input("Name: ")
        email_details[email] = full_name
        email = input("Email: ")
        print(email_details)

    for email, full_name in email_details.items():
        print(f"{full_name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address"""
    email_prefix = email.split("@")[0]
    name_parts = email_prefix.split(".")
    full_name = " ".join(name_parts).title()
    return full_name


main()
