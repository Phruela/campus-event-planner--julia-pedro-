import json 
# O nome do arquivo que vamos usar como nossa "base de dados"
NOME_ARQUIVO = "dados_eventos.json"

def carregar_dados():
    try:
        # 'r' significa que estamos abrindo em modo de leitura
        with open(NOME_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(lista_eventos):
    # 'w' significa que estamos abrindo em modo pra escrever
    with open(NOME_ARQUIVO, 'w') as arquivo:
        json.dump(lista_eventos, arquivo, indent=4)

def adicionar_evento(lista_eventos):
    print("\n--- Adicionar Novo Evento ---")

    #ID que eu esqueci :)
    if not lista_eventos:
        novo_id = 1
    else: 
        ultimo_evento = lista_eventos[-1]
        novo_id = ultimo_evento['id'] + 1
    nome = input("Digite o nome do evento: ")
    data = input("Digite a data: ")
    local = input("Digite o local do evento: ")
    categoria = input("Digite a categoria do evento: ")
    
    novo_evento = {
        "id": novo_id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participou": False
    }
    
    lista_eventos.append(novo_evento)

    salvar_dados(lista_eventos)
    
    print(f"Evento '{nome}' adicionado com sucesso!")

def listar_eventos(lista_eventos):

    print("\n--- Lista de Eventos Cadastrados ---")
    if not lista_eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    for i, evento in enumerate(lista_eventos, start=1):
        status = "SIM" if evento["participou"] else "NÃO"
        print(f"{i}. Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Participou: {status}")
