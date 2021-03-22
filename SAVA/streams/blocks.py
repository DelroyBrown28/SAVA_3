from wagtail.core import blocks


class ServiceCardBlock(blocks.StructBlock):
    service_title = blocks.CharBlock(
        required=True, help_text="Add the title of the service you're offering")

    service_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('service_item', blocks.TextBlock(required=True, max_length=55)),
            ]
        )
    )
    
    class Meta:
        template = 'blocks/service_card_block.html'
        icon = 'placeholder'
        label = 'Services'
