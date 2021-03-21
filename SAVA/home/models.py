from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """This will be the main page"""
    template = 'home/home_page.html'
    max_count = 1

    main_page_title = models.CharField(max_length=400, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("main_page_title")
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
