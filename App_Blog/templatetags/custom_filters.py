from django import template

register = template.Library()


def custom_filter(value):
    return value[0:500]+"............................"


register.filter('range_filter',custom_filter)