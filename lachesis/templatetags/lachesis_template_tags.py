from django import template
from lachesis.models import Genre

register = template.Library()

@register.inclusion_tag('lachesis/gens.html')
def get_genre_list(gen=None):
    return {'gens': Genre.objects.all(), 'act_gen': gen}
