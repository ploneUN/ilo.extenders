from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from ilo.extenders import MessageFactory as _


class IEvalTheme(form.Schema):
    """
       Marker/Form interface for Eval Theme
    """

    # -*- Your Zope schema definitions here ... -*-
    eval_theme = schema.List(
        title=_(u'Themes'),
        description=_(u''),
        value_type=schema.Choice(vocabulary='ilo.vocabulary.evalthemes'),
        required=False,
        )

alsoProvides(IEvalTheme, IFormFieldProvider)
