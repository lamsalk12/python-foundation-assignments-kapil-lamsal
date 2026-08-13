raw_name = "  sAgar THAPA "

raw_city = "kATHMANDU "

raw_age = "27"

raw_email = " SAGAR@MAIL.COM "

clean_name = raw_name.strip().title()

clean_city = raw_city.strip().title()

clean_age = int(raw_age.strip())

clean_email = raw_email.strip().lower()

status = "Adult" if clean_age >= 18 else "Minor"

print(f"Name: {clean_name}")

print(f"City: {clean_city}")

print(f"Age: {clean_age}")

print(f"Email: {clean_email}")

print(f"Status: {status}")
