# Software Parts
from django.db import models
from django.contrib import admin

from openPLM.plmapp.models import Part
from openPLM.plmapp.controllers import PartController
from openPLM.plmapp.utils import get_next_revision
# end of imports

# class Software
class Software(Part):

    # Software fields
    #nb_wheels = models.PositiveIntegerField("Number of wheels", default=lambda: 2)
    #color = models.CharField(max_length=25, blank=False)
    details = models.TextField(blank=False)
    
    # Software properties
    @property
    def attributes(self):
        attrs = list(super(Software, self).attributes)
        #attrs.extend(["nb_wheels", "color", "details"])
        attrs.extend(["details"])
        return attrs

    # excluded_creation_fields
    @classmethod
    def excluded_creation_fields(cls):
        return super(Software, cls).excluded_creation_fields() + ["details"]

# end Software

admin.site.register(Software)

# class SoftwareController
class SoftwareController(PartController):

    def revise(self, new_revision):
        if new_revision == get_next_revision(get_next_revision(self.revision)):
            self.details += """
            ----------------
            hello easter egg
            ----------------
            """
            self.save()
        return super(SoftwareController, self).revise(new_revision)

# end SoftwareController

