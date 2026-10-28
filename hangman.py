import re
def clean_phrase(x):
    cleaned = x.upper() 
    return re.sub("[^A-Z ]", "", cleaned)
print(clean_phrase("If it ain't broke, dont fix it."))

def redact_phrase(x, y):
    return re.sub(f"[^{y} ]", "-", x)
print(redact_phrase("IF IT AINT BROKE DONT FIX IT", ""))