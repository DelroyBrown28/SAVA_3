from django.db import models
from streams import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel


class HomePage(Page):
    """This will be the main page"""
    template = 'home/home_page.html'
    max_count = 1

    main_page_title = models.CharField(max_length=400, blank=False, null=True)
    main_page_subtitle = RichTextField(features=["bold", "italic"])
    main_page_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    card_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content = StreamField(
        [
            ("service_cards", blocks.ServiceCardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("main_page_title"),
        FieldPanel("main_page_subtitle"),
        ImageChooserPanel("main_page_background_image"),
        PageChooserPanel("card_cta"),
        StreamFieldPanel("content"),
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


