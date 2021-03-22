from django.db import models
from streams import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class HomePage(Page):
    """This will be the main page"""
    template = 'home/home_page.html'
    max_count = 1

    main_page_title = models.CharField(max_length=400, blank=False, null=True)

    services_panels = StreamField(
        [
            ('services', blocks.ServiceCardBlock()),

        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("main_page_title"),
        StreamFieldPanel('services_panels'),
        
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
