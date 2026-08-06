endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
endpoint_quantity_erros = [0, 0, 0]
endpoint_quantity_sucessos = [0, 0, 0]
for i in range(len(endpoints)):
    print(f"Endpoint: {endpoints[i]}")
    previous_was_error = False 
    for j in range(len(status[i])):
        current_is_error = False 
        print(f"Status code: {status[i][j]}")
        if status[i][j] < 299:
            print("Sucesso")
            endpoint_quantity_sucessos[i] += 1
            current_is_error = False
        else: 
            print("Falha")
            endpoint_quantity_erros[i] += 1
            current_is_error = True

   
        if current_is_error and previous_was_error:
            print(f" Dois erros consecutivos detectados para o endpoint {endpoints[i]}!")
        
       
        previous_was_error = current_is_error
    print(f"Quantidade de erros: {endpoint_quantity_erros[i]}")
    print(f"Quantidade de sucessos: {endpoint_quantity_sucessos[i]}")
    print()

    total_requests = endpoint_quantity_erros[i] + endpoint_quantity_sucessos[i]
    if total_requests > 0:
        percentage_success = (endpoint_quantity_sucessos[i] / total_requests) * 100
        print(f"Porcentagem de sucesso: {percentage_success:.2f}%")
    print()
    if percentage_success > 80:
        print(f"estavel")
    if percentage_success < 80:
        print(f"instavel")




if endpoint_quantity_erros[0] > endpoint_quantity_erros[1] and endpoint_quantity_erros[0] > endpoint_quantity_erros[2]:
    print(f"O endpoint com mais erros é: {endpoints[0]} com {endpoint_quantity_erros[0]} erros")
if endpoint_quantity_erros[1] > endpoint_quantity_erros[0] and endpoint_quantity_erros[1] > endpoint_quantity_erros[2]:
    print(f"O endpoint com mais erros é: {endpoints[1]} com {endpoint_quantity_erros[1]} erros")
if endpoint_quantity_erros[2] > endpoint_quantity_erros[0] and endpoint_quantity_erros[2] > endpoint_quantity_erros[1]:
    print(f"O endpoint com mais erros é: {endpoints[2]} com {endpoint_quantity_erros[2]} erros")