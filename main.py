def menu():
    ''' Exibe o menu de opções do sistema '''
    print('AGENDA DE CONTATOS')
    print('(1) Criar novo contato:')
    print('(2) Listar todos os contatos.')
    print('(3) Buscar contato.')


def cadastrarContato(nome, telefone, email, arquivoAgenda):
    #Abre o arquivo em modo append, para escrever ao final do arquivo
    #Se o arquvivo não existir ele será criado automaticamente.
    agenda = open(arquivoAgenda, 'a')
    #Escrevemos os dados os dados do contato e damos retorno \r
    agenda.write(f'{nome},{telefone},{email}\r')
    #Fecha o arquivo
    agenda.close()

def listarContatos(arquivoAgenda):
    ''' Lista nome, telefone, e-mail de cada contato na agenda definida pelo caminho do arquivo'''
    #Abrir agenda para leitura
    agenda = open("agenda.csv",'r')
    #lê todo o conteúdo 
    contatos = agenda.read()
    #cria uma lista onde cada elemento da lista é uma das linhas da agenda.
    contatos = contatos.splitlines()
    agenda.close()

    # percorre a lista de contatos
    print(f"{'CONTATO':30}\t{'TELEFONE':>20}\t{'E-MAIL':>30}")
    for contato in contatos:
        contato = contato.split(',')
        nome = contato[0]
        telefone = contato[1]
        email = contato[2]
        print(f'{nome:30}\t{telefone:>20}\t{email:>30}')

def buscarContato(busca, arquivoAgenda):
    agenda = open(arquivoAgenda, 'r')
    contatos = agenda.read()
    contatos = contatos.splitlines()
    agenda.close()
    resultados = 0
    for contato in contatos:
        contato = contato.split(',')
        nome, telefone, email = contato[0], contato[1], contato[2]
        if busca in nome or busca in telefone or busca in email:
            print(f'{nome:<30}\t{telefone:>20}\t{email:<30}')
            resultados += 1
    print(f'\n{resultados} resultados(s) encontrados(s). ')

arquivoAgenda = input('Informe o arquivo da agenda: ')

while True:
    menu()

    opcao = int(input('Selecione a opção desejada (Digite 9 caso queira sair): '))
    print('-'*40)
    if opcao == 1:
        print('Cadastro de novo contato.')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('E-mail: ')
        cadastrarContato(nome, telefone, email, arquivoAgenda)
        print(f'\nContato {nome} cadastrado com sucesso!')
        print('-'*40)
    elif opcao == 2:
        print('Listar todos os contatos.')
        listarContatos(arquivoAgenda)
        print('-'*40)
    elif opcao == 3:
        print('Buscar contato.')
        busca = input('Informe o parâmetro de busca: ')
        buscarContato(busca, arquivoAgenda)
        print('-'*40)
    elif opcao == 9:
        break
    else:
        print('Opção inválida.')
        print('-'*40)

