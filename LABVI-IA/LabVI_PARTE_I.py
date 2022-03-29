
class Rule:
    """Create Rules to be tested

    Parameters
    ----------
    relation : String
        Logical operator (>=, ==, <=, >, <, !)
    percept_ref : String
        Define the Reference to role (37.5, 'loss taste', ...)
    percept_name: String
        Rule Name to be tested
    action: String
       Result when the relation matches with the percept_ref
    """
    def __init__(self, relation, percept_ref, percept_name, action): # Contructor
        self.percept_name = percept_name                               #self = this
        self.percept_ref = percept_ref
        self.relation = relation
        self.action = action

    def __str__(self): # Contructor
        return "Rule(relation: '{}', percept_ref: '{}', percept_name: '{}',  action: '{}')".format(self.relation, self.percept_ref, self.percept_name, self.action)

class Inference:
    """Create Rules to be tested

    Parameters
    ----------
    rules : List<Rule>
        Define an list of rules to be tested
    operators : List<String>
        Define the operator between the roles
    action: String
        Result when 
    rule_percept_names: Set<String>
        The name of rules tested
    """
    def __init__(self, rules, operators, action):
        self.rules = rules
        self.operators = operators
        self.action = action
        self.rule_percept_names = set() # builds the rule's percept names set to compare it # to percept inputs.
        print("init rule_percept_names with values from rules")    
        for rule in rules:
            print(f'adding rule {rule} on rule_percept_names')
            self.rule_percept_names.add(rule.percept_name) #From Rule {relation, percept_ref, percept_name, action}


    def infer(self, percepts): #verify if percepts match rules's percept names
        keys = percepts.keys() #get keys as in key-value = "temperature":"38.5" from percepts
        print(f'keys: "{keys}"')
        print(f'rule_percept_names: "{self.rule_percept_names}"') # rule_percept_names is an attribute from class Inference

        if self.rule_percept_names.issubset(keys): # validate rule_percept_names is in keys, se os valores de rule_percept_names estão contidos no keys
            rule_actions = [] # store result from test in every Rule
            # commando "len(self.rules)" returns size of list rules
            # range(len(self.rules)) retorna um array com todos os número de 0 até o tamanho da lista
            print(f'len(self.rules): "{len(self.rules)}""')
            print(f'range(len(self.rules)): "{range(len(self.rules))}"')
            for i in range(len(self.rules)):
                print(f'i: {i}')
                print(f'self.rules[i]: {self.rules[i]}')
                print(f'self.rules[i].percept_name {self.rules[i].percept_name}')
                print(f'percepts[self.rules[i].percept_name] {percepts[self.rules[i].percept_name]}')
                print(f'self.rules[i].relation: {self.rules[i].relation}')
                print(f'self.rules[i].percept_ref: {self.rules[i].percept_ref}')
                print(f'eval(percepts[self.rules[i].percept_name] +" "+ self.rules[i].relation +" "+ self.rules[i].percept_ref): {eval(percepts[self.rules[i].percept_name] +" "+ self.rules[i].relation +" "+ self.rules[i].percept_ref)}')
                if eval(percepts[self.rules[i].percept_name] +" "+ self.rules[i].relation +" "+ self.rules[i].percept_ref):
                    rule_actions.append(self.rules[i].action)
                    print("Doctor Eval says (...)")
                else:
                    rule_actions.append('False')
                    print("Doctor Eval says (...)")
                print(rule_actions)
            if len(rule_actions) == 1:
                print("Doctor Eval says (...)")
                return rule_actions[0]
            else:
                current_inference = rule_actions[0]
                k = 1
                print(f'len(rule_actions){len(rule_actions)}')
                while k < len(rule_actions) and current_inference == 'True':
                    print(f'k: {k}')
                    print(f'current_inference: {current_inference}')
                    print(f'self.operators[k-1]:{self.operators[k-1]}')
                    print(f'rule_actions:{rule_actions}')
                    print(f'eval(str(current_inference) + " " +self.operators[k-1] +" "+ rule_actions[k]): {eval(str(current_inference) + " " +self.operators[k-1] +" "+ rule_actions[k])}')
                    current_inference = eval(str(current_inference) + " " +self.operators[k-1] +" "+ rule_actions[k])
                    ++k
                print(f'current_inference:{current_inference}')
                if eval(str(current_inference)):
                    return self.action
                else:
                    return False

        else:
            return False


# Usage example:

rule_1 = Rule(">=", "37.5", "temperature", "True")
rule_2 = Rule("==", "'loss of taste'", "taste", "True")
inference = Inference([rule_1, rule_2],["and"],["Covid"])
percepts = {"temperature":"38.5", "taste": "'loss of taste'", "breath":"'shortness of breath'"}
print(inference.infer(percepts))
