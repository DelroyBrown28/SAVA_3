from django.db import models
from wagtail.core import blocks

from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (FieldPanel,
                                         FieldRowPanel,
                                         InlinePanel,
                                         MultiFieldPanel)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (AbstractEmailForm,
                                          AbstractFormField)
from wagtailcaptcha.models import WagtailCaptchaEmailForm


class FormField(AbstractFormField):
    contact_form = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):
    template = 'contact/contact_page.html'

    form_intro = RichTextField(blank=True)
    contact_page_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('form_intro', classname='form-intro-text'),
        ImageChooserPanel('contact_page_background_image'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel("subject"),
        ], heading="Form Settings"),
    ]
