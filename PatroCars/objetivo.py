'''PatroCars - Gestão de Montadoras

V1: Montadoras


Objetivo:
Praticar uso de Registros, Vetores e Arquivos

Registros:
Montadora 
(id: ULID, nome: string, pais: string, ano_fundacao: int)
ULID() → considere que isso vai gerar um id(string). Pesquise sobre.  Quando for implementar a PatroCars
Biblioteca para gerar ID ULID automaticamente:
Javascript: https://www.npmjs.com/package/ulidx
Python: https://github.com/mdomke/python-ulid 
Sistema:
Desenvolver Sistema com MENU para Gestão de Cadastro de Montadora de Veículos.
Requisitos:
CRUD: 
Criar, 
Listar todos
Atualizar; e
Remover (listar e então perguntar qual deseja remover)
Filtrar:
Parte do Nome
Parte do Nome País
Ao listar todas ou filtrar, sempre perguntar se desejar ordenar por qual atributo e ainda se ASC ou DESC (nome, pais, ano_funcacao)
Status: Mostrar situação do Cadastro, exemplo: Temos 5 Montadoras Cadastradas.
Gravar dados em Arquivos 
Ou como opção do Menu, ou ao Alterar o cadastro, ou ainda ao sair do sistema)
Criar um padrão de String para gravar em cada linha um Montadora
Ao inicializar o Programar verificar os dados em Arquivos
Extrair cadastro de cada linha e botar em Memória em uma Vetor de Registros de Montadora
Organização:
Arquivo Principal (Menu + Funções de Funcionalidades)
Utils (diversos arquivos para funcionalidades gerais de entrada/saída de dados, validações, vetores, strings, arquivos, registros e etc)
'''



'''
Objetivo:
- Criar lista com montadoras (E salvar)
- Listar montadoras
- Atualizar montadoras (E salvar)
- Remover Montadoras (Listar e perguntar qual é para remover) (E salvar)
- Filtrar ?
(Ao listar todas ou filtrar, sempre perguntar se desejar ordenar por qual atributo e ainda se ASC ou DESC (nome, pais, ano_fundacao)
- Exibir Status (Ex: temos 5 montadoras)

- Sair --> Gravar Dados? [Sim] [Não]
- Criar padrão de string para gravar em cada linha uma montadora


1. Quais são os dados de entrada necessários?
- (id: ULID, nome: string, pais: string, ano_fundacao: int)

2. O que devo fazer com esses dados?
- gravar eles em um arquivo para fazer alterações neles posteriormente

3, Quais são as restrições desse problema?
- Tem que haver dois arqvs para organização

4. Qual o resultado esperado
- Bom funcionamento do programa
5. Qual a sequência de passos a ser feita para chegar nesse resultado?
- Gerar ULID
- pedir as entradas nome, pais, ano_fundação.
- Inserir os dados em uma lista juntamente com o ULID
- Salvar em um Arquivo


'''


