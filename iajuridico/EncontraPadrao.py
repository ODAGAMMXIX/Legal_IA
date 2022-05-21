#APLICAÇÃO DE INTELIGÊNCIA ARTIFICIAL

#LABORATÓRIO DE DESENVOLVIMENTO DE BANCO DE DADOS VI

# ANÁLISE DE AMOSTRAGEM + RECOMENDAÇÃO PARA ADVOCACIA.


from operator import contains
from apyori import apriori

#SIMULAÇÃO DE LINGUAGEM NATURAL: amostragem 12 processos
#>ria x -1 = <minoria = PROPONHA AÇÃO
#>ria = FAÇA ACORDO
#itemset = {{'ação'},{'nexo'},{'dano'}}
item_set = frozenset(['ação','nexo','dano'])
item_set_2 = frozenset(['omissão','nexo','dano'])
transactions_bd= [['ação'], # improcedente 
                  ['ação', 'nexo'],# improcedente 
                  ['ação', 'nexo', 'dano'],# procedente = 16,67% dos casos
                    ['omissão'],# improcedente
                  ['omissão', 'nexo'],# improcedente
                  ['omissão', 'nexo', 'dano'],# procedente = 16,67% dos casos
                  ] # neste exemplo, em 33,33% dos casos temos #PROCEDENTE
                    # então, 66,67% dos casos temos #IMPROCEDENTE
                        # 1-0,166666666667 = PROPONHA ACORDO OU NÃO ENTRE COM AÇÃO
                        # 0,1666666667% = -------------PROCESSO JUDICIAL ---------------

# In this example, support >= 40% and confidence >= 70% define "relevant" rules
# If you look at the result that is printed, the question answered is: "What
# association rules have high probability, with respect to support and confidence
# values, to become "good recommendation rules". Adapt it for the case related
# to legal process senteces. What questions can be answered if one take the output
# of the algorithm? Consider 2 cases:
# 1) min_support and min_confidence are specified. What do the output associations
#  mean?
# 2 ) min_suport and min_confidence are not specified. Look at their values at
#  the output, considering some association. FOR CASES WITHOUT SPECIFICATION OF min_support (==0.1) AND min_confidence (==0.0)
    # THEREFORE = MAXIMUM COMBINATIONS OF PARAMETERS.
#
# Remember that any rule has a form: antecedent ---> consequent
# In other words: if antecedent then consequent.
#

## This code is to perform analysis of question 1)
results = list(apriori(transactions_bd, min_support = 0.1, min_confidence = 0.15))
#results = list(apriori(transactions_bd))
# MIN_SUPPORT = PROPORÇÃO DE OCORRÊNCIAS DE UM ÚNICO ITEM
# MIN_CONFIDENCE = PROPORÇÃO DE OCORRÊNCIAS DE ITENS ASSOCIADOS
print('Rules with support and confidence above the specified threshold: ')
print("--------------------------")
association = 1
for result in results:
    r = result[0]
    sup = result[1]
    print("(#%s th)Association: items = %s, support= %s" % (association, r, sup))
    association += 1
    rule = 1
    for os in result[2]:
        print('Rule #', rule)
        print("rule antecedent: ", r - os[1])
        print("rule consequent: %s, confidence: %s" % (os[1], os[2]))
        print(type(os[1])) #VERIFICAR O QUE TEM DENTRO DO "os"
        
        #if os[1].issubset(item_set): #item_set = frozenset(['ação','nexo','dano'])
        #if os[1].issubset(item_set): #item_set = frozenset(['ação','nexo','dano'])
        if os[1] == item_set or os[1] == item_set_2:
            print("-------------PROCESSO JUDICIAL--------------")            
        else:             
            print("PROPONHA ACORDO OU NÃO ENTRE COM AÇÃO")
        
        rule+=1
    print("_____________________________________________________________________________")


## This code is to perform analysis of question 2)
'''print('*************************************************************************************')
results = list(apriori(transactions_bd, min_support=0.001, min_confidence=0.001))
print('Rules with support and confidence not specified ')
print("--------------------------")
association = 1
for result in results:
    r = result[0]
    sup = result[1]
    print("(#%s th)Association: items = %s, support= %s" % (association, r, sup))
    association += 1
    rule = 1
    for os in result[2]:
        print('Rule #', rule)
        print("rule antecedent: ", r - os[1])
        print("rule consequent: %s, confidence: %s" % (os[1], os[2]))
        rule+=1
    print("##################################################################")'''

