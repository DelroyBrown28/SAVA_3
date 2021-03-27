from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """This will eventually become the Testimonials Block"""
    title = blocks.CharBlock(required=True, help_text="Add Title")
    text = blocks.TextBlock(required=True, help_text="add some text")

    class Meta:
        template = "blocks/title_and_text_block.html"
        icon = 'edit'
        label = 'Title & Text'


class ServiceCardBlock(blocks.StructBlock):
    """Cards that display services"""
    service_title = blocks.CharBlock(required=True, help_text="Add Title")

    service_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("service_card_icon", ImageChooserBlock()),
                ("service_title", blocks.RichTextBlock(
                    required=True, max_length=50)),
                ("service_item", blocks.RichTextBlock(
                    required=True, max_length=75)),
                ("button_page", blocks.PageChooserBlock(
                    required=False, help_text="Link to page on your website")),
                ("button_url", blocks.URLBlock(
                    required=False, help_text="Link to EXTERNAL URL")),
                ("button_text", blocks.TextBlock(required=True, max_length=25)),
            ]
        )
    )

    class Meta:
        template = "blocks/service_card_block.html"
        icon = 'image'
        label = 'Service Cards'


class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = 'blocks/richtext_block.html'
        icon = "doc-full"
        label = "Richtext"


class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = 'blocks/richtext_block.html'
        icon = "edit"
        label = "Simple Richtext"


class CTABlock(blocks.StructBlock):
    """This will eventually be the call to action on the home page"""

    title = blocks.CharBlock(required=True, max_length=100)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(
        required=True, default="Button Text", max_length=45)

    class Meta:
        template = 'blocks/cta_block.html'
        icon = 'image'
        label = 'Call To Action'


class TestimonialsBlock(blocks.StructBlock):
    testimonial_name = blocks.CharBlock(required=True, max_length=100)
    testimonial_message = blocks.RichTextBlock(required=True, max_length=214)

    class Meta:
        template = 'blocks/testimonials_block.html'
        icon = 'placeholder'
        label = 'Testimonial Card'
