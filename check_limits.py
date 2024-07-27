
def battery_is_ok(temperature, soc, ch_rate):
  temp_check(temperature)
  soc_check(soc)
  charge_rate_check(ch_rate)
  
def temp_check(temp):
  if temp < 0 or temp > 45:
    print('Temperature is out of range!')
    return False
  else: return True
    
def soc_check(soc):
  if soc <=20 or soc > 80:
    low_high_soc(soc)
  else:
    check_soc(soc)

def low_high_soc(soc):
  if soc<20:
    print('State of Charge is LOW BREACH')
  else:
    print('State of Charge is HIGH BREACH')

def check_soc(soc):
  if soc <25 or soc >75:
    warning_check(soc)
  else:
    print('State of Charge is NORMAL')

def warning_check(soc):
  if soc <25:
    print('State of Charge is LOW WARNING')
  else:
    print('State of Charge is HIGH WARNING')
    
def charge_rate_check(ch):
  if ch > 0.8:
    print('Charge rate is out of range!')
    return False
  else: return True
    
if __name__ == '__main__':
  battery_is_ok(25, 70, 0.7)
  battery_is_ok(50, 85, 0)

  
