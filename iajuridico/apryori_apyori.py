# Basic apriori application to perform
# data analysis. In this example market items have been
# used. Adapt it to the specific problem.
#
# Author: Fabrício G. M. de Carvalho, Ph.D
# LET'S C WTF!
##


from apyori import apriori

transactions_bd = [
    ['queijo', 'pão', 'batata'],
    ['queijo', 'presunto'],
    ['queijo'],
    ['queijo', 'batata', 'pão'],
    ['batata']
]
# In this example, support >= 40% and confidence >= 70% define "relevant" rules
# If you look at the result that is printed, the question answered is: "What
# association rules have high probability, with respect to support and confidence
# values, to become "good recommendation rules". Adapt it for the case related
# to legal process senteces. What questions can be answered if one take the output
# of the algorithm? Consider 2 cases:
# 1) min_support and min_confidence are specified. What do the output associations
#  mean?
# 2 ) min_suport and min_confidence are not specified. Look at their values at
#  the output, considering some association.
#
# Remember that any rule has a form: antecedent ---> consequent
# In other words: if antecedent then consequent.
#

## This code is to perform analysis of question 1)
results = list(apriori(transactions_bd, min_support = 0.40, min_confidence = 0.7))
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
        rule+=1
    print("##################################################################")


## This code is to perform analysis of question 2)
print('*************************************************************************************')
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
    print("##################################################################")

