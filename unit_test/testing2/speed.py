def speed_eval(speed):
    if speed < 0 or speed > 220:
        return "Invalid"
    if speed < 40:
        return "Low"
    if speed < 120:
        return "Normal"
    if speed < 200:
        return "High"
    return "V.High"