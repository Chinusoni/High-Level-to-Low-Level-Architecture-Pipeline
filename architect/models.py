# architect/models.py
from django.db import models

class Blueprint(models.Model):
    requirement = models.TextField()
    modules = models.JSONField()       # To store list of modules
    schema_sql = models.TextField()    # To store SQL code
    pseudocode = models.TextField()    # To store logic
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Spec for: {self.requirement[:30]}..."