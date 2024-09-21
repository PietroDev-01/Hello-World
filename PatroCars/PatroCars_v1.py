import utils

def main():
    print(utils.main_menu())
    opcao = utils.get_number_in_range('Expresse o seu Comando: ', 1,3)
    if opcao == 1:
        utils.insert_automaker()
        return main()
    if opcao == 2:
        utils.list_automaker()
        return main()
    if opcao == 3:
        print('Fim')

main()