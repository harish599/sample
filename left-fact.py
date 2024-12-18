def left_factoring(s):
    alphabetset = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start, rules = s.replace(" ", "").split("->")
    rules = rules.split("|")

    grouped = {}
    for rule in rules:
        grouped.setdefault(rule[0], []).append(rule)

    for key, rule_list in grouped.items():
        common_prefix = ''.join(c[0] for c in zip(*rule_list) if len(set(c)) == 1)
        if common_prefix:
            new_non_terminal = alphabetset.pop(0)
            print(f"{start}->{common_prefix}{new_non_terminal}")
            suffixes = [rule[len(common_prefix):] or "ε" for rule in rule_list]
            print(f"{new_non_terminal}->" + " | ".join(suffixes))

    remaining = [rule for rule in rules if rule[0] not in grouped]
    for rule in remaining:
        print(f"{start}->{rule}")

s = "A -> aB | aC | bD"
left_factoring(s)