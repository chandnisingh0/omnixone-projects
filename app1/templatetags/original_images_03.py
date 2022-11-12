from django import template

register = template.Library()


@register.simple_tag
def get_original_image_view_03(product, password):
    return product.get_original_image_view_03(password)
