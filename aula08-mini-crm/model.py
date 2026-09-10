from datetime import date
def model_lead(name, email, company, step ):
    """estrutura um lead como um dicionário"""
    return {
        "nome": name,
        "email": email,
        "company": company,
        "step": step,
        "created": date.today().isoformat()
    }