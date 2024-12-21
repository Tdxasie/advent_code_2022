import re

with open('input.txt', 'r') as infile:
    text = infile.read()
    
rule_pat = r"(?P<X>\d\d)\|(?P<Y>\d\d)"
updt_pat = r"(?P<update>\d\d,.*)"

rule_re = re.compile(rule_pat)
updt_re = re.compile(updt_pat)

rules = [m.groupdict() for m in rule_re.finditer(text)]
updts = [m.groupdict() for m in updt_re.finditer(text)]


rules_dict = {}
for rule in rules:
    X = int(rule["X"])
    Y = int(rule["Y"]) 
    if Y not in rules_dict:
        rules_dict[Y] = [X]
    else:
        rules_dict[Y].append(X)

print(rules_dict[53])

tot = 0
for upd in updts:
    pages = [int(i) for i in upd["update"].split(",")]
    
    safe = True
    for i, page in enumerate(pages):
        next_pages = pages[i+1:]
        forbidden_pages = rules_dict.get(page)
        if forbidden_pages is None:
            continue
        for forbidden_page in forbidden_pages:
            safe &= forbidden_page not in next_pages
    
    if safe:
        tot += pages[int(len(pages)/2)]

print(tot)

