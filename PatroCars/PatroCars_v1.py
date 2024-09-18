import utils

def main():
    print(utils.main_menu())
    opcao = int(input('Expresse seu Comando: '))

    if opcao == 1:
        utils.insert_automaker()
        return main()
    if opcao == 2:
        utils.list_automaker()
        return main()
    if opcao == 99:
        print('Fim')

main()