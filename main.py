from interface_usuario import *
# from gerenciador_eventos import *
import os
import time

def main():
    while(True):
        os.system("cls" if os.name == "nt" else "clear")
        escolha = get_escolha()
        match escolha:
        #     # case 1:
        #     #     listar_eventos()
        #     # case 2:
        #     #     adicionar_evento()
            case 3:
                categoria = input('Informe a categoria a ser filtrada: ')
                filtrar_por_categoria(lista_eventos, categoria)
                print()
                print('Pressione Enter para continuar.')
                input()
            case 4:
                id_evento = int(input("Informe o ID do evento para marcar a participação: "))
                marcar_evento_atendido(lista_eventos, id_evento)
                print()
                print('Pressione Enter para continuar')
                input()
            case 5:
                gerar_relatorio(lista_eventos)
                print()
                print('Pressione Enter para continuar')
                input()
        #     # case 6:
        #     #     deletar_evento()
            case 7:
                break
            case _:
                print('Opção Inválida')
                time.sleep(2)


if __name__ == "__main__":
    main()
