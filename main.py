# main.py - Versão final e integrada
from interface_usuario import *
# from gerenciador_eventos import *
import gerenciador_eventos as ge
import interface_usuario as iu
import os
import time

def main():
    eventos = ge.carregar_dados()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        iu.display_menu()
        escolha = iu.get_escolha()
        match escolha:
            case 1:
                ge.listar_eventos(eventos)
            case 2:
                ge.adicionar_evento(eventos)
            case 3:
                categoria = input('Informe a categoria a ser filtrada: ')
                iu.filtrar_por_categoria(eventos, categoria)
            case 4:
                try:
                    id_evento = int(input("Informe o ID do evento para marcar a participação: "))
                    iu.marcar_evento_atendido(eventos, id_evento)
                    ge.salvar_dados(eventos)
                except ValueError:
                    print("ID inválido. Por favor, digite um número.")
            case 5:
            
                iu.gerar_relatorio(eventos)
            case 6:
                print("\n--- Excluir Evento ---")
                ge.listar_eventos(eventos)
                
                if eventos:
                    try:
                        id_para_remover = int(input("Digite o ID do evento que você deseja excluir: "))
                        sucesso = ge.remover_evento(eventos, id_para_remover)
                        if sucesso:
                            ge.salvar_dados(eventos)
                    except ValueError:
                        print("Erro: ID inválido. Por favor, digite um número.")
            case 7:
                print("Saindo do programa...")
                break
            case _:
                print('Opção Inválida')
                time.sleep(2)
        
        if escolha != 7:
            print('\nPressione Enter para continuar.')
            input()

if __name__ == "__main__":
        main()