import re
def check_password_strength(password):
    score= 0
    suggestion = []
    if len(password) >= 8:
        score +=1
    else:
        suggestion.append("use atleast a characters")
    if re.search ()
