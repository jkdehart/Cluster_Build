# Mechanical Parts
from django.db import models
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from openPLM.plmapp.models import Part, ParentChildLinkExtension, register_PCLE
#from openPLM.plmapp.controllers import PartController
#from openPLM.plmapp.utils import get_next_revision
# end of imports

def register(cls):
    try:
        admin.site.register(cls)
    except admin.sites.AlreadyRegistered:
        pass

# class Mechanical
class Mechanical(Part):

    # Mechanical fields
    #nb_wheels = models.PositiveIntegerField("Number of wheels", default=lambda: 2)
    #color = models.CharField(max_length=25, blank=False)
    details = models.TextField(blank=False)
    
    # Mechanical properties
    #@property
    #def attributes(self):
    #    attrs = list(super(Mechanical, self).attributes)
    #    #attrs.extend(["nb_wheels", "color", "details"])
    #    attrs.extend(["details"])
    #    return attrs
		
		
	@property
    def attributes(self):
        attrs = ["details"]
        return super(Mechanical, self).attributes + attrs

    # excluded_creation_fields
    #@classmethod
    #def excluded_creation_fields(cls):
        #return super(Mechanical, cls).excluded_creation_fields() + ["details"]

# end Mechanical

register(Mechanical)

# class MechanicalController
class MechanicalController(PartController):

    def revise(self, new_revision):
        if new_revision == get_next_revision(get_next_revision(self.revision)):
            self.details += """
            ----------------
            hello easter egg
            ----------------
            """
            self.save()
        return super(MechanicalController, self).revise(new_revision)

# end MechanicalController

