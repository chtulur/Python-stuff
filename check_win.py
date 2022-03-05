def check_for_win(signs, startP):
  a, b, c, *d = signs
  *e, f, g, h = signs
  
  #Top Row
  if a == startP and b == startP and c == startP:    
    return True
  #Last Row
  elif f == startP and g == startP and h == startP:
    return True
  #Middle Row
  elif signs[3] == startP and signs[4] == startP and signs[5] == startP:
    return True
  #Left Col
  elif signs[0] == startP and signs[3] == startP and signs[6] == startP:
    return True
  #Mid Col
  elif signs[1] == startP and signs[4] == startP and signs[7] == startP:
    return True
  #Right Col
  elif signs[2] == startP and signs[5] == startP and signs[8] == startP:
    return True
  #\ diagonal
  elif signs[0] == startP and signs[4] == startP and signs[8] == startP:
    return True
  #/ diagonal
  elif signs[2] == startP and signs[4] == startP and signs[6] == startP:
    return True
  else:
    return False