from typing import List, Dict
from time import sleep

from models.funcionarios import Funcionario
from models.servicos import Servico
from utils.helpers import formata_float_str_moeda

profissionais: List[Funcionario] = []
servicos: List[Servico] = []
agendamento: List[Dict[Servico, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=========== SPA YinYang ==========')
    print('===================================')
    print('MENU')
    print('1 - Cadastrar funcionário')
    print('2 - Cadastrar serviço')
    print('3 - Associar Profissional a Serviço')
    print('4 - Listar quadro de funcionários')
    print('5 - Listar serviços')
    print('6 - Agendar tratamento')
    print('7 - Confirmar Agendamento')
    print('8 - Sair do sistema')

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadFunc()
    elif opcao == 2:
        cadServ()
    elif opcao == 3:
        associaFunc_serv()
    elif opcao == 4:
        listFunc()
    elif opcao == 5:
        listServ()
    elif opcao == 6:
        agendar()
    elif opcao == 7:
        confAgendamento()
    elif opcao == 8:
        print('Sistema Encerrado')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

def cadFunc() -> None:
    print('Cadastro de Funcionário')
    print('===================')

    nome: str = input('Nome Completo: ').title()
    especialidade: str = input('Especialidade: ').title()

    profissional: Funcionario = Funcionario(nome, especialidade)

    profissionais.append(profissional)

    print(f'Cadastro de profissional {profissional.nome} realizado com sucesso!')
    sleep(2)
    menu()

def cadServ() -> None:
    print('Cadastro de Serviço\n','-'*20)

    nome: str = input('Serviço: ').title()
    valor: float = float(input('Valor do Serviço: '))

    servico: Servico = Servico(nome, valor)

    servicos.append(servico)

    print(f'Cadastro de {servico.nome} realizado com sucesso')
    sleep(2)
    menu()

def associaFunc_serv() -> None:
    print('Associação de Profissional a Serviço\n', '-' * 20)
    if len(servicos) > 0:
        print('Listagem de Serviços\n','-'*20)
        for i in servicos:
            print(i)
            print('-'*20)
            sleep(1)
    else:
        print('Não há serviços a serem listados.')

    codigo: int = int(input('Informe o código do serviço a ser associado: '))
    nome: str = input('Informe o nome do profissional a ser associado: ').title()

    for i in servicos:
        if i.codigo == codigo:
            i.adicionar_profissional(nome)

    print('Associação feita com sucesso!')
    sleep(2)
    menu()

def listFunc() -> None:
    if len(profissionais) > 0:
        print('Listagem de Funcionários\n','-'*20)
        for i in profissionais:
            print(i)
            print('----------------')
            sleep(1)
        voltar = input('Digite VOLTAR para retornar ao menu ').upper()
        while voltar != 'VOLTAR':
            print('Entrada Inválida')
            voltar = input('Digite VOLTAR para retornar ao menu ').upper()
        menu()
    else:
        print('Ainda não existem profissionais cadastrados.')
    sleep(2)
    menu()

def listServ() -> None:
    if len(servicos) > 0:
        print('Listagem de Serviços\n','-'*20)
        for i in servicos:
            print(i)
            print('-'*20)
            sleep(1)
        voltar = input('Digite VOLTAR para retornar ao menu ').upper()
        while voltar != 'VOLTAR':
            print('Entrada Inválida')
            voltar = input('Digite VOLTAR para retornar ao menu ').upper()
        menu()
    else:
        print('Ainda não existem serviços cadastrados.')
    sleep(2)
    menu()

def agendar() -> None:
    if len(servicos) > 0:
        print('\./ Serviços Disponíveis \./')
        for i in servicos:
            print(i)
            print('-'*20)
            sleep(1)
        codigo: int = int(input('Informe o código do serviço a ser agendado: '))
        servico: Servico = addServ_cod(codigo)

        if servico:
            if len(agendamento) > 0:
                servAdicionado: bool = False
                for i in agendamento:
                    quant: int = i.get(servico)
                    if quant:
                        i[servico] = quant + 1
                        print(f'O serviço {servico.nome} agora possui {quant + 1} seleções para agendamento.')
                        servAdicionado = True
                        sleep(2)
                        menu()
                if not servAdicionado:
                    serv = {servico: 1}
                    agendamento.append(serv)
                    print(f'O serviço {servico.nome} foi selecionado para o agendamento.')
                    sleep(2)
                    menu()
            else:
                i = {servico: 1}
                agendamento.append(i)
                print(f'O serviço {servico.nome} foi selecionado para o agendamento.')
                sleep(2)
                menu()
        else:
            print(f'O serviço com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem serviços disponíveis.')
    sleep(2)
    menu()

def confAgendamento() -> None:
    if len(agendamento) > 0:
            valor_total: float = 0

            print('.\./Agendamento\./.')
            for i in agendamento:
                for dados in i.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    valor_total += dados[0].valor * dados[1]
                    print('------------------------')
                    sleep(1)
            print(f'Valor total dos serviços: {formata_float_str_moeda(valor_total)}')
            desistencia = input('Gostaria de remover algum serviço? S/N ').upper()
            while desistencia != 'N':
                indServ = int(input('Informe posição na lista do serviço a ser removido: '))
                agendamento.pop(indServ - 1)
                desistencia = input('Gostaria de remover algum serviço? S/N ').upper()

            valor_total: float = 0
            print('.\./Agendamento\./.')
            for i in agendamento:
                for dados in i.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    valor_total += dados[0].valor * dados[1]
                    print('------------------------')
                    sleep(1)
            print(f'Valor total dos serviços: {formata_float_str_moeda(valor_total)}')
            print('Volte sempre!')
            agendamento.clear()
            sleep(5)
    else:
        print('Ainda não existe agendamento a ser confirmado.')
    sleep(2)
    menu()

def addServ_cod(codigo: int) -> Servico:
    s: Servico = None

    for i in servicos:
        if i.codigo == codigo:
            s = i
    return s

if __name__ == '__main__':
    main()

