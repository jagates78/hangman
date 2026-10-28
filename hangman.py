import re
def clean_phrase(x):
    cleaned = x.upper() 
    return re.sub("[^A-Z ]", "", cleaned)
print(clean_phrase("If it ain't broke, dont fix it."))