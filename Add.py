def error():  
  return False

def add_sign_to_board(num, signs, startingP):  
  match(num):
    case b'7':
      if signs[0] == " ":
        signs[0:1] = startingP
        return True        
      else:
        error()
    case b'8':
      if signs[1] == " ":
        signs[1:2] = startingP
        return True
      else:
        error()        
    case b'9':
      if signs[2] == " ":
        signs[2:3] = startingP
        return True
      else:
        error()
    case b'4':
      if signs[3] == " ":
        signs[3:4] = startingP
        return True
      else:
        error()
    case b'5':
      if signs[4] == " ":
        signs[4:5] = startingP
        return True
      else:
        error()
    case b'6':
      if signs[5] == " ":
        signs[5:6] = startingP
        return True
      else:
        error()
    case b'1':
      if signs[6] == " ":
        signs[6:7] = startingP
        return True
      else:
        error()
    case b'2':
      if signs[7] == " ":
        signs[7:8] = startingP
        return True
      else:
        error()
    case b'3':
      if signs[8] == " ":
        signs[8:9] = startingP
        return True