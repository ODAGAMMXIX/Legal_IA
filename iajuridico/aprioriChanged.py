# A simple 1-level association rule apriori
# algorithm implementation
#
# Author: Fabrício G. M. de Carvalho, Ph.D
# Adttion: F.O. 2-level ssociation rule.


itemset = ['ação','nexo','dano']
transactions_bd= [{'ação'},
                  {'ação', 'nexo'},
                  {'ação', 'nexo', 'dano'},
                  {'nexo', 'ação', 'dano'},
                  {'nexo', 'dano'},
                  {'dano', 'nexo'}
                  ]

itemset2 = ['omissão','nexo','dano']
transactions_bd2= [{'omissão'},
                  {'omissão', 'nexo'},
                  {'omissão', 'nexo', 'dano'},
                  {'nexo', 'omissão', 'dano'},
                  {'nexo', 'dano'},
                  {'dano', 'nexo'}
                  ]                  

#Support calculation
def support(Ix, Iy, Iz, bd): # % of occurrences
    # print(f'[support - init] Ix {Ix}, Iy {Iy}, Iz {Iz}, bd {bd}')
    sup = 0
    for transaction in bd:
        # print(f'[support - midlle] transaction {transaction}')
        if (Ix.union(Iy).union(Iz)).issubset(transaction): # o conjunto Ix + conjunto Iy está dentro(contido) no transaction
            sup+=1
    # print(f'[support = middle] sup {sup}')
    sup = sup/len(bd)
    # print(f'[support - end] sup {sup}')
    return sup

# Confidence calculation
def confidence(Ix, Iy,Iz, bd): # quantity of associated events
    # print(f'[confidence - init] Ix {Ix}, Iy {Iy}, Iz {Iz}, bd {bd}')
    Ix_count = 0
    Ixy_count = 0
    Ixyz_count = 0
    for transaction in bd:
        # print(f'[confidence - middle] transaction {transaction}')
        if Ix.issubset(transaction): # Ix está contido em transaction
            Ix_count+=1
            if (Ix.union(Iy)).issubset(transaction): # o conjunto Ix + conjunto Iy está dentro(contido) no transaction
                Ixy_count += 1
                if (Ix.union(Iy).union(Iz)).issubset(transaction):
                    Ixyz_count += 1
    # print(f'[confidence - middle] Ixy_count {Ixy_count}, Ix_count {Ix_count}')
    conf = Ixyz_count / (Ix_count + Ixy_count) #TODO validate this math conf = Ixy_count / Ix_count
    # print(f'[conf - end] conf {conf}')
    return conf
            

# This function eliminates all the items in 
# ass_rules which have sup < min_sup and
# conf < min_conf. It returns a "pruned" list
def prune(ass_rules, min_sup, min_conf):
    # print(f'[prune - init] ass_rules {ass_rules}, min_sup {min_sup}, min_conf {min_conf}')
    pruned_ass_rules = []
    for ar in ass_rules:
        #print(f'prune - middle] arr {ar}')
        if ar['support'] >= min_sup and ar['confidence'] >= min_conf:
            pruned_ass_rules.append(ar)
    #print(f'[prune - end] pruned_ass_rules {pruned_ass_rules}')
    return pruned_ass_rules
    

# Apriori for association between 2 items
def apriori_2(itemset, bd, min_sup, min_conf):
    ass_rules = []
    ass_rules.append([]) #level 1 (large itemsets)
    #print("first for")
    for item in itemset:
        #print("******")
        #print(item)
        sup = support({item},{item},{item},bd)
        ass_rules[0].append({'rule': str(item), \
                             'support':sup, \
                             'confidence': 1})        
    #print(f"PRUNINNG...")
    ass_rules[0] = prune(ass_rules[0],min_sup, min_conf)
    ass_rules.append([]) #level 2 (2 items association)
    #print("=============")
    #print("second for")
    for item_1 in ass_rules[0]:
        for item_2 in ass_rules[0]:
            for item_3 in ass_rules[0]:
                if item_1['rule'] != item_2['rule']:
                    # print("******")
                    rule = item_1['rule']+'_'+item_2['rule']+'_'+item_3['rule']
                    Ix = {item_1['rule']}
                    Iy = {item_2['rule']}
                    Iz = {item_3['rule']}
                    #print(f'[apriori - middle] rule {rule} Ix {Ix}, Iy {Iy}, Iz {Iz}')
                    sup = support(Ix,Iy, Iz,bd)
                    conf = confidence(Ix, Iy, Iz,bd)
                    # print(f'[apriori - middle] rule {rule} Ix {Ix}, Iy {Iy}, Iz {Iz} , sup {sup}, conf {conf}')
                    ass_rules[1].append({'rule':rule, \
                                        'support': sup, \
                                        'confidence': conf})
    #print(f"PRUNINNG...")
    ass_rules[1] = prune(ass_rules[1],min_sup, min_conf) #leave meaningful data
    return ass_rules

    
if __name__ == "__main__": # prevents execution by a proxy
    print(apriori_2(itemset, transactions_bd, 0.4, 0.6))
    print("******************************************************************************")
    print(apriori_2(itemset2, transactions_bd2, 0.4, 0.6))
    cont = input('Press enter to continue...')
