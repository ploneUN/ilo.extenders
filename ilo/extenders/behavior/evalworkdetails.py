from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from ilo.extenders import MessageFactory as _

class IEvalWorkDetails(form.Schema):
    
    worked_with_eval = schema.Bool(
        title = _(u"Has worked with EVAL"),
        default = False,
        required = False,
    )
    
    has_alert = schema.Bool(
        title = _(u"Alert Status"),
        default = False,
        required = False,
    )
    
    contact_eval = schema.Bool(
        title = _(u"Contact EVAL"),
        default = False,
        required = False,
    )
    
alsoProvides(IEvalWorkDetails,IFormFieldProvider)
    