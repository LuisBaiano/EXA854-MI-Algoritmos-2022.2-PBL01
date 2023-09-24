#*********************************************************************************************************************

#Autor: Luis Felipe Pereira de Carvalho
#Componente curricular: MI Algoritmos I
#Concluído em: 24/09/2022
#  Declaro que este código foi elaborado por mim de forma indivdual e não contém nenhum trecho de código de colega ou de outro autor,
#tais como provindos de livros e apostilas, e paginas ou documentos eletrônicos da internet. qualquer trecho de código de outra autoria
#que não a minha está destacado como uma citação ao autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fim de avaliação.

#*********************************************************************************************************************

#iniciando as variáveis para as saidas de area total(reg: registrada, area_total_xx : onde xx é a sigla do estado)

area_reg = 0; area_nordeste = 0; area_total_al = 0; area_total_ba = 0; area_total_ce = 0; area_total_ma = 0 
area_total_pb = 0; area_total_pe = 0; area_total_pi = 0; area_total_rn = 0; area_total_se = 0; maior_area = 0

#variáveis para número total de areas (nordeste e estados)
qntd_area_nordeste = 0;  qntd_area_al = 0;  qntd_area_ba = 0;  qntd_area_ce = 0;  qntd_area_ma = 0
qntd_area_pb = 0; qntd_area_pe = 0; qntd_area_pi = 0;  qntd_area_rn = 0; qntd_area_se = 0

#=========================================================================================
#Iniciando as variáveis a serem utilizadas na registro dos tipos de árvore utilizados

#variáveis de contagem do número de vezes que cada tipo de árvore foi usado e
#na contagem de area total reflorestada respectivamente(linha 1 e 2)

bambu = 0; caju = 0; coque = 0; dende = 0; ipe = 0; manga = 0
area_tt_bambu = 0; area_tt_caju = 0; area_tt_coque = 0; area_tt_dende = 0; area_tt_ipe = 0; area_tt_manga = 0

#===================================================================================================================
#Iniciando variável para coletar o nome do estado e do tipo de arvore a serem exibidos na saída dos dados referente a maior área registrada
nome_estado = ''; nome_arvore = ''; cod_maior_area = ''; cid_maior_area = ''; est_maior_area = ''; are_maior_area = 0; arv_maior_area = ''
#===================================================================================================================

print('==='* 29)
print('BEM-VINDO(A) AO SISTEMA DE CADASTRO DE ÁREAS REFLORESTADAS DA ONG REFLORESTAR É REVIVER!') 
print('==='* 29)
opcao_inicial = int(input('''O que deseja fazer?
Digite apenas o número da opção que deseja executar.

[1] - Cadastrar nova área
[2] - Exibir relatório das áreas reflorestadas
[0] - Sair do programa
==============================================================
opção escolhida: '''))

while ( opcao_inicial !=0 ):
    if(opcao_inicial == 1):

        estado = int(input('''\nPor Favor, utilizando apenas a numeração indicada,
escolha o estado onde a área se encontra:

[1] - Alagoas
[2] - Bahia
[3] - Ceará
[4] - Maranhão
[5] - Paraíba
[6] - Pernambuco
[7] - Piauí
[8] - Rio Grande do Norte
[9] - Sergipe
==============================================================
opção escolhida: '''))
        while estado <1 or estado >9:
            estado = int(input('''\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!

Utilizando apenas a numeração indicada, escolha o estado onde a área se encontra:

[1] - Alagoas
[2] - Bahia
[3] - Ceará
[4] - Maranhão
[5] - Paraíba
[6] - Pernambuco
[7] - Piauí
[8] - Rio Grande do Norte
[9] - Sergipe
==============================================================
Opção escolhida: '''))

