'''
arquivo_automaker = open('automaker_data.txt', 'a')

lista_automaker = [f"ID: {id_automaker}", f"Nome da Montadora: {name_automaker}", f"Nacionalidade da Montadora: {country_automaker}", f"Ano de Fundação da Montadora: {year_of_fundation}"]

for item in lista_automaker:
    arquivo_automaker.write(str(item) + ' ')
arquivo_automaker.write('\n')
'''


'''
    with open('automaker_data.txt', 'a') as arquivo:
        dicionario = {"ID:": id_automaker, "Nome da Montadora:": name_automaker, "Nacionalidade da Montadora:": country_automaker, "Ano de Fundação da Montadora:": year_of_fundation}
        lista_a = [dicionario]
        
    for item in lista_a:
            arquivo.write(str(item) + ' ')
    arquivo.write('\n')

'''