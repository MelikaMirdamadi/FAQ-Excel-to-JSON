import pandas as pd
import json
import os

dirname = os.path.dirname(__file__)

print(f"Running Dir : {dirname=}")
excel_file = f"{dirname}\\Export.xlsx"
df = pd.read_excel(excel_file, engine="openpyxl")


template = {"file_name": "FAQ", "languages": "eng+fas", "CHUNK__": None}

state = []

chunk_raw_size = 6
perv_faq = ""
for index_raw, (index, row) in enumerate(df.iterrows()):
    question = row["سوال"]
    answer = row["پاسخ"]

    perv_faq += f"\nQuestion : {question} -> Answer : {answer}" + "-" * 15
    if ((index_raw + 1) % chunk_raw_size) == 0:
        state.append(perv_faq.strip())
        perv_faq = ""
template["CHUNK__"] = list(set(state))
json_data = json.dumps(template, indent=4, ensure_ascii=False)

with open("faqs.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print("Successful")