#variáveis para coleta das informações (código , área (base e altura) e cidade);

        codigo_area = str(input('\nDigite um código para a área reflorestada: '))

        cidade = str(input('\nDigite o nome da cidade onde a área se encontra: '))

        alt_area = float(input('\nDigite a altura da área em metros(são aceitos apenas números e ponto(.)): '))

        while(alt_area <= 0):
            alt_area = float(input('''\nEXTENSÃO DE ÁREA INVÁLIDA 
Digite novamente a altura da área em metros(são aceitos apenas números e ponto(.)): '''))

        base_area = float(input('\nDigite a base da área em metros(são aceitos apenas números e ponto(.)): '))

        while(base_area <= 0):
            base_area = float(input('''\nEXTENSÃO DE ÁREA INVÁLIDA, 
Digite novamente a base da área em metros(são aceitos apenas números e ponto(.)): '''))

        #registro do tipo de arvore utilizado;

        arvore = int(input('''\nUtilizando apenas a numeração indicada, Qual tipo de árvore foi utilizada?

[1] - Bambu gigante
[2] - Cajueiro
[3] - Coqueiro
[4] - Dendê
[5] - Ipê
[6] - Mangueira
==============================================================
Opção escolhida: '''))
        while (arvore < 1 or arvore > 6):
            arvore = int(input('''\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!

Utilizando apenas a numeração indicada, qual tipo de árvore foi utilizada?

[1] - Bambu gigante
[2] - Cajueiro
[3] - Coqueiro
[4] - Dendê
[5] - Ipê
[6] - Mangueira
==============================================================
Opção escolhida:'''))

        #variável area_reg para registrar a área informada pelo usuário  e area_nordeste é incrementada pela area informada;

        area_reg = (base_area*alt_area)
        area_nordeste += area_reg  

# Armazenando as informações conforme o estado escolhido
# Incremento da area do estado com a area informada;
# Incremento na quantidade de áreas reflorestadas no estado;
# Registro do nome do estado para ser utilizado na saída dos dos dados referentes a maior area;

        if estado == 1:
            area_total_al += area_reg
            qntd_area_al += 1
            nome_estado = 'Alagoas'

        elif estado == 2:
            area_total_ba += area_reg
            qntd_area_ba += 1
            nome_estado = 'Bahia'

        elif estado == 3:
            area_total_ce += area_reg
            qntd_area_ce += 1
            nome_estado = 'Ceará'

        elif estado == 4:
            area_total_ma += area_reg
            qntd_area_ma += 1
            nome_estado = 'Maranhão'

        elif estado == 5:
            area_total_pb += area_reg
            qntd_area_pb += 1
            nome_estado = 'Paraíba'

        elif estado == 6:
            area_total_pe += area_reg
            qntd_area_pe += 1
            nome_estado = 'Pernambuco'

        elif estado == 7:
            area_total_pi += area_reg
            qntd_area_pi += 1
            nome_estado = 'Piauí'

        elif estado == 8:
            area_total_rn += area_reg
            qntd_area_rn += 1
            nome_estado = 'Rio Grande do Norte'

        elif estado == 9:
            area_total_se += area_reg
            qntd_area_se += 1
            nome_estado = 'Sergipe' 

