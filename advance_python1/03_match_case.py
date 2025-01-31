'''
def https_Status(Status):
    match Status:
        case 200:
            return "Working"
        case 404:
            return "Error"
        case 500:
            return "Unknown Error"
        case _:
            return "Unknown Status"

print(https_Status(200))

'''

find = int(input("Enter the number here: "))

def https_status(find):
    match find:
        case 404:
            return "Working"
        case 505:
            return "Unexpected Error"
        case 999:
            return "Internet Problem"
        case _:
            return "Syntex Error"
        
print(https_status(find))