import ticket_validator

def test_valid_ticket(): 
  assert ticket_validator.validate_ticket("TK674269") == True

def test_invalid_ticket(): 
  assert validate_ticket("42") == False

def test_general_ticket():
  assert ticket_validator.get_ticket_tier("TK159841") == "General" 

def test_VIP_ticket():
  assert ticket_validator.get_ticket_tier("TK459841") == "VIP" 

def test_Platinum_ticket():
  assert ticket_validator.get_ticket_tier("TK759841") == "Platinum" 

def test_too_much_discount():
  assert calculate_total(10, 1.1) == ValueError

def test_negative_discount(): 
  assert calculate_total(10, -0.5) == ValueError

def test_if_price_is_list(): 
  assert calculate_total == list == True
