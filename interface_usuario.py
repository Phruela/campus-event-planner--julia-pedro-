def display_menu():
    '''Exibe o menu principal para o usuário.
    
    Imprime todas as opções disponíveis que o usuário
    pode escolher para gerenciar os eventos'''

    print('''
    === Planejador de Eventos do Campus ===
    1. Ver todos os eventos
    2. Adicionar Evento
    3. Filtrar Categoria
    4. Marcar Evento como Participado
    5. Gerar Relatório
    6. Excluir Evento
    7. Sair
    ''')

def get_escolha():
    '''Lê e valida a escolha do usuário no menu
    
    Solicita que o usuário informe um número em um loop 
    até que seja informada uma entrada válida
    
    Returns:
        int: O número inteiro correspondente  à opção escolhida pelo usuário
    '''

    while(True):
        try:
            escolha = int(input("Esolha uma opção: "))
            return escolha
        except ValueError:
            print('Informe um número inteiro válido')

def filtrar_por_categoria(lista_eventos, categoria):
'''Filtra e exibe os eventos da categoria selecionada.

A função percorre a lista de eventos e imprime os eventos 
que pertencem à categoria fornecida. Se nenhum evento for 
encontrado a função retorna uma mensagem informando que 
nenhum evento foi encontrado.

Args:
    lista_eventos (lista): A lista de dicionários dos eventos.
    categoria (str): A categoria que irá filtrar os eventos.
'''

    eventos_filtrados = [
        evento for evento in lista_eventos
        if categoria.lower() == evento['Categoria'].lower()
    ]
    print(f'=== Eventos na categoria: {categoria} ===')
    if not eventos_filtrados:
        print('Nenhum evento cadastrado nessa categoria.')
    else: 
        for evento in eventos_filtrados:
            print(f'ID: {evento['id']} - {evento['nome']}')
