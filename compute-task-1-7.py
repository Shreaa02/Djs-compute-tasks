import re
test_ids = ["ABC1234", "sbaz56", "Wuy1452", "TYP9006", "KZED439"]
vi =[]
for i in test_ids:
    if len(i) ==7 and re.search(r"\b[A-Z][A-Z][A-Z]",i) and re.search(r"[0-9][0-9][0-9][0-9]\b",i):
        vi.append(i)
print(f"Valid IDs= {vi}")