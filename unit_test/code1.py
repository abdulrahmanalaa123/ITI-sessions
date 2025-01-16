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
def score_eval(score):
    if score < 0 or score > 100:
        return "Invalid"
    if score < 50:
        return "Failed"
    if score < 65:
        return "Passed"
    if score < 75:
        return "Good"
    if score < 85:
        return "V.Good"
    return "Excellent"