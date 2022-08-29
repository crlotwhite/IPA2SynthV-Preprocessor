import csv,json

res = {
    "JPN": {},
    "ENG": {},
    "MAN": {},
}

with open('./IPA2SynthV.csv', encoding='utf-8') as f:
    # Example ['vowel', 'diphthong', 'ㅢ', 'xi', 'wi', '', '']
    rdr = csv.reader(f)
    for row in rdr:
        res["JPN"].update({row[3]: row[4]})

with open("./output.json", 'w', encoding='utf-8') as file:
    json.dump(res, file, indent="\t", ensure_ascii=False)