def test_valid_ticket(): 
  assert validate_ticket("TK674269") = True

def test_invalid_ticket(): 
  assert validate_ticket("42") = False

# def test_if_ticket_is_string(): 
# assert validate_ticket 

def test_general_ticket
  assert get_ticket_tier("TK159841") = "General" 

def test_VIP_ticket
  assert get_ticket_tier("TK459841") = "VIP" 

def test_Platinum_ticket
  assert get_ticket_tier("TK759841") = "Platinum" 

