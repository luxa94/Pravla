from textx.metamodel import metamodel_from_file
rule_mm = metamodel_from_file('rule.tx')

with open('sample.rule', 'r') as f:
    data = f.read()

rule_model = rule_mm.model_from_str(data)