# Registro dos tipo de arvore dentro dos ifs onde são processados:
# incremento no número de vezes que o tipo de arvore foi utilizado;
# incremento no número de area total no qual cada tipo de arvore foi utilizado;
# registro do nome do tipo de arvore para ser utilizado na saída dos dos dados referentes a maior area;

        if arvore == 1:
            bambu += 1
            area_tt_bambu += area_reg
            nome_arvore = 'Bambu gigante'

        elif arvore == 2:
            caju += 1
            area_tt_caju += area_reg
            nome_arvore = 'Cajueiro' 

        elif arvore == 3:
            coque += 1
            area_tt_coque += area_reg
            nome_arvore = 'Coqueiro'

        elif arvore == 4:
            dende += 1
            area_tt_dende += area_reg
            nome_arvore = 'Dendê'

        elif arvore == 5:
            ipe += 1
            area_tt_ipe += area_reg
            nome_arvore = 'Ipê'

        elif arvore == 6:
            manga += 1
            area_tt_manga += area_reg
            nome_arvore = 'Mangueira'

        #Condicional para a coleta da exibição das informações referentes a maior área registrada

        if(area_reg > maior_area):
            maior_area = area_reg
            cod_maior_area = codigo_area
            cid_maior_area = cidade
            est_maior_area = nome_estado
            are_maior_area = area_reg
            arv_maior_area = nome_arvore

        opcao_inicial = int(input('''\nCADASTRO CONCLUIDO COM SUCESSO!

O que deseja fazer agora ?

[1] - Novo Cadastro
[2] - Exibir as estatísticas
[0] - Sair do sistema
==============================================================
Opção escolhida: '''))

    elif(opcao_inicial == 2):
        
        #Relatório de saída dos dados cadastrados

        print('==='*29)
        print('RELATÓRIO DAS PRINCIPAIS ESTATÍSTICAS DE REFLORESTAMENTO ')
        print('==='*29)

        # de modo a verificar a existência ou não de dados cadastrados, é utilizado um condicional em relação ao valor da area total do nordeste, estado escolhido(por numeração)
        # pois a area nordeste é sempre incrementada na execução do código, além de que, o usuário é obrigado a fornecer valores validos para o cadastro da área.

        if(area_nordeste != 0):

            print('\nÁREA TOTAL REFLORESTADA POR ESTADOS: \n')

            print('Alagoas: %.2f m² ' % area_total_al)
            print('Bahia: %.2f m² ' % area_total_ba)
            print('Ceará: %.2f m² ' % area_total_ce)
            print('Maranhão: %.2f m² ' % area_total_ma)
            print('Paraíba: %.2f m² ' % area_total_pb)
            print('Pernambuco: %.2f m² ' % area_total_pe)
            print('Piauí: %.2f m² ' % area_total_pi)
            print('Rio Grande do Norte: %.2f m² ' % area_total_rn)
            print('Sergipe: %.2f m² ' % area_total_se)

            print('======================================================================================= \nA ÁREA TOTAL REFLORESTADA NA REGIÃO NORDESTE FOI DE:\n')
            print('Região Nordeste: %.2f m²\n' % area_nordeste)

            print('======================================================================================= \nQUANTIDADE TOTAL DE ÁREAS REFLORESTADAS POR ESTADOS: \n')
            print('Alagoas: %d área(s) ' % qntd_area_al)
            print('Bahia: %d área(s) ' % qntd_area_ba)
            print('Ceará: %d área(s) ' % qntd_area_ce)
            print('Maranhão: %d área(s) ' % qntd_area_ma)
            print('Paraíba: %d área(s) ' % qntd_area_pb)
            print('Pernambuco: %d área(s) ' % qntd_area_pe)
            print('Piauí: %d área(s) ' % qntd_area_pi)
            print('Rio Grande do Norte: %d área(s) ' % qntd_area_rn)
            print('Sergipe: %d área(s) ' % qntd_area_se)

            print('=======================================================================================\nA ÁREA TOTAL REFLORESTADA POR CADA TIPO DE ARVORE:\n')
            print('Bambu gigante: %.2f m² ' % area_tt_bambu)
            print('Cajueiro: %.2f m² ' % area_tt_caju)
            print('Coqueiro: %.2f m² ' % area_tt_coque)
            print('Dendê: %.2f m² ' % area_tt_dende)
            print('Ipê: %.2f m² ' % area_tt_ipe)
            print('Mangueira: %.2f m² \n' % area_tt_manga)

            print('\n======================================================================================= \nO(S) TIPO(S) DE ÁRVORE QUE FOI(RAM) MAIS UTILIZADO(S) NO REFLORESTAMENTO: \n')

            if bambu >= caju and bambu >= coque and bambu >= dende and bambu >= ipe and bambu >= manga:
                print('Bambu gigante: %d vez(es).' % bambu)

            if caju >= bambu and caju >= coque and caju >= dende and caju >= ipe and caju >= manga:
                print('Cajueiro: %d vez(es).' % caju)

            if coque >= bambu and coque >= caju and coque >= dende and coque >= ipe and coque >= manga:
                print('Coqueiro: %d vez(es).' % coque)

            if dende >= bambu and dende >= coque and dende >= caju and dende >= ipe and dende >= manga:
                print('Dênde: %d vez(es).' % dende)

            if ipe >= bambu and ipe >= coque and ipe >= dende and ipe >= caju and ipe >= manga:
                print('Ipê: %d vez(es).' % ipe)

            if manga >= bambu and manga >= coque and manga >= dende and manga >= ipe and manga >= caju:
                print('Mangueira: %d vez(es).' % manga)

            print('\n======================================================================================= \nO(S) TIPO(S) DE ÁRVORE(S) QUE FOI(RAM) MENOS UTILIZADO(S) NO REFLORESTAMENTO: \n''')

            if bambu <= caju and bambu <= coque and bambu <= dende and bambu <= ipe and bambu <= manga:
                print('Bambu gigante: %d vez(es).' % bambu)

            if caju <= bambu and caju <= coque and caju <= dende and caju <= ipe and caju <= manga:
                print('Cajueiro: %d vez(es).' % caju)

            if coque <= bambu and coque <= caju and coque <= dende and coque <= ipe and coque <= manga:
                print('Coqueiro: %d vez(es).' % coque)

            if dende <= bambu and dende <= coque and dende <= caju and dende <= ipe and dende <= manga:
                print('Dênde: %d vez(es).' % dende)

            if ipe <= bambu and ipe <= coque and ipe <= dende and ipe <= caju and ipe <= manga:
                print('Ipê: %d vez(es).' % ipe)

            if manga <= bambu and manga <= coque and manga <= dende and manga <= ipe and manga <= caju:
                print('Mangueira: %d vez(es).' % manga)

            print('\n======================================================================================= \nO(S) ESTADO(S) MAIS REFLORESTADO(s) FOI(RAM):\n')
            if area_total_al >= area_total_ba and area_total_al >= area_total_ce and area_total_al >= area_total_ma and area_total_al >= area_total_pb and area_total_al >= area_total_pe and area_total_al >= area_total_pi and area_total_al >= area_total_rn and area_total_al >= area_total_se:
                print(f'Alagoas: {area_total_al} m².')

            if area_total_ba >= area_total_al and area_total_ba >= area_total_ce and area_total_ba >= area_total_ma and area_total_ba >= area_total_pb and area_total_ba >= area_total_pe and area_total_ba >= area_total_pi and area_total_ba >= area_total_rn and area_total_ba >= area_total_se:
                print(f'Bahia: {area_total_ba} m².')

            if area_total_ce >= area_total_al and area_total_ce >= area_total_ba and area_total_ce >= area_total_ma and area_total_ce >= area_total_pb and area_total_ce >= area_total_pe and area_total_ce >= area_total_pi and area_total_ce >= area_total_rn and area_total_ce >= area_total_se:
                print(f'Ceará: {area_total_ce} m².')

            if area_total_ma >= area_total_al and area_total_ma >= area_total_ba and area_total_ma >= area_total_ce and area_total_ma >= area_total_pb and area_total_ma >= area_total_pe and area_total_ma >= area_total_pi and area_total_ma >= area_total_rn and area_total_ma >= area_total_se:
                print(f'Maranhão: {area_total_ma} m².')

            if area_total_pb >= area_total_al and area_total_pb >= area_total_ba and area_total_pb >= area_total_ce and area_total_pb >= area_total_ma and area_total_pb >= area_total_pe and area_total_pb >= area_total_pi and area_total_pb >= area_total_rn and area_total_pb >= area_total_se:
                print(f'Paraíba: {area_total_pb} m².')

            if area_total_pe >= area_total_al and area_total_pe >= area_total_ba and area_total_pe >= area_total_ce and area_total_pe >= area_total_ma and area_total_pe >= area_total_pb and area_total_pe >= area_total_pi and area_total_pe >= area_total_rn and area_total_pe >= area_total_se:
                print(f'Pernambuco: {area_total_pe} m².')
            
            if area_total_pi >= area_total_al and area_total_pi >= area_total_ba and area_total_pi >= area_total_ce and area_total_pi >= area_total_ma and area_total_pi >= area_total_pb and area_total_pi >= area_total_pe and area_total_pi >= area_total_rn and area_total_pi >= area_total_se:
                print(f'Piauí: {area_total_pi} m².')

            if area_total_rn >= area_total_al and area_total_rn >= area_total_ba and area_total_rn >= area_total_ce and area_total_rn >= area_total_ma and area_total_rn >= area_total_pb and area_total_rn >= area_total_pe and area_total_rn >= area_total_pi and area_total_rn >= area_total_se:
                print(f'Rio Grande do Norte: {area_total_rn} m².')

            if area_total_se >= area_total_al and area_total_se >= area_total_ba and area_total_se >= area_total_ce and area_total_se >= area_total_ma and area_total_se >= area_total_pb and area_total_se >= area_total_pe and area_total_se >= area_total_pi and area_total_se >= area_total_rn:
                print(f'Sergipe: {area_total_se} m².')


            print('\n======================================================================================= \nO(S) ESTADO(S) MENOS REFLORESTADO(s) FOI(RAM):\n')
            if area_total_al <= area_total_ba and area_total_al <= area_total_ce and area_total_al <= area_total_ma and area_total_al <= area_total_pb and area_total_al <= area_total_pe and area_total_al <= area_total_pi and area_total_al <= area_total_rn and area_total_al <= area_total_se:
                print(f'Alagoas: {area_total_al} m².')

            if area_total_ba <= area_total_al and area_total_ba <= area_total_ce and area_total_ba <= area_total_ma and area_total_ba <= area_total_pb and area_total_ba <= area_total_pe and area_total_ba <= area_total_pi and area_total_ba <= area_total_rn and area_total_ba <= area_total_se:
                print(f'Bahia: {area_total_ba} m².')

            if area_total_ce <= area_total_al and area_total_ce <= area_total_ba and area_total_ce <= area_total_ma and area_total_ce <= area_total_pb and area_total_ce <= area_total_pe and area_total_ce <= area_total_pi and area_total_ce <= area_total_rn and area_total_ce <= area_total_se:
                print(f'Ceará: {area_total_ce} m².')

            if area_total_ma <= area_total_al and area_total_ma <= area_total_ba and area_total_ma <= area_total_ce and area_total_ma <= area_total_pb and area_total_ma <= area_total_pe and area_total_ma <= area_total_pi and area_total_ma <= area_total_rn and area_total_ma <= area_total_se:
                print(f'Maranhão: {area_total_ma} m².')

            if area_total_pb <= area_total_al and area_total_pb <= area_total_ba and area_total_pb <= area_total_ce and area_total_pb <= area_total_ma and area_total_pb <= area_total_pe and area_total_pb <= area_total_pi and area_total_pb <= area_total_rn and area_total_pb <= area_total_se:
                print(f'Paraíba: {area_total_pb} m².')

            if area_total_pe <= area_total_al and area_total_pe <= area_total_ba and area_total_pe <= area_total_ce and area_total_pe <= area_total_ma and area_total_pe <= area_total_pb and area_total_pe <= area_total_pi and area_total_pe <= area_total_rn and area_total_pe <= area_total_se:
                print(f'Pernambuco: {area_total_pe} m².')
            
            if area_total_pi <= area_total_al and area_total_pi <= area_total_ba and area_total_pi <= area_total_ce and area_total_pi <= area_total_ma and area_total_pi <= area_total_pb and area_total_pi <= area_total_pe and area_total_pi <= area_total_rn and area_total_pi <= area_total_se:
                print(f'Piauí: {area_total_pi} m².')

            if area_total_rn <= area_total_al and area_total_rn <= area_total_ba and area_total_rn <= area_total_ce and area_total_rn <= area_total_ma and area_total_rn <= area_total_pb and area_total_rn <= area_total_pe and area_total_rn <= area_total_pi and area_total_rn <= area_total_se:
                print(f'Rio Grande do Norte: {area_total_rn} m².')

            if area_total_se <= area_total_al and area_total_se <= area_total_ba and area_total_se <= area_total_ce and area_total_se <= area_total_ma and area_total_se <= area_total_pb and area_total_se <= area_total_pe and area_total_se <= area_total_pi and area_total_se <= area_total_rn:
                print(f'Sergipe: {area_total_se} m².')

            #relatório dos dados cadastrados para a maior area registrada

            print('======================================================================================= \nINFORMAÇÕES DA MAIOR ÁREA REGISTRADA\n')
            print('''Código: %s 
Cidade: %s 
Estado: %s 
Área: %.2f m² 
Tipo de arvore: %s''' % (cod_maior_area, cid_maior_area, est_maior_area, are_maior_area, arv_maior_area))
            
            print('\nEstatísticas exibidas com sucesso!')
        else:
            print('\nNão existem dados cadastrados.')
            
        opcao_inicial = int(input('''\nO que deseja fazer agora ?
[1] - Novo Cadastro
[2] - Exibir Novamente o relatório de estatísticas
[0] - Sair do sistema
==============================================================
Opção escolhida: '''))

    else:
        opcao_inicial = int(input('''======================================
Opção inválida, Tente novamente!
=====================================
Escolha uma opção:
[1] - Cadastrar nova área
[2] - Exibir relatório das áreas reflorestadas
[0] - Sair do sistema

Digite apenas o número da opção que deseja executar: '''))

print('\nObrigado por usar nosso sistema, A ONG Reflorestar é Reviver agradeçe a sua colaboração.')