# ticket_validator.py -- start with stubs, no logic

def validate_ticket(code):
    if not(type(code) == str):
        raise TypeError
    if len(code) == 8:
        if code[0:2] == "TK":
            return True
    
                        
def get_ticket_tier(code):
    try:
        if validate_ticket(code):
            if code[2] in "123": 
                return "General"
            if code[2] in "456": 
                return "VIP"
            if code[2] in "789": 
                return "Platinum"
    except ValueError:
        pass

def calculate_total(prices, discount=0):
    pass
