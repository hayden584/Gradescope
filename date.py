
current_date = input("Enter the date in US format (MM/DD/YY):")
month, day, year = current_date.split("/")
date_in_ISO_format = "20" + year + "-" + month + "-" + day

print("The date in ISO 8601 extended format is:", date_in_ISO_format)