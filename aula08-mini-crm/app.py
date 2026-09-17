from model import model_lead
import control
def add_lead():
    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    company = input("Digite a empresa: ")
    step = input("Digite a etapa(novo, em andamento, fechado): ")

    # validar as entradas do usuario 
    #depois de validar vamos modelar os dados
    print(model_lead(name, email, company, step))
    print("\nAdicionar lead")
    #depois de modelados vamos enviar esse dict(leads) para o leads.json
    #para salvar, vamos usar o modulo control
    control.create_lead(model_lead(name, email, company, step))
def list_leads():

    leads = control.read_leads()
    if not leads:
        print("Nenhum lead encontrado.")
        return
    
    print(f"## | {'Nome ':<10} | {'Email':<10} | {'Empresa':<10} ")

    for i, lead in enumerate(leads):
        print(f"{i:0d} | {lead['nome']:<10} | {lead['email']:<10} | {lead['company']:<10}")

def screach_leads():
    print("\nBuscar leads")

    query = input("Buscar por:").strip().lower()
    if not query:
        print("Nenhum termo de busca fornecido.")
        return

    #Envia a query para o controul realizar a busca no leads.json

    lead_finded = control.read_leads_seach(query)
    if not lead_finded:
        print("Nenhum lead encontrado.")
        return

    print(f"##| {'Nome ':<10} | {'Email':<10} | {'Empresa':<10} ")
    for i, lead in lead_finded:
        print(f"{i:0d} | {lead['nome']:<10} | {lead['email']:<10} | {lead['company']:<10}")

def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Erro ao exportar leads para CSV.")
    else:
        print(f"Leads exportados para CSV com sucesso: {path_csv}")

def main():
    while True:
            print("\nMini CRM de Leads")
            print("[1] Adicionar lead")
            print("[2] listar leads")
            print("[3] Buscar leads (nome/email/empresa)")
            print("[4] Exportar para CSV")
            print("[0] Sair")

            opt = input("Escolha uma opção: ")

            if opt == "1":
                add_lead()

            elif opt == "2":
                list_leads()
            elif opt == "3":
                screach_leads()
            elif opt == "4":
                export_leads()

            elif opt == "0":
                print("Saindo...")
                break
            else: 
                print("Opção inválida.")
if __name__ == "__main__":
    main()