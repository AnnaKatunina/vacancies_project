from django import template

register = template.Library()


@register.filter
def salary_space(value):
    return '{:,}'.format(value).replace(',', ' ')
