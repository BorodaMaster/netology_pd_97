from datetime import datetime

from application.db.people import get_employees
from application.salary import calculate_salary
from helperss.search import get_address

data = {
  "people": [
    {"address": ["123 Main St", "California", "US"]},
    {"address": ["345 Alt St", "Alaska", "US"]},
  ]
}

if __name__ == '__main__':
    # Print current time
    print(datetime.today())

    # Call functions from module
    calculate_salary()
    get_employees()

    # Get addresses
    addresses = get_address(data)

    for address in addresses:
        print("Street: {}, State: {}".format(address[0], address[1]))
