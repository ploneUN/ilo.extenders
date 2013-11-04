from collective.grok import gs
from ilo.extenders import MessageFactory as _

@gs.importstep(
    name=u'ilo.extenders', 
    title=_('ilo.extenders import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.extenders.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
