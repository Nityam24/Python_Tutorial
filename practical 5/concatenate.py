#Write a script to concatenate given dictionaries.
d1={'vicky':23,'kat':34,'nat':21}
d2={'alex':39,'john':49,'tom':63}

for key,value in d1.items():
    d2[key]=value
print(d2)