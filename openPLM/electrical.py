# Electrical Parts
from django.db import models
from django.contrib import admin

from openPLM.plmapp.models import Part
from openPLM.plmapp.controllers import PartController
from openPLM.plmapp.utils import get_next_revision
# end of imports

# class Electrical
class Electrical(Part):

    # Electrical fields
    #nb_wheels = models.PositiveIntegerField("Number of wheels", default=lambda: 2)
    #color = models.CharField(max_length=25, blank=False)
    details = models.TextField(blank=False)
    
    # Electrical properties
    @property
    def attributes(self):
        attrs = list(super(Electrical, self).attributes)
        #attrs.extend(["nb_wheels", "color", "details"])
        attrs.extend(["details"])
        return attrs

    # excluded_creation_fields
    @classmethod
    def excluded_creation_fields(cls):
        return super(Electrical, cls).excluded_creation_fields() + ["details"]

# end Electrical

admin.site.register(Electrical)

# class ElectricalController
class ElectricalController(PartController):

    def revise(self, new_revision):
        if new_revision == get_next_revision(get_next_revision(self.revision)):
            self.details += """
            ----------------
            hello easter egg
            ----------------
            """
            self.save()
        return super(ElectricalController, self).revise(new_revision)

# end ElectricalController

