"""
Word Occurrences
Estimate: 20 minutes
Actual:   36 minutes
"""


def extract_name_from_email(email):
    """Extract name from an email address before the '@'."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

email_to_name = {}

email = input("Email: ").strip()
while email != "":
    extracted_name = extract_name_from_email(email)
    confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

    if confirmation in ["", "y"]:
        name = extracted_name
    else:
        name = input("Name: ").strip()

    email_to_name[email] = name
    email = input("Email: ").strip()

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")
