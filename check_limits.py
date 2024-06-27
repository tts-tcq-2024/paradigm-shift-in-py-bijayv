
def battery_is_ok(temperature, soc, ch_rate):
  if temp_check(temperature) and soc_check(soc) and charge_rate_check(ch_rate):
    print(" Battery is OK")
  
def temp_check(temp):
  if temp < 0 or temp > 45:
    print('Temperature is out of range!')
    return False
  else: return True
    
def soc_check(soc):
  if soc <20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  else: return True
    
def charge_rate_check(ch):
  if ch > 0.8:
    print('Charge rate is out of range!')
    return False
  else: return True
    
if __name__ == '__main__':
  assert(battery_is_ok(35, 30, 0.6) is True)

  
