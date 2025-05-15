from django import template

register = template.Library()

@register.filter
def groupby(value, n):
    """
    Group a list into sublists of n items
    Example: {{ mylist|groupby:3 }} -> [[item1, item2, item3], [item4, item5, item6], ...]
    """
    try:
        n = int(n)
        if not value:  # Handle None or empty list
            return []
        return [value[i:i + n] for i in range(0, len(value), n)]
    except (ValueError, TypeError, AttributeError):
        return [] 