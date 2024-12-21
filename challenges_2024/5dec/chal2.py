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


def idx_to_swap(pages: list) -> tuple[int, int] | None:
    for i, page in enumerate(pages):
        next_pages = pages[i+1:]
        forbidden_pages = rules_dict.get(page)
        if forbidden_pages is None:
            continue
        for forbidden_page in forbidden_pages:
            if forbidden_page in next_pages:
                return i, pages.index(forbidden_page)
    return None


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

    if not safe:
        while not safe:
            if (vals := idx_to_swap(pages)):
                i, j = vals
                pages[i], pages[j] = pages[j], pages[i]
            else:
                safe = True
        
        
        tot += pages[int(len(pages)/2)]

print(tot)

