status_code = int(input("Enter the status code of your API endpoint: "))

match status_code:
    case 200:
        print("Request was successful.")
    case 404:
        print("Resource not found.")
    case _:
        print("Unknown status code.")
