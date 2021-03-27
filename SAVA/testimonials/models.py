from django.db import models
from streams import blocks
# from wagtail.core import blocks
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import (FieldPanel,
                                         FieldRowPanel,
                                         InlinePanel,
                                         MultiFieldPanel,
                                         StreamFieldPanel)


class TestimonialFormField(AbstractFormField):
    page = ParentalKey(
        'TestimonialFormPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class TestimonialFormPage(AbstractEmailForm):
    template = 'testimonials/testimonials_page.html'

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Testimonial Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject")
        ], heading="Email Settings"),
    ]


class Testimonials(Page):
    template = 'testimonials/testimonials.html'

    testimonials_page_title = models.CharField(
        max_length=400, blank=False, null=True)
    testimonials_page_subtitle = RichTextField(features=["bold", "italic"])
    testimonials_page_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("testimonials", blocks.TestimonialsBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("testimonials_page_title"),
        FieldPanel("testimonials_page_subtitle"),
        ImageChooserPanel("testimonials_page_background_image"),
        StreamFieldPanel("content"),
    ]

    # testimonial_name = models.CharField(blank=False, null=True, max_length=75)
    # testimonial_message = RichTextField(
    #     features=["bold", "italic"], default="Paste message here...")
    # content_panels = Page.content_panels + [
        # MultiFieldPanel([
        #     FieldRowPanel([
        #         FieldPanel('testimonial_name', classname='col12'),
        #         FieldPanel('testimonial_message', classname='col12'),
        #     ]),
        # ], heading="Testimonial Card"),
    # ]
