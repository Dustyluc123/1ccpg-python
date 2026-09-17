from pathlib import Path
import json
import csv
DATA_DIR = Path(__file__).resolve().parent
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"
#READ
def read_leads():
    if not DB_PATH.exists():
        return []
    try: 
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
#CREATE
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads,ensure_ascii=False ,indent=2), encoding="utf-8")

#EXPORT lEADS COMO CSV
def  export_csv():
    
    path_csv = DATA_DIR/"leads.csv"
    leads = read_leads() # LISTA - ARRAY!!

    try: 
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    
    except PermissionError:
        print("Erro: Permissão negada ao criar o arquivo CSV.")
        return None
# READ LEADS FROM QUERY/SEARCH
def read_leads_seach(query):
    leads = read_leads()
    results = []
    for i, lead in enumerate(leads):
        txt_lead = f"{lead['nome']} {lead['email']} {lead['company']}".lower()
        #print(txt_lead)
        if query in txt_lead:
            results.append((i, lead)) # (0, {"name": "John"...})

    return results
print(read_leads_seach("lucas")) 