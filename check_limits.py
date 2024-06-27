
def battery_is_ok(temperature, soc, ch_rate):
  return (temp_check(temperature) and soc_check(soc) and charge_rate_check(ch_rate)):
  
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
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)

  
