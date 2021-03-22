from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """This will eventually become the Testimonials Block"""
    title = blocks.CharBlock(required=True, help_text="Add Title")
    text = blocks.TextBlock(required=True, help_text="add some text")

    class Meta:
        template = "blocks/title_and_text_block.html"
        icon = 'edit'
        label = 'Title & Text'


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
