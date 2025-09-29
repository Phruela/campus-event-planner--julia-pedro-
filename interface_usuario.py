from collections import Counter

def display_menu():
    '''Exibe o menu principal para o usuário.
    
    Imprime todas as opções disponíveis que o usuário
    pode escolher para gerenciar os eventos
    '''

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
    print(f'--- Eventos na categoria: {categoria} ---')
    if not eventos_filtrados:
        print('Nenhum evento cadastrado nessa categoria.')
    else: 
        for evento in eventos_filtrados:
            print(f'ID: {evento['id']} - {evento['nome']}')


def marcar_evento_atendido(lista_eventos, id_informado):
    '''Marca um evento como participado.

    Busca um evento na lista pelo ID e altera o status de participação
    para True. O usuário é informado se a operação foi bem sucedida ou
    se não foi possível encontrar um evento com o ID fornecido.

    Args: 
        lista_eventos (lista): A lista de dicionários dos eventos.
        id_informado (int): O ID do evento que deve ser marcado como participado.
    '''

    for evento in lista_eventos:
        if evento['id'] == id_informado:
            if evento['participacao']:
                print(f'A Participação no evento {evento['nome']} já estava confirmada')
            else:
                evento['participacao'] = True
                print(f'Participação no evento {evento['nome']} confirmada')
            return
    print(f'Nenhum evento com o ID {evento['id_informado']} encontrado.')


def gerar_relatorio(lista_eventos):
    '''Exibe um relatório com as estatisticas do evento.

    A função calcula as segintes estatisticas sobre os eventos e as imprime no console:
    1. O número total de eventos cadastrados
    2. A contagem de eventos por categoria
    3. A porcentagem de eventos marcados como participados

    Args:
        lista_eventos (list): A lista contendo todos os dicionários dos eventos
    '''
    if not lista_eventos:
        print('Nenhum evento cadastrado')
        return

    total_eventos = len(lista_eventos)
    lista_categorias = [evento['categoria'] for evento in lista_eventos]
    contagem_categorias = Counter(lista_categorias)
    total_participacoes = 0
    for evento in lista_eventos:
        if evento['participacao']:
            total_participacoes += 1
    porcentagem_participacoes = (total_participacoes / total_eventos) * 100

    print('--- Relatório de Eventos ---')
    print(f'Total de eventos: {total_eventos}')
    print('Eventos por categoria:')
    for categoria, contagem in contagem_categorias.most_common():
        print(f'- {categoria}: {contagem}')
    print(f'Participados: {porcentagem_participacoes:.2f}% ({total_participacoes}/{total_eventos})')



