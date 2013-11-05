from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces import IATContentType
from zope.interface import Interface
from five import grok
from ilo.extenders.interfaces import IProductSpecific, IILOThemeEnabled
from ilo.extenders import MessageFactory as _

# Visit http://pypi.python.org/pypi/archetypes.schemaextender for full 
# documentation on writing extenders

class ExtensionLinesField(ExtensionField, atapi.LinesField):
    pass

class ILOTheme(grok.Adapter):

    # This applies to all AT Content Types, change this to
    # the specific content type interface you want to extend
    grok.context(IILOThemeEnabled)
    grok.name('ilo.extenders.ilo_theme')
    grok.implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    grok.provides(IOrderableSchemaExtender)

    layer = IProductSpecific

    fields = [
        # add your extension fields here
        ExtensionLinesField(
            name='ilo_themes',
            widget=atapi.MultiSelectionWidget(
                label="ILO Themes",
                description="Select the related themes. Hold CTRL to make multiple selections.",
            ),
            vocabulary_factory='ilo.vocabulary.themes',
            multiValued=1,
        )
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, schematas):
        # you may reorder the fields in the schemata here
        return schematas
