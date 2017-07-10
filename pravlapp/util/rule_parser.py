from textx.exceptions import TextXSyntaxError
from textx.metamodel import metamodel_from_file

from pravlapp.rule.parsed_rule import ParsedRule


def parse_rule(definition):
    rule_mm = metamodel_from_file('metamodel/rule.tx')
    try:
        rule_model = rule_mm.model_from_str(definition)
    except TextXSyntaxError:
        return None

    rule = ParsedRule()
    rule.interpret(rule_model)
    return rule
