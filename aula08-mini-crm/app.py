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
    print("\nLista de leads:")
    for lead in leads:
        print(f"\n Nome: {lead['nome']},\n Email: {lead['email']},\n Empresa: {lead['company']},\n Etapa: {lead['step']},\n Criado em: {lead['created']}")

def main():
    while True:
            print("\nMini CRM de Leads")
            print("[1] Adicionar lead")
            print("[2] listar leads")
            print("[0] Sair")

            opt = input("Escolha uma opção: ")

            if opt == "1":
                add_lead()

            elif opt == "2":
                list_leads()

            elif opt == "0":
                print("Saindo...")
                break
            else: 
                print("Opção inválida.")
if __name__ == "__main__":
    main()