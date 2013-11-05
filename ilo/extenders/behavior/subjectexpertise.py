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

class ISubjectExpertise(form.Schema):
    """
       Marker/Form interface for Subject Expertise
    """

    # -*- Your Zope schema definitions here ... -*-

    subject_expertise = schema.List(
        title=u'Subject Expertise',
        required=False,
        value_type = schema.Choice(vocabulary='ilo.vocabularies.subject_expertise')
    )

alsoProvides(ISubjectExpertise,IFormFieldProvider)
