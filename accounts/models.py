from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaLanguageBaseProfile
# Create your models here.
class MyProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    events_assisted = models.IntegerField(_('Events already assisted'),null=True
                                       ) 

class Attendee(models.Model):
    profile = models.ForeignKey(MyProfile)
    #Extra fields here
    class Meta:
        db_table = 'attendee'

class Organizer(models.Model):
    profile = models.ForeignKey(MyProfile)
    #Extra fields here
    class Meta:
        db_table = 'organizer'

@property
def full_name(self):
    return "%s %s" % (self.user.first_name, self.user.last_name)
