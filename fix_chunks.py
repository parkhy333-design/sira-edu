import json

with open("data/index/chunks.jsonl", "r", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]

for row in rows:
    row["text"] = row["text"].replace("\x00", " ")

with open("data/index/chunks.jsonl", "w", encoding="utf-8") as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print("완료")
