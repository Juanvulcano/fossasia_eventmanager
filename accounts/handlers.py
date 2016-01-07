from django.conf import settings
from django.utils.translation import ugettext_noop as _

def create_notice_types(sender, **kwargs):
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType
        print "Creating notices for myapp"
        NoticeType.create("event_invite", _("A new event have been organize! Come and participate"), _("you have received an invitation"))
    else:
        print "Skipping creation of NoticeTypes as notification app not found"

