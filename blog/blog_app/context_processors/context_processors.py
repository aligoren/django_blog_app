from ..models import Page

def pages_processor(request):
    pages = Page.objects.filter(active=True)

    return { 'pages': pages }