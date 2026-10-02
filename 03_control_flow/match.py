# Python 3.10+ match-case (In JS: switch statement)
# Note: No 'break' needed! No fall-through bugs!

def get_status_message(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 401 | 403:       # Match multiple with |
            return "Auth Error"
        case 404:
            return "Not Found"
        case _:               # In JS: default
            return "Unknown Error"

print("200:", get_status_message(200))
print("403:", get_status_message(403))
print("500:", get_status_message(500))
