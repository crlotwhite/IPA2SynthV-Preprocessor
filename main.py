import csv,json

res = {
    "IPA": [],
    "JPN": [],
    "ENG": [],
    "MAN": [],
}

with open('./IPA2SynthV.csv', encoding='utf-8') as f:
    # Example ['vowel', 'diphthong', 'ㅢ', 'xi', 'wi', '', '']
    rdr = csv.reader(f)
    next(rdr)
    for row in rdr:
        res["IPA"].append(row[3])
        res["JPN"].append(row[4])

with open("./output.json", 'w', encoding='utf-8') as file:
    json.dump(res, file, indent="\t", ensure_ascii=False)