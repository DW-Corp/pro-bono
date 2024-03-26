from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField

# Create your models here.

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    api_fields = [
        APIField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    # Only allow BlogPages beneath this page.
    subpage_types = ['blog.BlogIndexPage']

class BlogPage(Page):
    #Different from the real publication date,
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    api_fields = [
        APIField('date'),
        APIField('intro'),
        APIField('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    # Only allow this page to be created beneath a BloIndexPage
    parent_page_types = ['blog.BlogIndexPage']



